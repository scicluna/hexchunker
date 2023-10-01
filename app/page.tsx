import type { Island } from "@/types/islandTypes";
import World from "@/components/World";
import { readText } from "@/utils/readText";


export default async function Main() {
  const islandChain: Island[][] = await readText();

  return (
    <main>
      <World islandChain={islandChain} />
    </main>
  )
}
