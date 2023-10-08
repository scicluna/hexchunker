import HexSkeleton from "./Hex/HexSkeleton"

type LoadingProps = {
    islandChainSize: number
}

export default function LoadingWorld({ islandChainSize }: LoadingProps) {
    const HEXSIZE = 20
    const CHUNKDIMENSIONS = 10
    const islandChain = Array.from({ length: 8 }, () => Array(100).fill(""));
    return (
        <section className="h-screen w-fit grid grid-cols-[repeat(4,1fr)] overflow-hidden">
            {islandChain && islandChain.map((island, islandNumber) => (
                <div className={`grid grid-cols-[repeat(10,1fr)] h-[${HEXSIZE}rem] max-w-fit`} key={islandNumber}>
                    {island.map((tile, i) => (
                        <HexSkeleton pos={i} size={HEXSIZE} chunkSize={CHUNKDIMENSIONS} key={`${islandNumber + '-' + tile.pos}`} />
                    ))}
                </div>
            ))}
        </section>
    )
}