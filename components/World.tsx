import { Island } from "@/types/islandTypes"
import Hex from "./Hex/Hex"
import { Suspense } from "react"

type MainStageProps = {
    islandChain: Island[][]
}

export default function World({ islandChain }: MainStageProps) {
    const HEXSIZE = 20
    const CHUNKDIMENSIONS = 10
    return (
        <main className="grid grid-cols-[repeat(10,1fr)]">
            {islandChain && islandChain.map((island, islandNumber) => (
                <div className={`grid grid-cols-[repeat(10,1fr)] h-[${HEXSIZE}rem] max-w-fit`} key={islandNumber}>
                    <Suspense>
                        {island.map(tile => (
                            <Hex tile={tile} size={HEXSIZE} chunkSize={CHUNKDIMENSIONS} key={`${islandNumber + '-' + tile.pos}`} />
                        ))}
                    </Suspense>
                </div>
            ))}
        </main>
    )
}