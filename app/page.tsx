import { char } from "@/components/Hex/Hex";
import MainStage from "@/components/MainStage";
import { readText } from "@/utils/readText";

export default async function Main() {

  const island = await readText()
  const islandChain = island.replace("\r", "").split("\n")

  return (
    <main>
      <MainStage islandChain={islandChain} />
    </main>
  )
}
