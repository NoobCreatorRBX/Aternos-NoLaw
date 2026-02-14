import requests
import os
from datetime import datetime

HOST = os.environ["SERVER_IP"]
WEBHOOK_URL = os.environ["WEBHOOK_URL"]
MESSAGE_ID = os.environ["MESSAGE_ID"]

def check_server():
    try:
        r = requests.get(f"https://api.mcstatus.io/v2/status/java/{HOST}", timeout=10)
        data = r.json()

        # True only if server is actually responding properly
        if data.get("online") and data.get("players") is not None:
            return True
        else:
            return False

    except:
        return False

online = check_server()

status = "ONLINE" if online else "OFFLINE"
color = 5763719 if online else 15548997

data = {
    "embeds": [{
        "title": "🎮 Aternos Server",
        "description": f"Status: **{status}**",
        "footer": {
            "text": f"Last checked: {datetime.utcnow().strftime('%H:%M:%S')} UTC"
        },
        "color": color
    }]
}

requests.patch(f"{WEBHOOK_URL}/messages/{MESSAGE_ID}", json=data)

