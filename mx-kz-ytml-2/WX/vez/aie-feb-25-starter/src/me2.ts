/*
This file is form the following repo 
https://github.com/nicoalbanese/aie-feb-25-starter 
*/

// --- Imports Zone ---

import { groq } from "@ai-sdk/groq"
import { generateText } from "ai"
import boxen from "boxen"
import chalk from "chalk"
import "dotenv/config"

// --- Function Definitions ---

// This function is following the tutorial
export const main1 = async () => {
  const result = await generateText({
    model: groq("llama-3.3-70b-versatile"),
    messages: [
      {
        role: "user",
        content: "When was the AI engineer summit 2025",
      },
    ],
  })

  // Using boxen for boxes and chalk for color output
  console.log(chalk.bold.blue("Generated Recipe:"))
  const boxedMessage = boxen(result.text, {
    padding: 1,
    margin: 1,
    borderStyle: "round",
    borderColor: "yellow", // Optional background color
  })
  console.log(chalk.greenBright(boxedMessage))
  console.log(chalk.bold.green("✔ Operation completed"))
}

// Above function - Change Name to test

export const panty = async () => {
  const quez = "Explain Booty Dancing and Booty Candies, compare and constrast"

  const result = await generateText({
    model: groq("llama-3.3-70b-versatile"),
    messages: [
      {
        role: "user",
        content: quez,
      },
    ],
  })

  // Using boxen for boxes and chalk for color output
  console.log(chalk.bold.blue("Generated Recipe:"))
  const boxedMessage = boxen(result.text, {
    padding: 1,
    margin: 1,
    borderStyle: "round",
    borderColor: "yellow", // Optional background color
  })
  console.log(chalk.greenBright("Groq-llama-3.3-70b-versatile"))
  console.log(chalk.greenBright(boxedMessage))
  console.log(chalk.bold.green("✔ Operation completed"))
}
