# PyGlitch

PyGlitch is a Python library that applies glitch effects to images and creates glitch GIFs using these effects. This project is designed for developers who want to engage in image manipulation and create fun effects.

<div style="display: flex;">
  <img src="https://raw.githubusercontent.com/thealper2/PyGlitch/refs/heads/main/images/input.png" alt="Input Image" style="width: 50%; margin-right: 10px;">
  <img src="https://raw.githubusercontent.com/thealper2/PyGlitch/refs/heads/main/images/output.gif" alt="Output Image" style="width: 50%;">
</div>

## :clipboard: Table of Contents

1. [Features](https://github.com/thealper2/PyGlitch?tab=readme-ov-file#dart-%C3%B6zellikler)
2. [Installation](https://github.com/thealper2/PyGlitch?tab=readme-ov-file#hammer_and_wrench-kurulum)
3. [Usage](https://github.com/thealper2/PyGlitch?tab=readme-ov-file#joystick-kullan%C4%B1m)
4. [Contributing](https://github.com/thealper2/PyGlitch?tab=readme-ov-file#handshake-katk%C4%B1da-bulunma)
5. [License](https://github.com/thealper2/PyGlitch?tab=readme-ov-file#scroll-lisans)

---

## :dart: Features

- Applies random glitch effects to images.
- Creates animated GIFs using glitch effects.
- Parameters such as thickness, length, number, and speed of glitch effects can be easily adjusted.
- Properly handles Markdown cells and HTML outputs.

## :hammer_and_wrench: Installation

Clone the project to your machine:

```bash
git clone https://github.com/thealper2/PyGlitch.git
cd PyGlitch
```

Use the `pyproject.toml` file to install the necessary dependencies:

```bash
pip install .
```

## :joystick: Usage

### Command Line Interface (CLI)

To run the project from the command line:

```bash
pyglitch /path/to/input_image.png /path/to/output.gif --thickness 5 --length 50 --num_glitches 10 --num_frames 20 --speed 0.1
```

### Using as a Python Module

You can also use the project as a Python module:

```python
from pyglitch import GlitchConfig, GlitchGIFGenerator

config = GlitchConfig(thickness=5, length=50, num_glitches=10, num_frames=20, speed=0.1)

generator = GlitchGIFGenerator("input_image.png", "output.gif", config)
generator.create_glitch_gif()
```

## :handshake: Contributing

If you wish to contribute, please follow these steps:

1. Fork this repository.
2. Create a new branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push your branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.

## :scroll: License

This project is licensed under the MIT License. For more information, see the LICENSE file.