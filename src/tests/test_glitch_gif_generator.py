import unittest
import os
from src.pyglitch.config import GlitchConfig
from src.pyglitch.generator import GlitchGIFGenerator
from PIL import Image


class TestGlitchGIFGenerator(unittest.TestCase):
    def setUp(self):
        """Set up a test image and GlitchConfig."""
        self.image_path = "test_image.png"
        self.output_path = "output.gif"
        self.config = GlitchConfig(num_frames=5)
        self.test_image = Image.new("RGB", (100, 100), color="white")
        self.test_image.save(self.image_path)

    def tearDown(self):
        """Clean up generated files."""
        if os.path.exists(self.image_path):
            os.remove(self.image_path)
        if os.path.exists(self.output_path):
            os.remove(self.output_path)
        if os.path.exists("frames"):
            for file in os.listdir("frames"):
                os.remove(os.path.join("frames", file))
            os.rmdir("frames")

    def test_validate_inputs(self):
        """Test validation of input paths."""
        with self.assertRaises(FileNotFoundError):
            invalid_generator = GlitchGIFGenerator(
                "invalid_path.png", self.output_path, self.config
            )

    def test_generate_glitch_frames(self):
        """Test generation of glitch frames."""
        generator = GlitchGIFGenerator(self.image_path, self.output_path, self.config)
        generator.generate_glitch_frames()
        self.assertEqual(len(generator.frames), self.config.num_frames)
        self.assertTrue(os.path.exists("frames"))

    def test_create_glitch_gif(self):
        """Test creation of glitch GIF."""
        generator = GlitchGIFGenerator(self.image_path, self.output_path, self.config)
        generator.create_glitch_gif()
        self.assertTrue(os.path.exists(self.output_path))


if __name__ == "__main__":
    unittest.main()
