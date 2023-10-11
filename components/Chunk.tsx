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
    const chunkRef = useRef<Island[]>(island) //allow for mutable adjacent hexes / live updates to adjacent hex histories
    const HEXSIZE = 20 //rems
    const CHUNKDIMENSIONS = Math.floor(Math.sqrt(island.length)) //size noted by generator

    return (
        <div className={`h-[${HEXSIZE}rem] max-w-fit gap-x-[1px] grid`} style={{ gridTemplateColumns: `repeat(${CHUNKDIMENSIONS}, 1fr)` }} key={islandNumber}>
            {chunkRef.current.map((tile, i) => (
                <Hex tile={tile} chunkno={islandNumber} adjHexes={getAdjacentHexes(i, CHUNKDIMENSIONS, chunkRef.current)} image={imagePick(tile.terrain)} size={HEXSIZE} chunkSize={CHUNKDIMENSIONS} key={`${islandNumber + '-' + i}`} />
            ))}
        </div>
    )
}