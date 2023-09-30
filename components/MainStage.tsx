import { Island } from "@/types/islandTypes"
import Hex from "./Hex/Hex"

type MainStageProps = {
    islandChain: Island[][]
}

export default function MainStage({ islandChain }: MainStageProps) {
    const HEXSIZE = 20
    const CHUNKDIMENSIONS = 10
    return (
        <main className="grid grid-cols-[repeat(10,1fr)]">
            {islandChain && islandChain.map((island, islandNumber) => (
                <div className={`grid grid-cols-[repeat(10,1fr)] h-[${HEXSIZE}rem] max-w-fit`} key={islandNumber}>
                    {island.map(tile => (
                        <Hex tile={tile} size={HEXSIZE} chunkSize={CHUNKDIMENSIONS} key={`${islandNumber + '-' + tile.pos}`} />
                    ))}
                </div>
            ))}
        </main>
    )
}