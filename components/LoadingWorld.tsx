import HexSkeleton from "./Hex/HexSkeleton"

type LoadingProps = {
    islandChainSize: number
}

export default function LoadingWorld({ islandChainSize }: LoadingProps) {
    const HEXSIZE = 20
    const CHUNKDIMENSIONS = 10
    const islandChain = Array.from({ length: islandChainSize }, () => Array(100).fill(""));
    return (
        <main className="grid grid-cols-[repeat(10,1fr)]  bg-gradient-to-r from-transparent via-rose-50/10 to-transparent -translate-x-full animate-[shimmer_3s_infinite]">
            {islandChain && islandChain.map((island, islandNumber) => (
                <div className={`grid grid-cols-[repeat(10,1fr)] h-[${HEXSIZE}rem] max-w-fit`} key={islandNumber}>
                    {island.map((tile, i) => (
                        <HexSkeleton pos={i} size={HEXSIZE} chunkSize={CHUNKDIMENSIONS} key={`${islandNumber + '-' + tile.pos}`} />
                    ))}
                </div>
            ))}
        </main>
    )
}