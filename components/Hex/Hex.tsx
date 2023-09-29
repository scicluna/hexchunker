import style from './Hex.module.css'
import Image from 'next/image'
import { imagePick } from '@/utils/imagePick'
import { Island } from '@/types/islandTypes'

export type char = 'F' | 'H' | 'M' | 'O' | 'P'
type HexProps = {
    tile: Island
    size: number
    chunkSize: number
}

export default function Hex({ tile, size, chunkSize }: HexProps) {

    const hexImage = imagePick(tile.terrain);
    return (
        <div style={{
            "--hex-size": `${size}rem`, marginBottom: `${-size * .25}rem`,
            marginLeft: `${Math.floor(tile.pos / chunkSize) % 2 === 0 ? size * .5 : 0}rem`,
            marginRight: `${Math.floor(tile.pos / chunkSize) % 2 === 0 ? -size * .5 : 0}rem`
        } as React.CSSProperties}
            className={`relative ${style.hexagon}`} >
            <div>
                <Image src={hexImage} alt={'map tile'} fill className='aspect-square' />
            </div>
        </div>
    )
}