import random
import string

class PromptGenerator:

    def generate_prompt(extra_context="")->str:
        string_length = random.randint(0,100)
        prompt =  ''.join(random.choice(string.ascii_letters + string.digits + "-._~()!*:@,;") for _ in range(string_length))
        if extra_context:
            prompt = f"{prompt}, {extra_context}"
        return prompt