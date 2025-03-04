import random
import numpy as np
from PIL import Image

from src.pyglitch.config import GlitchConfig


class GlitchEffect:
    """
    A class that applies a glitch effect to an image.

    Attributes:
        config (GlitchConfig): Configuration parameters for glitch effect.
    """

    def __init__(self, config: GlitchConfig):
        """
        Initializes the glitch effect with configuration parameters.

        Args:
            config (GlitchConfig): Configuration parameters for the glitch effect.
        """
        self.config = config
        self._validate_config()

    def _validate_config(self) -> None:
        """
        Validates the glitch effect configuration parameters.

        Raises:
            ValueError: If any of the parameters are not positive integers.
        """
        if (
            self.config.thickness <= 0
            or self.config.length <= 0
            or self.config.num_glitches <= 0
        ):
            raise ValueError("Glitch parameters must be positive integers.")

    def _apply_glitch(self, image: Image.Image) -> Image.Image:
        """
        Applies the glitch effect to an image.

        Args:
            image (Image.Image): The input image to apply the glitch effect to.

        Returns:
            Image.Image: The glitched image.
        """
        img_array = np.array(image)
        height, width, _ = img_array.shape

        # Apply glitches by shifting random sections of the image
        for _ in range(self.config.num_glitches):
            y = random.randint(0, height - self.config.thickness)
            x_start = random.randint(0, width - self.config.length)
            x_end = min(width, x_start + self.config.length)
            shift = random.randint(-10, 10)
            img_array[y : y + self.config.thickness, x_start:x_end] = np.roll(
                img_array[y : y + self.config.thickness, x_start:x_end], shift, axis=1
            )

        return Image.fromarray(img_array)
