/* 
This will have various functions you are testing while doing the tutorial. 
*/

import { google } from "@ai-sdk/google"
import { groq } from "@ai-sdk/groq"
import { generateText } from "ai"
import boxen from "boxen"
import chalk from "chalk"
import "dotenv/config"
import { saveAsMarkdown } from "./wm"

export async function m1_main() {
  explainAtmosphereInGangstaRap()
}

///////////////////////////////////////////////////////////////
// Groq Usage
///////////////////////////////////////////////////////////////

// Query closed model from groq directly
export async function explainAtmosphereInGangstaRap() {
  try {
    const result = await generateText({
      model: groq("llama-3.3-70b-versatile"),
      prompt: "Explain what is atmosphere, in gangsta rap style",
    })

    console.log(chalk.bold.blue("🔥 Atmosphere, Gangsta Style:"))

    const boxedMessage = boxen(result.text, {
      padding: 1,
      margin: 1,
      borderStyle: "round",
      borderColor: "yellow",
    })

    console.log(chalk.greenBright(boxedMessage))
    console.log(chalk.bold.green("✔ Operation completed"))

    return result.text // Optional: return the response for reuse
  } catch (error) {
    console.error(chalk.red.bold("💥 Error:"), error.message)
    throw error
  }
}

// Query Compount Beta which also has web search
export async function compoundBetaTest() {
  try {
    const result = await generateText({
      model: groq("compound-beta"),
      messages: [
        {
          role: "user",
          content:
            "Explain the key points of the Iran-Israel War as of June 2025",
        },
      ],
    })

    console.log(chalk.bold.blue("🔥 Atmosphere, Gangsta Style:"))

    const boxedMessage = boxen(result.text, {
      padding: 1,
      margin: 1,
      borderStyle: "round",
      borderColor: "yellow",
    })

    console.log(chalk.greenBright(boxedMessage))
    console.log(chalk.greenBright(result.sources)) // Note if there are sources then it will be here
    console.log(chalk.bold.green("✔ Operation completed"))

    return result.text // Optional: return the response for reuse
  } catch (error) {
    console.error(chalk.red.bold("💥 Error:"), error.message)
    throw error
  }
}

///////////////////////////////////////////////////////////////
// Googel Usage
///////////////////////////////////////////////////////////////

// Query Compount Beta which also has web search
export async function googleSearchGrounding() {
  const quez = "Explain high profile hacks web 2 and web 3 as of 2025"

  try {
    const result = await generateText({
      model: google("gemini-2.5-flash-preview-04-17", {
        useSearchGrounding: true,
      }),
      messages: [
        {
          role: "user",
          content: quez,
        },
      ],
    })

    console.log(chalk.bold.blue("🔥 Atmosphere, Gangsta Style:"))

    const boxedMessage = boxen(result.text, {
      padding: 1,
      margin: 1,
      borderStyle: "round",
      borderColor: "yellow",
    })

    console.log(chalk.greenBright(boxedMessage))
    console.log(chalk.greenBright(result.sources)) // Note if there are sources then it will be here
    console.log(chalk.bold.green("✔ Operation completed"))

    // Save and write to markdown file in directory called rez
    saveAsMarkdown(result.text, {
      model: "gemini-2.5-flash",
      sources: result.sources,
      query: "Iran-Israel War June 2025",
      functionName: "googleSearchGrounding",
    })

    return result.text // Optional: return the response for reuse
  } catch (error) {
    console.error(chalk.red.bold("💥 Error:"), error.message)
    throw error
  }
}
