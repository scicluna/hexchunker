"use client"
import style from './Hex.module.css'

type HexSkeletonProp = {
    size: number
    pos: number
    chunkSize: number
}

export default function HexSkeleton({ pos, size, chunkSize }: HexSkeletonProp) {
    return (
        <div style={{
            "--hex-size": `${size}rem`, marginBottom: `${-size * .25}rem`,
            marginLeft: `${Math.floor(pos / chunkSize) % 2 === 0 ? size * (1.732 / 2 / 2) : 0}rem`,
            marginRight: `${Math.floor(pos / chunkSize) % 2 === 0 ? -size * (1.732 / 2 / 2) : 0}rem`
        } as React.CSSProperties}
            className={`relative ${style.hexagon} bg-white`} >
            <div />
        </div>
    )
}