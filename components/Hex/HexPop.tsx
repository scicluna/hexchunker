import { Island } from "@/types/islandTypes"
import {
    Popover,
    PopoverContent,
    PopoverTrigger,
} from "@/components/ui/popover"
import style from './Hex.module.css'
import Image, { StaticImageData } from "next/image"
import HexWindow from "./HexWindow"
import { AdjacentHexes } from "@/utils/getAdjacentHexes"

type HexPopProps = {
    tile: Island
    adjHexes: AdjacentHexes
    chunkno: number
    size: number
    hexImage: StaticImageData
    biome: string
}

export default function HexPop({ tile, adjHexes, chunkno, size, hexImage, biome }: HexPopProps) {
    const terrainDict = {
        O: "Ocean",
        P: "Plains",
        H: "Hills",
        M: "Mountain",
        F: "Forest",
        T: "Town"
    }

    return (
        <Popover>
            <PopoverTrigger className="h-full w-full">Open</PopoverTrigger>
            <PopoverContent
                style={{ "--hex-size": `50vh` } as React.CSSProperties}
                className={`${style.hexagon} pt-[30%] font-mono`}>
                <Image src={hexImage} alt={"backsplash"} fill className="opacity-40" />
                <div className="text-[1vh] font-bold h-fit text-white">
                    <p>Tile: {`${chunkno}-${tile.pos}`}</p>
                    <p>Terrain: {`${terrainDict[tile.terrain]}`}</p>
                    <p>{tile.terrain === "T" ? `Name: ${tile.features}` : `Feature: ${tile.features || "None"}`}</p>
                    <p>Encounter: {tile.encounter || "None"}</p>
                    <HexWindow tile={tile} adjHexes={adjHexes} biome={biome} />
                </div>
            </PopoverContent>
        </Popover>
    )
}