import style from './Hex.module.css'
import Image, { StaticImageData } from 'next/image'
import { Island } from '@/types/islandTypes'
import HexPop from './HexPop'

type HexProps = {
    tile: Island
    chunkno: number
    size: number
    chunkSize: number
    image: StaticImageData
}

export default function Hex({ tile, chunkno, size, chunkSize, image }: HexProps) {
    return (
        <div style={{
            "--hex-size": `${size}rem`, marginBottom: `${-size * .25}rem`,
            marginLeft: `${Math.floor(tile.pos / chunkSize) % 2 === 0 ? size * (1.732 / 2 / 2) : 0}rem`,
            marginRight: `${Math.floor(tile.pos / chunkSize) % 2 === 0 ? -size * (1.732 / 2 / 2) : 0}rem`
        } as React.CSSProperties}
            className={`relative ${style.hexagon}`} >
            <div className='relative h-full w-full point cursor-pointer hover:scale-105 hover:animate-pulse transition-all'>
                <Image src={image} alt={'map tile'} fill className='aspect-square cursor-pointer pointer-events-none' unoptimized />
                <HexPop tile={tile} hexImage={image} chunkno={chunkno} size={size} />
            </div>
        </div>
    )
}