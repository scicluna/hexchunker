import { Terrain } from '@/types/islandTypes'
import { forest, hills, mountains, ocean, plains } from '@/data/images'

export function imagePick(char: Terrain) {
    switch (char) {
        case "F": {
            return forest[Math.floor(Math.random() * forest.length)]
        }
        case "H": {
            return hills[Math.floor(Math.random() * hills.length)]
        }
        case "M": {
            return mountains[Math.floor(Math.random() * mountains.length)]
        }
        case "O": {
            return ocean[Math.floor(Math.random() * ocean.length)]
        }
        case "P": {
            return plains[Math.floor(Math.random() * plains.length)]
        }
        default: {
            return ocean[Math.floor(Math.random() * ocean.length)]
        }
    }
}