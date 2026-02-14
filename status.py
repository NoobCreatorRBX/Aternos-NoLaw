import requests
import os
from datetime import datetime

SERVER_ID = os.environ["SERVER_ID"]
WEBHOOK_URL = os.environ["WEBHOOK_URL"]
MESSAGE_ID = os.environ["MESSAGE_ID"]

def check_server():
    try:
        r = requests.get(
            f"https://aternos.org/ajax/server/status.php?server={SERVER_ID}",
            timeout=10
        )
        data = r.json()

        # Real Aternos state
        return data.get("status") == "online"

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



