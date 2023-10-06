import LoadingWorld from "@/components/LoadingWorld";

export default async function Loading() {
    const islandChainSize = 120
    return (
        <main className="bg-black">
            <LoadingWorld islandChainSize={islandChainSize} />
        </main>
    )
}