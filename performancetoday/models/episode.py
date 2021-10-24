from dataclasses import dataclass



@dataclass
class Episode:
    date: str
    title: str
    description: str
    photo_url: str
    audio: str
