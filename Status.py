import requests
import socket
import os

HOST = os.environ["SERVER_IP"]
PORT = 25565
WEBHOOK_URL = os.environ["WEBHOOK_URL"]
MESSAGE_ID = os.environ["MESSAGE_ID"]

def check_server():
    try:
        socket.create_connection((HOST, PORT), timeout=5)
        return "ONLINE"
    except:
        return "OFFLINE"

status = check_server()

color = 5763719 if status == "ONLINE" else 15548997

data = {
    "embeds": [{
        "title": "🎮 Aternos Server",
        "description": f"Status: **{status}**",
        "color": color
    }]
}

requests.patch(f"{WEBHOOK_URL}/messages/{MESSAGE_ID}", json=data)
