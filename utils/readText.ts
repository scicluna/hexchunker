import { readFile, readdir } from 'fs/promises';
import * as path from 'path';

export async function readText() {
    const files = await readdir(path.join(__dirname, '../../../public/_islands/processed'));
    const jsonFiles = files.filter(file => file.endsWith('.json'));

    jsonFiles.sort(() => Math.random() - 0.5);

    const islandObjects = [];
    for (const file of jsonFiles) {
        const content = await readFile(path.join(__dirname, '../../../public/_islands/processed', file), 'utf-8');
        const islandObject = await JSON.parse(content);
        islandObjects.push(islandObject);
    }

    return islandObjects;
}