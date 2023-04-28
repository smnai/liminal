import settings
from media_generator import MediaGenerator

if __name__ == "__main__":
    for _ in range(settings.NUM_ITERATIONS):
        mg = MediaGenerator()
        mg.create_images_audio_and_upload_to_storage()