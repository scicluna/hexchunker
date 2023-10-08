import type { Island } from "@/types/islandTypes";
import World from "@/components/World";
import { readJsonChunks } from "@/utils/readJsonChunks";


export default async function Main() {
  const islandChain: Island[][] = await readJsonChunks();

  return (
    <main className="w-fit h-fit">
      <World islandChain={islandChain} />
    </main>
  )
}
