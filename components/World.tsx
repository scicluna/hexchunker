import { Island } from "@/types/islandTypes"
import Chunk from "./Chunk"

type MainStageProps = {
    islandChain: Island[][]
}

export default function World({ islandChain }: MainStageProps) {
    const CHAINCOL = Math.floor(Math.sqrt(islandChain.length))
    return (
        <main className={`h-full w-fit grid`} style={{ gridTemplateColumns: `repeat(${CHAINCOL}, 1fr)` }}>
            {islandChain && islandChain.map((island, islandNumber) => (
                <Chunk key={islandNumber} island={island} islandNumber={islandNumber} />
            ))}
        </main>
    )
}