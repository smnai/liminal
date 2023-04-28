from pydantic import BaseModel

class ResourceType(BaseModel):
    image = "image"
    audio = "audio"
