import Hex from "./Hex/Hex"

type MainStageProps = {
    islandChain: string[]
}

export default function MainStage({ islandChain }: MainStageProps) {
    return (
        <main className="flex flex-col ">
            {islandChain && islandChain.map((row, rowIndex) => (
                <div className={`flex gap-[.1%] -mb-[3%]  ${rowIndex % 2 === 0 ? 'translate-x-[5%]' : ''}`} key={rowIndex}>
                    {row.replace("\r", "").split("").map((char, islandIndex) => (
                        <Hex char={char} key={rowIndex + islandIndex} />
                    ))}
                </div>
            ))}
        </main>
    )
}