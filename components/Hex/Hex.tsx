import style from './Hex.module.css'
import Image, { StaticImageData } from 'next/image'
import { Island } from '@/types/islandTypes'
import HexPop from './HexPop'
import { AdjacentHexes } from '@/utils/getAdjacentHexes'

type HexProps = {
    tile: Island
    chunkno: number
    size: number
    chunkSize: number
    adjHexes: AdjacentHexes
    image: StaticImageData
    biome: string
}

export default function Hex({ tile, chunkno, size, chunkSize, adjHexes, image, biome }: HexProps) {
    return (
        <div style={{
            "--hex-size": `${size}rem`, marginBottom: `${-size * .25}rem`,
            marginLeft: `${Math.floor(tile.pos / chunkSize) % 2 === 0 ? size * (1.732 / 2 / 2) : 0}rem`,
            marginRight: `${Math.floor(tile.pos / chunkSize) % 2 === 0 ? -size * (1.732 / 2 / 2) : 0}rem`
        } as React.CSSProperties}
            className={`relative ${style.hexagon}`} >
            <div className='relative h-full w-full point cursor-pointer hover:scale-105 hover:animate-pulse transition-all'>
                <Image src={image} alt={'map tile'} height={(size) * 17} width={(size * (1.732 / 2)) * 17} unoptimized className='w-auto h-full aspect-auto absolute bottom-0 cursor-pointer pointer-events-none' />
                <HexPop tile={tile} adjHexes={adjHexes} hexImage={image} chunkno={chunkno} size={size} biome={biome} />
            </div>
        </div>
    )
}