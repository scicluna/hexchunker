import Hex from "./Hex/Hex"

type MainStageProps = {
    islandChain: string[]
}

export default function MainStage({ islandChain }: MainStageProps) {
    const HEXSIZE = 20
    return (
        <main className="flex flex-col">
            {islandChain && islandChain.map((row, rowIndex) => (
                <div className={`flex h-[${HEXSIZE}rem] min-w-fit`} key={rowIndex}
                    style={{ marginBottom: `${-HEXSIZE * .25}rem`, marginLeft: `${rowIndex % 2 === 0 ? HEXSIZE * .503 : 0}rem` }} >
                    {row.replace("\r", "").split("").map((char, islandIndex) => (
                        <Hex char={char} size={HEXSIZE} key={rowIndex + islandIndex} />
                    ))}
                </div>
            ))}
        </main>
    )
}