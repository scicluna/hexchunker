import { readFile, readdir } from 'fs/promises';
import * as path from 'path';

export async function readJsonChunks() {
    const files = await readdir(path.join(__dirname, '../../../public/_islands/processed'));
    const jsonFiles = files.filter(file => file.endsWith('.json'));

    const islandObjects = [];
    for (const file of jsonFiles) {
        const content = await readFile(path.join(__dirname, '../../../public/_islands/processed', file), 'utf-8');
        const islandObject = await JSON.parse(content);
        islandObjects.push(islandObject);
    }

    return islandObjects;
}