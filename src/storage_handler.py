import uuid

import cloudinary
import cloudinary.uploader as cldup

import settings
from models import ResourceType

config = cloudinary.config(secure=True)

def upload_files(prompt: str, image_output: list[str], resource_type: ResourceType= "image") -> bool:
    for _, img_url in enumerate(image_output):
        cldup.upload_large(
            img_url,
            resource_type=resource_type,
            public_id=f"{settings.CLD_FOLDER}/{resource_type}/{prompt}_{uuid.uuid4()}.png",
            chunk_size=6000000,
            eager_async=True,
        )