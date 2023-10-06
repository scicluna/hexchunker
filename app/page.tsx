import type { Island } from "@/types/islandTypes";
import World from "@/components/World";
import { readText } from "@/utils/readText";


export default async function Main() {
  const islandChain: Island[][] = await readText();
  console.log("chunks", islandChain.length)

  return (
    <main className="w-fit h-fit">
      <World islandChain={islandChain} />
    </main>
  )
}
