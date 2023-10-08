"use client"
import { Island } from "@/types/islandTypes"
import { updateChunk } from "@/utils/updateChunk";
import { Message, useChat } from "ai/react";
import React, { useEffect, useRef, useState } from "react";

type HexWindowProps = {
    tile: Island
    adjHexes: Island[]
}

export default function HexWindow({ tile, adjHexes }: HexWindowProps) {
    const { messages, input, handleInputChange, handleSubmit, isLoading, } = useChat({
        onFinish: (async (message: Message) => {
            try {
                await updateChunk(tile, message.content)
                tile.history = [...tile.history, message.content]
            }
            catch (err) {
                console.log("something went wrong: ERROR")
            }
        })
    });

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
            <div className="relative z-50 mini scrollbar w-full h-[15vh] overflow-y-scroll bg-slate-500 bg-opacity-20 gap-1 flex flex-col p-1" ref={chatContainer}>
                <div className="flex flex-col gap-1">
                    <h3>History:</h3>
                    <hr />
                    {tile.history.map((history, x) => (
                        <React.Fragment key={`${tile.chunk}-${tile.pos}-${x}`}>
                            <p>{history}</p>
                            <hr />
                        </React.Fragment>
                    ))}
                </div>
                {messages.map((m, i) => (
                    <div key={m.id} className='flex flex-col p-2'>
                        <p className='font-extrabold'>{m.role === 'user' ? 'User: ' : 'AI: '}</p>
                        <p>{m.content}</p>
                    </div>
                ))}
            </div>
            <form onSubmit={(e) => {
                handleSubmit(e, {
                    options: {
                        body: { details: JSON.stringify(tile), adjacent: JSON.stringify(adjHexes) }
                    }
                })
            }}
                className='w-full flex gap-4 justify-center items-center relative z-50'>
                <input
                    autoComplete='off'
                    className="border border-gray-300 dark:border-slate-600 rounded shadow-xl p-2 w-1/2 text-black"
                    value={input}
                    onChange={handleInputChange}
                    name="prompt"
                    placeholder='Prompt the AI'
                />
                <button className=' bg-purple-600 dark:text-gray-100 dark:bg-purple-950 px-4 py-2 rounded-full hover:bg-purple-500 hover:dark:bg-purple-800' type="submit" disabled={isLoading}>Send</button>
            </form>
        </div>
    )
}