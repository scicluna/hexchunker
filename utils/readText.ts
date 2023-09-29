import { readFile, writeFile } from 'fs/promises';
import * as path from 'path';

export async function readText() {
    return await readFile(path.join(__dirname, '../../../public/_islands/island1.txt'), 'utf-8')
}