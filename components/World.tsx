import { Island } from "@/types/islandTypes"
import Chunk from "./Chunk"

type MainStageProps = {
    islandChain: Island[][]
}

export default function World({ islandChain }: MainStageProps) {
    return (
        <main className="h-full w-fit grid grid-cols-[repeat(10,1fr)]">
            {islandChain && islandChain.map((island, islandNumber) => (
                <Chunk island={island} islandNumber={islandNumber} />
            ))}
        </main>
    )
}