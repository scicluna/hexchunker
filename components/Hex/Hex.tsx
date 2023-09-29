import style from './Hex.module.css'
import Image from 'next/image'
import { imagePick } from '@/utils/imagePick'

export type char = 'F' | 'H' | 'M' | 'O' | 'P'
type HexProps = {
    char: string
}

export default function Hex({ char }: HexProps) {
    const hexImage = imagePick(char as char);
    return (
        <div className={`relative hexagon ${style.hexagon}`}>
            <Image src={hexImage} alt={'map tile'} fill />
        </div>
    )
}