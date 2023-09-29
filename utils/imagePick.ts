import { char } from "@/components/Hex/Hex";
import { forest, hills, mountains, ocean, plains } from '@/data/images'

export function imagePick(char: char) {
    switch (char) {
        case "F": {
            return forest[Math.floor(Math.random() * forest.length)]
        }
        case "H": {
            return hills[Math.floor(Math.random() * forest.length)]
        }
        case "M": {
            return mountains[Math.floor(Math.random() * forest.length)]
        }
        case "O": {
            return ocean[Math.floor(Math.random() * forest.length)]
        }
        case "P": {
            return plains[Math.floor(Math.random() * forest.length)]
        }
    }
}