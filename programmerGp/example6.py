import webbrowser
import time
import random

while True:
    sites = random.choice(['google.com', 'nabegheha.com', 'maktabkhooneh.org/', 'python.org/'])
    webbrowser.open(sites)
    seconds = random.randrange(5, 20)
    time.sleep(seconds)