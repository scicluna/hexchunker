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
        <div ref={chatContainer}>

        </div>
    )
}