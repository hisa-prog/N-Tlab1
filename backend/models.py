from pydantic import BaseModel

class Mail(BaseModel):
    address: str
    subject: str
    body: str | None
    audio: str | None
    audio_name: str | None