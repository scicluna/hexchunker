import { NextRequest } from 'next/server';
import { Message as VercelChatMessage, StreamingTextResponse } from 'ai';
import { ChatOpenAI } from 'langchain/chat_models/openai';
import { BytesOutputParser } from 'langchain/schema/output_parser';
import { PromptTemplate } from 'langchain/prompts';
export const runtime = 'edge';

const formatMessage = (message: VercelChatMessage) => {
    return `${message.role}: ${message.content}`;
};

const TEMPLATE = `
Rules:
{rules}
---
Meta Narrative:
{meta_narrative}
---
Surrounding Hex Information:
(ignore undefined hexes)
{adjacent}
---
Current Hex Information:
{details}
---
Current conversation:
{chat_history}
---
User: {input}
AI:`;

export async function POST(req: NextRequest) {
    const body = await req.json();
    const details = body.details
    const adjacent = body.adjacent
    const messages = body.messages ?? [];
    const formattedPreviousMessages = messages.slice(0, -1).map(formatMessage);
    const currentMessageContent = messages[messages.length - 1].content;

    const prompt = PromptTemplate.fromTemplate(TEMPLATE);

    const model = new ChatOpenAI({
        modelName: "gpt-4",
        temperature: 0.3,
    });

    const outputParser = new BytesOutputParser();
    const chain = prompt.pipe(model).pipe(outputParser);

    let ruleSet = "Craft a narrative linking the current hex with its adjacent hexes (pointy end on top). Think like a creative DM's Assistant embracing the unusual and aiding the DM (me, the User). Connect, describe, and surprise. Keep answers terse and formatted with bullet points (seperated by \n). Use adjacent hex information when appropriate"

    let metaNarrative = 'This chain of islands was once a continent of magical power and splendor, rendered apart by a grand catastrophy.'

    const stream = await chain.stream({
        rules: ruleSet,
        meta_narrative: metaNarrative,
        adjacent: adjacent,
        details: details,
        chat_history: formattedPreviousMessages.join('\n'),
        input: currentMessageContent,
    });

    return new StreamingTextResponse(stream);
}