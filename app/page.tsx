import type { Island } from "@/types/islandTypes";
import MainStage from "@/components/MainStage";
import { readText } from "@/utils/readText";


export default async function Main() {

  const islandChain: Island[][] = await readText();

  return (
    <main>
      <MainStage islandChain={islandChain} />
    </main>
  )
}
