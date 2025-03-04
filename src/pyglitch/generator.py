import os
from PIL import Image
from typing import List

from src.pyglitch.config import GlitchConfig
from src.pyglitch.effect import GlitchEffect


class GlitchGIFGenerator:
    """
    A class that generates a glitch effect GIF from an input image.

    Attributes:
        image_path (str): Path the input image.
        output_path (str): Path to save the output GIF.
        config (GlitchConfig): Configuration parameters for the glitch effect.
        frames (List[Image.Image]): List to store individual frames of the GIF.
        frames_folder (str): Folder to store individual frames.
    """

    def __init__(self, image_path: str, output_path: str, config: GlitchConfig):
        """
        Initializes the glitch GIF generator.

        Args:
            image_path (str): Path to the input image.
            output_path (str): Path to save the output GIF.
            config (GlitchConfig): Configuration parameters for the glitch effect.
        """
        self.image_path = image_path
        self.output_path = output_path
        self.config = config
        self.glitch_effect = GlitchEffect(config)
        self.frames: List[Image.Image] = []
        self.frames_folder = os.path.join(os.path.dirname(output_path), "frames")
        self._create_output_folder()
        self._validate_inputs()

    def _validate_inputs(self) -> None:
        """
        Validates input path.

        Raises:
            FileNotFoundError: If the input image file does not exist.
        """
        if not os.path.exists(self.image_path):
            raise FileNotFoundError(f"Image file not found: {self.image_path}")

    def _create_output_folder(self) -> None:
        """
        Creates a folder to store individual frames if it does not already exist.
        """
        os.makedirs(self.frames_folder, exist_ok=True)

    def generate_glitch_frames(self) -> None:
        """
        Generates glitch frames and saves them as  individual images.
        """
        try:
            image = Image.open(self.image_path).convert("RGB")
            for i in range(self.config.num_frames):
                # Apply glitch effect to the image
                glitched_image = self.glitch_effect._apply_glitch(image)
                frame_path = os.path.join(self.frames, f"frame_{i:03d}.png")
                glitched_image.save(frame_path)
                self.frames.append(glitched_image)
        except Exception as e:
            print(f"Error generating frames: {e}")

    def create_glitch_gif(self) -> None:
        """
        Creates a GIF from the generated frames and saves it to the output path.
        """
        try:
            self.generate_glitch_frames()
            gif_path = self.output_path
            # Save all frames as a GIF
            self.frames[0].save(
                gif_path,
                save_all=True,
                append_images=self.frames[1:],
                duration=int(self.config.speed * 1000),
                loop=0,
            )
            print(f"GIF saved at {gif_path}")
        except Exception as e:
            print(f"Error creating GIF: {e}")
