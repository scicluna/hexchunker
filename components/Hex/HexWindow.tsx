"use client"
import { Island } from "@/types/islandTypes"
import { useChat } from "ai/react";
import { useEffect, useRef } from "react";

type HexWindowProps = {
    tile: Island
}

export default function HexWindow({ tile }: HexWindowProps) {
    const { messages, input, handleInputChange, handleSubmit, isLoading, } = useChat({});
    const chatContainer = useRef<HTMLDivElement>(null)

    useEffect(() => {
        if (!chatContainer.current) return;
        const { scrollHeight } = chatContainer.current;
        if (true) {
            chatContainer.current.scrollTo({
                top: scrollHeight,
                behavior: "smooth",
            });
        }
    }, [messages]);

    return (
        <div className="flex flex-col gap-2 h-full m-2 opacity-100">
            <div className="mini scrollbar w-full h-[16vh] overflow-y-scroll bg-slate-500 bg-opacity-20" ref={chatContainer}>
                {messages.map((m, i) => (
                    <div key={m.id} className='flex flex-col p-2'>
                        <p className='font-extrabold'>{m.role === 'user' ? 'User: ' : 'AI: '}</p>
                        <p>{m.content}</p>
                    </div>
                ))}
            </div>
            <form onSubmit={(e) => handleSubmit(e, {
                options: {
                    body: { details: JSON.stringify(tile) }
                }
            })} className='w-full flex gap-4 justify-center items-center relative z-50'>
                <input
                    autoComplete='off'
                    className="border border-gray-300 dark:border-slate-600 rounded shadow-xl p-2 w-1/2"
                    value={input}
                    onChange={handleInputChange}
                    name="prompt"
                    placeholder='Prompt the AI'
                />
                <button className='bg-purple-600 dark:text-gray-100 dark:bg-purple-950 px-4 py-2 rounded-full hover:bg-purple-500 hover:dark:bg-purple-800' type="submit" disabled={isLoading}>Send</button>
            </form>
        </div>
    )
}