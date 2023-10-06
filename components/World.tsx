import { Island } from "@/types/islandTypes"
import Hex from "./Hex/Hex"

type MainStageProps = {
    islandChain: Island[][]
}

export default function World({ islandChain }: MainStageProps) {
    const HEXSIZE = 20
    const CHUNKDIMENSIONS = 10 //MUST MATCH
    return (
        <main className="h-full w-fit grid grid-cols-[repeat(10,1fr)]">
            {islandChain && islandChain.map((island, islandNumber) => (
                <div className={`grid grid-cols-[repeat(10,1fr)] h-[${HEXSIZE}rem] max-w-fit gap-x-[1px]`} key={islandNumber}>
                    {island.map(tile => (
                        <Hex tile={tile} chunkno={islandNumber} size={HEXSIZE} chunkSize={CHUNKDIMENSIONS} key={`${islandNumber + '-' + tile.pos}`} />
                    ))}
                </div>
            ))}
        </main>
    )
}