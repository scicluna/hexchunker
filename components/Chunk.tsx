"use client"
import Hex from "./Hex/Hex"
import { imagePick } from "@/utils/imagePick"
import { getAdjacentHexes } from "@/utils/getAdjacentHexes"
import { useRef } from "react"
import { Island } from "@/types/islandTypes"

type ChunkProps = {
    island: Island[]
    islandNumber: number
}

export default function Chunk({ island, islandNumber }: ChunkProps) {
    const chunkRef = useRef<Island[]>(island)
    const HEXSIZE = 20
    const CHUNKDIMENSIONS = 10 //MUST MATCH

    return (
        <div className={`grid grid-cols-[repeat(10,1fr)] h-[${HEXSIZE}rem] max-w-fit gap-x-[1px]`} key={islandNumber}>
            {chunkRef.current.map((tile, i) => (
                <Hex tile={tile} chunkno={islandNumber} adjHexes={getAdjacentHexes(i, CHUNKDIMENSIONS, chunkRef.current)} image={imagePick(tile.terrain)} size={HEXSIZE} chunkSize={CHUNKDIMENSIONS} key={`${tile.chunk + '-' + tile.pos}`} />
            ))}
        </div>
    )
}