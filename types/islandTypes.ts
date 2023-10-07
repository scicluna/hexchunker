export type Island = {
    chunk: number
    pos: number
    terrain: Terrain
    features: string
    encounter: string
    history: string[]
}

export type Terrain = 'F' | 'H' | 'M' | 'O' | 'P' | 'T'