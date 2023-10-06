export type Island = {
    pos: number
    terrain: Terrain
    features: string
    encounter: string
}

export type Terrain = 'F' | 'H' | 'M' | 'O' | 'P' | 'T'