# Generated on 2025-06-23 14:42:40

- ##Model: compound-beta
- ##Question: Find AI based automated web app penetesting tools that are opnsource and utilize google gemini api 

Based on the search results and analysis, I have found a few tools and resources that might be relevant to AI-based automated web app penetration testing tools that are open-source and utilize the Google Gemini API.

1. **PentestGPT**: This is an open-source penetration testing tool that can utilize the Google Gemini API among other models. It is designed to streamline and automate the testing process. PentestGPT provides a unified terminal input for web penetration testing and guides users interactively through testing processes. It relies on the OpenAI API to achieve high-quality reasoning and can be installed using pip.

2. **QAutomator**: Although primarily focused on mobile apps, QAutomator is an AI-powered application that could potentially be adapted or serve as inspiration for web app testing. It is designed to automate the testing process for mobile apps.

3. **Browser Use Tool**: This tool integrates AI models like Gemini with LangChain for customizable workflows, which could be used for web app testing.

4. **Open-Source Deep Research Tool**: While not directly focused on penetration testing, this guide shows how to build an open-source tool with the Gemini API, which could be adapted for penetration testing.

5. **Firebase AI Logic and Gemini API**: This provides a way to integrate the Gemini API into web apps with enhanced security features, which could be useful in the context of penetration testing.

Among these options, **PentestGPT** appears to be the most directly relevant tool for AI-based automated web app penetration testing that is open-source and utilizes the Google Gemini API. It is designed specifically for penetration testing, supports the Gemini API, and is available on GitHub for setup and use.

Therefore, the answer to the question "Find AI based automated web app penetration testing tools that are open-source and utilize Google Gemini API" is:

* **PentestGPT**: An open-source, AI-powered penetration testing tool that utilizes the Google Gemini API and is designed to automate and guide the penetration testing process interactively. 

You can find more information and setup instructions for PentestGPT on its GitHub repository: https://github.com/GreyDGL/PentestGPT. 

Additionally, other tools and resources like QAutomator, Browser Use Tool, Open-Source Deep Research Tool, and Firebase AI Logic with Gemini API might be useful for adapting or inspiring web app testing solutions, but PentestGPT is the most directly relevant tool based on the current information. 

Here is a code snippet to get started with PentestGPT:
```python
# Install PentestGPT
pip3 install git+https://github.com/GreyDGL/PentestGPT

# Configure API keys
export OPENAI_API_KEY='your_key_here'  # For OpenAI models
export GOOGLE_API_KEY='your_key_here'  # For Gemini models
export DEEPSEEK_API_KEY='your_key_here'  # For Deepseek models

# Test connection
pentestgpt-connection

# Start PentestGPT with default settings (GPT-4o)
pentestgpt
```
Please note that you need to replace `'your_key_here'` with your actual API keys for the respective models. 

Also, keep in mind that PentestGPT is for educational purposes only, and the author does not condone any illegal use. Always ensure that you have the necessary permissions and follow ethical guidelines when performing penetration testing.