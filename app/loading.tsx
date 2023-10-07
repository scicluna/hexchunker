import LoadingWorld from "@/components/LoadingWorld";

export default async function Loading() {
    const islandChainSize = 120
    return (
        <main className="bg-slate-500">
            <LoadingWorld islandChainSize={islandChainSize} />
        </main>
    )
}