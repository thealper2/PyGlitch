import unittest
from src.pyglitch.config import GlitchConfig
from src.pyglitch.effect import GlitchEffect
from PIL import Image
import numpy as np


class TestGlitchEffect(unittest.TestCase):
    def setUp(self):
        """Set up a test image and GlitchConfig."""
        self.config = GlitchConfig(thickness=5, length=50, num_glitches=10)
        self.glitch_effect = GlitchEffect(self.config)
        self.test_image = Image.new("RGB", (100, 100), color="white")

    def test_validate_config(self):
        """Test validation of GlitchConfig."""
        with self.assertRaises(ValueError):
            invalid_config = GlitchConfig(thickness=0, length=0, num_glitches=0)
            GlitchEffect(invalid_config)

    def test_apply_glitch(self):
        """Test applying glitch effect to an image."""
        glitched_image = self.glitch_effect._apply_glitch(self.test_image)
        self.assertIsInstance(glitched_image, Image.Image)
        self.assertNotEqual(
            np.array(self.test_image).tolist(), np.array(glitched_image).tolist()
        )


if __name__ == "__main__":
    unittest.main()
