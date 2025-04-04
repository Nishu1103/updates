import requests
import time

url = "https://nishantstocks.streamlit.app/"  # Replace with your app’s URL
while True:
    requests.get(url)
    print("Pinged app to keep it awake")
    time.sleep(3600)  # Ping every hour (3600 seconds)