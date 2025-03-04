from src.pyglitch.config import GlitchConfig
from src.pyglitch.generator import GlitchGIFGenerator
from src.pyglitch.utils import setup_argparser


def main() -> int:
    """
    Function of the main program.
    """
    parser = setup_argparser()
    args = parser.parse_args()

    # Initialize configuration and generate the glitch GIF
    config = GlitchConfig(
        args.thickness, args.length, args.num_glitches, args.num_frames, args.speed
    )
    generator = GlitchGIFGenerator(args.image_path, args.output_path, config)
    generator.create_glitch_gif()
