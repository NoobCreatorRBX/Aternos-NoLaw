import requests
import os
from datetime import datetime

HOST = os.environ["SERVER_IP"]
WEBHOOK_URL = os.environ["WEBHOOK_URL"]
MESSAGE_ID = os.environ["MESSAGE_ID"]

def check_server():
    try:
        r = requests.get(
            f"https://api.mcstatus.io/v2/status/java/{HOST}",
            timeout=10
        )
        data = r.json()

        if not data.get("online"):
            return False

        # Require real Minecraft data
        if not data.get("version"):
            return False

        if not data.get("players"):
            return False

        return True

    except:
        return False

online = check_server()

status = "ONLINE" if online else "OFFLINE"
color = 5763719 if online else 15548997

embed = {
    "embeds": [{
        "title": "🎮 Aternos Server",
        "description": f"Status: **{status}**",
        "footer": {
            "text": f"Last checked: {datetime.utcnow().strftime('%H:%M:%S')} UTC"
        },
        "color": color
    }]
}

requests.patch(f"{WEBHOOK_URL}/messages/{MESSAGE_ID}", json=embed)
