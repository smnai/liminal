import replicate

import settings as settings
from prompt_generator import PromptGenerator
from storage_handler import upload_files

class MediaGenerator:

    def __init__(self):
        extra_context = ""
        self.prompt = PromptGenerator.generate_prompt(extra_context=extra_context)
        self.image_output = []
        self.audio_output = []

    def create_images(self):
        output = replicate.run( 
            settings.REPLICATE_IMAGE_MODEL_TAG,
            input={"prompt": self.prompt}, 
            num_outputs=settings.NUM_OUTPUTS_PER_PROMPT,
        )
        return output

    def create_audio(self):
        output = replicate.run( 
            settings.REPLICATE_AUDIO_MODEL_TAG,
            input={"prompt": self.prompt}, 
            num_outputs=settings.NUM_OUTPUTS_PER_PROMPT,
        )
        output = [item.get('audio') for item in output.items()]
        return output

    def create_images_audio_and_upload_to_storage(self, create_audio=False):
        image_output = self.create_images()
        upload_files(self.prompt, image_output)
        if create_audio:
            audio_output = self.create_audio()
            upload_files(self.prompt, audio_output)