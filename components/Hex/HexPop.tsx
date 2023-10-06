import { Island } from "@/types/islandTypes"
import {
    Popover,
    PopoverContent,
    PopoverTrigger,
} from "@/components/ui/popover"
import style from './Hex.module.css'
import Image, { StaticImageData } from "next/image"

type HexPopProps = {
    tile: Island
    chunkno: number
    size: number
    hexImage: StaticImageData
}

export default function HexPop({ tile, chunkno, size, hexImage }: HexPopProps) {

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
                className={`${style.hexagon} pt-[30%] font-mono`}
                onScroll={close}>
                <Image src={hexImage} alt={"backsplash"} fill className="opacity-40" />
                <div className="text-[1vh] font-bold opacity-100">
                    <p>Tile: {`${chunkno}-${tile.pos}`}</p>
                    <p>Terrain: {`${terrainDict[tile.terrain]}`}</p>
                    <p>{tile.terrain === "T" ? `Name: ${tile.features}` : `Feature: ${tile.features || "None"}`}</p>
                    <p>Encounter: {tile.encounter || "None"}</p>
                </div>
            </PopoverContent>
        </Popover>
    )
}