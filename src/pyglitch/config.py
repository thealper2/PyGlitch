class GlitchConfig:
    """
    A class to store glitch effect parameters.

    Attributes:
        thickness (int): Thickness of the glitch lines.
        length (int): Maximum length of the glitch lines.
        num_glitcher (int): Number of glitches to apply per frame.
        num_frames (int): Number of frames in the GIF.
        speed (float): Speed of the animation (frame duration in seconds).
    """

    def __init__(
        self,
        thickness: int = 5,
        length: int = 50,
        num_glitches: int = 10,
        num_frames: int = 20,
        speed: float = 0.1,
    ):
        self.thickness = thickness
        self.length = length
        self.num_glitches = num_glitches
        self.num_frames = num_frames
        self.speed = speed
