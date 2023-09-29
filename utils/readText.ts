import { readFile, writeFile } from 'fs/promises';
import * as path from 'path';

export async function readText() {
    const text = await readFile(path.join(__dirname, '../../../public/_islands/island1.txt'), 'utf-8')
    console.log(text)
    return text
}