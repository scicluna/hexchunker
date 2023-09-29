import style from './Hex.module.css'
import Image from 'next/image'
import { imagePick } from '@/utils/imagePick'

export type char = 'F' | 'H' | 'M' | 'O' | 'P'
type HexProps = {
    char: string
    size: number
}

export default function Hex({ char, size }: HexProps) {
    const hexImage = imagePick(char as char);

    return (
        <div style={{ "--hex-size": `${size}rem` } as React.CSSProperties} className={`relative ${style.hexagon}`} >
            <div>
                <Image src={hexImage} alt={'map tile'} fill className='aspect-square' />
            </div>
        </div>
    )
}