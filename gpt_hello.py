import globalPluginHandler
import ui
import os
import json
import urllib.request
import gui

def load_api_key():
    """
    Loads the OpenAI API key from a .env file in the same directory as this script.
    """
    try:
        plugin_dir = os.path.dirname(__file__)
        env_path = os.path.join(plugin_dir, ".env")
        with open(env_path) as f:
            for line in f:
                if line.strip().startswith("OPENAI_API_KEY="):
                    return line.strip().split("=", 1)[1]
    except Exception as e:
        import ui
        ui.message(f"Error loading API key: {str(e)}")
        return None

class GlobalPlugin(globalPluginHandler.GlobalPlugin):
    """
    A simple global NVDA plugin that responds to the key command NVDA+A
    by sending a prompt to ChatGPT and reading the response aloud.
    """

    def script_helloWorldGPT(self, gesture):
        ui.message("NVDA+A triggered!")  # Debug test message
        
        # Load API key securely
        api_key = load_api_key()
        if not api_key:
            ui.message("API key not found.")
            return

        try:
            # Prepare OpenAI HTTP request headers
            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {api_key}"
            }

            # Construct the message payload
            data = {
                "model": "gpt-3.5-turbo",
                "messages": [{"role": "user", "content": "hello world"}]
            }

            # Create the HTTP request
            req = urllib.request.Request(
                "https://api.openai.com/v1/chat/completions",
                data=json.dumps(data).encode("utf-8"),
                headers=headers,
                method="POST"
            )

            # Send request and parse response
            with urllib.request.urlopen(req) as res:
                result = json.loads(res.read().decode("utf-8"))
                reply = result["choices"][0]["message"]["content"]
                ui.message(reply) # Speak the reply for screen reader users
                gui.messageBox(
                    reply,
                    "GPT-4 Response",
                    gui.wx.OK | gui.wx.ICON_INFORMATION
                ) # Show popup for additional accessibility/visibility

        except Exception as e:
            # Handle network or API errors
            ui.message("Error: " + str(e))

    # Define keyboard shortcut gesture: NVDA+A triggers the method above
    __gestures = {
        "kb:NVDA+a": "helloWorldGPT"
    }
