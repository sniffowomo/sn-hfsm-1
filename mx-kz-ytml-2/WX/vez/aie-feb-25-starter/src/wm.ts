// markdown-utils.ts
import fs from "fs"
import path from "path"
import { fileURLToPath } from "url"

const __dirname = path.dirname(fileURLToPath(import.meta.url))

export const saveAsMarkdown = (
  content: string,
  metadata: {
    model: string
    sources?: { url: string; title?: string }[]
    query?: string
    functionName?: string
  }
): string => {
  const now = new Date()
  const timestamp = now.toLocaleString()
  const filename = `${metadata.functionName || "output"}_${now
    .toISOString()
    .replace(/[:.]/g, "-")}.md`
  const filePath = path.join(__dirname, "rez", filename)

  const sourcesText = metadata.sources?.length
    ? metadata.sources
        .map((s) => `- [${s.title || "Source"}](${s.url})`)
        .join("\n")
    : "No sources available"

  const markdownContent = `# ${metadata.query || "Analysis"}

**Generated**: ${timestamp}  
**Model**: ${metadata.model}

## Content
${content}

## Sources
${sourcesText}
`

  fs.mkdirSync(path.dirname(filePath), { recursive: true })
  fs.writeFileSync(filePath, markdownContent)
  return filePath
}

// Header Function
import boxen from "boxen"
import chalk from "chalk"

/*
Function Usage 
printTutorialHeader("Tu1 - Main Tutorial Function Calls", "t1_main")
*/

export const printTutorialHeader = (msg: string, title: string) => {
  const boxedMessage = boxen(msg, {
    padding: 1,
    margin: 1,
    borderStyle: "round",
    borderColor: "greenBright",
    title: title,
  })
  console.log(chalk.bold.yellowBright(boxedMessage))
}
