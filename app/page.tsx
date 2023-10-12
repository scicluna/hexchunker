import type { Island } from "@/types/islandTypes";
import World from "@/components/World";
import { readJsonChunks } from "@/utils/readJsonChunks";
import { readBiome } from "@/utils/readBiome";


export default async function Main() {
  const islandChain: Island[][] = await readJsonChunks();
  const biome = await readBiome();

  return (
    <main className="w-fit h-fit">
      <World islandChain={islandChain} biome={biome} />
    </main>
  )
}
