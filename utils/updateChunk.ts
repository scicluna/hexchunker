import { Island } from "@/types/islandTypes";

export async function updateChunk(tile: Island, message: string) {
    console.log(message)
    await fetch('/api/update', {
        method: "POST",
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            newMessage: message,
            filename: `chunk_${tile.chunk}.json`,
            pos: tile.pos
        })
    })
}