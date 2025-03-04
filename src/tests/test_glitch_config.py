import unittest
from src.pyglitch.config import GlitchConfig


class TestGlitchConfig(unittest.TestCase):
    def test_default_values(self):
        """Test default values of GlitchConfig."""
        config = GlitchConfig()
        self.assertEqual(config.thickness, 5)
        self.assertEqual(config.length, 50)
        self.assertEqual(config.num_glitches, 10)
        self.assertEqual(config.num_frames, 20)
        self.assertEqual(config.speed, 0.1)

    def test_custom_values(self):
        """Test custom values of GlitchConfig."""
        config = GlitchConfig(
            thickness=10, length=100, num_glitches=5, num_frames=30, speed=0.5
        )
        self.assertEqual(config.thickness, 10)
        self.assertEqual(config.length, 100)
        self.assertEqual(config.num_glitches, 5)
        self.assertEqual(config.num_frames, 30)
        self.assertEqual(config.speed, 0.5)


if __name__ == "__main__":
    unittest.main()
