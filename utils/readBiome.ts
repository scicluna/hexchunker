import { promises as fs } from 'fs'
import path from 'path'
export async function readBiome() {
    const narratives = {
        island: 'This chain of islands was once a continent of magical power and splendor, rendered apart by a grand catastrophy.',
        flat: 'A vast expanse of land - fantastical and untamed. The perfect place for adventure.',
        hilly: 'A place of rolling hills and valleys filled with mystery and wonder. Who knows what is hidden in these hills?',
        mountainous: 'A place of towering mountains and deep valleys. Monsters and treasure await those brave enough to explore.',
    }

    const biome = await fs.readFile(path.join(process.cwd(), "public", "generator", "processed", "biome.txt"), "utf8") as keyof typeof narratives

    if (!narratives.hasOwnProperty(biome)) return 'ERROR'
    return narratives[biome]
}