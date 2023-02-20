import os
import json

from googleapiclient.discovery import build


class Channel:
    def __init__(self, id_channel):
        self.id_channel = id_channel

        api_key: str = os.environ.get("API_KEY")
        youtube = build('youtube', 'v3', developerKey=api_key)
        self.channel = youtube.channels().list(id=id_channel, part='snippet,statistics').execute()

    def print_info(self):
        print(json.dumps(self.channel, indent=2, ensure_ascii=False))


vdud = Channel('UCMCgOm8GZkHp8zJ6l7_hIuA')
vdud.print_info()
