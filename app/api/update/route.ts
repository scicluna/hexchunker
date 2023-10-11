import { NextRequest } from "next/server";
import fs from "fs/promises"
import path from "path";

export async function POST(req: NextRequest) {
    const parsedreq = await req.json()
    let { newMessage, filename, pos } = parsedreq

    const filePath = path.join(process.cwd(), "public", "_islands", "processed", filename);

    console.log(filePath, "updated!")
    try {
        const fileContentRaw = await fs.readFile(filePath, "utf8");
        const fileContent = JSON.parse(fileContentRaw);

        // Assuming each chunk is an array of tiles.
        const targetTile = fileContent.find((t: any) => t.pos === pos);
        if (targetTile) {
            // Update the message or history or whichever property you want to.
            targetTile.history.push(newMessage);

            // Write the updated content back to the file.
            await fs.writeFile(filePath, JSON.stringify(fileContent, null, 4));

            return new Response('Success', { status: 200 })
        } else {
            return new Response("ERROR - TILE NOT FOUND", { status: 404 })
        }

    } catch (error) {
        return new Response("INTERNAL ERROR", { status: 400 })
    }
}