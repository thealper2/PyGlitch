import argparse


def setup_argparser() -> argparse.ArgumentParser:
    """
    Sets command line arguments.

    Returns:
        argparse.ArgumentParser: Argument parser
    """
    parser = argparse.ArgumentParser(
        description="Generate a glitch effect GIF from an image."
    )

    parser.add_argument("image_path", type=str, help="Path to the input image")
    parser.add_argument("output_path", type=str, help="Path to save the output GIF")
    parser.add_argument(
        "--thickness", type=int, default=5, help="Thickness of glitch lines"
    )
    parser.add_argument(
        "--length", type=int, default=50, help="Maximum length of glitch lines"
    )
    parser.add_argument(
        "--num_glitches", type=int, default=10, help="Number of glitches per frame"
    )
    parser.add_argument(
        "--num_frames", type=int, default=20, help="Number of frames in the GIF"
    )
    parser.add_argument(
        "--speed",
        type=float,
        default=0.1,
        help="Speed of the animation (frame duration in seconds)",
    )

    return parser
