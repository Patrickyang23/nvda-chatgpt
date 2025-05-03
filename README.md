# NVDA ChatGPT Hello World Add-on

This is a simple NVDA global plugin that allows users to press `NVDA+A` and receive a response from OpenAI’s ChatGPT. The response is shown in an **NVDA message box** and also accessible via screen reader.

## Features

- Press `NVDA+A` to send a fixed prompt (`"hello world"`) to ChatGPT.
- The reply is displayed in a popup **message box** using NVDA’s GUI.
- Uses OpenAI's REST API.
- API key is loaded securely from a `.env` file.
- Built using NVDA’s developer scratchpad (no packaging required).

## API Key Setup (`.env` File)

To use the OpenAI API securely:

1. **Create a `.env` file** in the same directory as `gpt_hello.py`.

2. Add your OpenAI API key to the `.env` file like this:

```env
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx