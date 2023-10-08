import { Island } from "@/types/islandTypes";

export function getAdjacentHexes(i: number, CHUNKDIMENSIONS: number, currentChunk: Island[]): Island[] {
    // Calculate the row and column of the hex with index i.
    let row = Math.floor(i / CHUNKDIMENSIONS);
    let col = i % CHUNKDIMENSIONS;

    // Calculate adjacent indices for a pointy-topped hex.
    let adjacent: [number, number][];
    if (row % 2 === 0) { // even rows
        adjacent = [
            [row - 1, col],   // top left
            [row - 1, col + 1], // top right
            [row, col - 1],   // left
            [row, col + 1],   // right
            [row + 1, col],   // bottom left
            [row + 1, col + 1]  // bottom right
        ];
    } else { // odd rows
        adjacent = [
            [row - 1, col - 1], // top left
            [row - 1, col],   // top right
            [row, col - 1],   // left
            [row, col + 1],   // right
            [row + 1, col - 1], // bottom left
            [row + 1, col]    // bottom right
        ];
    }

    // Convert adjacent coordinates back to indices and filter out any that are off the grid.
    return adjacent
        .filter(([adjRow, adjCol]) =>
            adjRow >= 0 && adjRow < CHUNKDIMENSIONS && adjCol >= 0 && adjCol < CHUNKDIMENSIONS)
        .map(([adjRow, adjCol]) => currentChunk[adjRow * CHUNKDIMENSIONS + adjCol])
        .filter(tile => tile !== undefined); // filter out any undefined tiles (just to be safe)
}
