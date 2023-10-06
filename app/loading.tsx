import LoadingWorld from "@/components/LoadingWorld";

export default async function Loading() {
    const islandChainSize = 120
    return (
        <main>
            <LoadingWorld islandChainSize={islandChainSize} />
        </main>
    )
}