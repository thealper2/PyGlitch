# PyGlitch

**PyGlitch**, görsellere glitch efektleri uygulayan ve bu efektlerle glitch GIF'leri oluşturan bir Python kütüphanesidir. Bu proje, görsel manipülasyon ve eğlenceli efektler oluşturmak isteyen geliştiriciler için tasarlanmıştır.

## :clipboard: İçindekiler

1. [Özellikler](https://github.com/thealper2/PyGlitch?tab=readme-ov-file#dart-%C3%B6zellikler)
2. [Kurulum](https://github.com/thealper2/PyGlitch?tab=readme-ov-file#hammer_and_wrench-kurulum)
3. [Kullanım](https://github.com/thealper2/PyGlitch?tab=readme-ov-file#joystick-kullan%C4%B1m)
4. [Katkıda Bulunma](https://github.com/thealper2/PyGlitch?tab=readme-ov-file#handshake-katk%C4%B1da-bulunma)
5. [Lisans](https://github.com/thealper2/PyGlitch?tab=readme-ov-file#scroll-lisans)

---

## :dart: Özellikler

- Görsellere rastgele glitch efektleri uygular.
- Glitch efektlerini kullanarak animasyonlu GIF'ler oluşturur.
- Glitch efektlerinin kalınlığı, uzunluğu, sayısı ve hızı gibi parametreler kolayca ayarlanabilir.
- Markdown hücrelerini ve HTML çıktılarını düzgün bir şekilde işler.

## :hammer_and_wrench: Kurulum

Projeyi yerel makinenize klonlayın:

```bash
git clone https://github.com/thealper2/PyGlitch.git
cd PyGlitch
```

Gerekli bağımlılıkları yüklemek için `pyproject.toml` dosyasını kullanın:

```bash
pip install .
```

## :joystick: Kullanım

### Komut Satırı Arayüzü (CLI)

Projeyi komut satırından çalıştırmak için:

```bash
pyglitch /path/to/input_image.png /path/to/output.gif --thickness 5 --length 50 --num_glitches 10 --num_frames 20 --speed 0.1
```

### Python Modülü Olarak Kullanım

Projeyi bir Python modülü olarak da kullanabilirsiniz:

```python
from pyglitch import GlitchConfig, GlitchGIFGenerator

config = GlitchConfig(thickness=5, length=50, num_glitches=10, num_frames=20, speed=0.1)

generator = GlitchGIFGenerator("input_image.png", "output.gif", config)
generator.create_glitch_gif()
```

### Testler

Proje, `unittest` kütüphanesi kullanılarak test edilmiştir. Testleri çalıştırmak için aşağıdaki komutu kullanın:

```bash
python run_tests.py
```

Bu komut, `src/tests/` dizinindeki tüm test dosyalarını çalıştırır.

## :handshake: Katkıda Bulunma

Katkıda bulunmak isterseniz, lütfen aşağıdaki adımları izleyin:

1. Bu depoyu forklayın.
2. Yeni bir branch oluşturun (`git checkout -b feature/AmazingFeature`).
3. Değişikliklerinizi commit edin (`git commit -m 'Add some AmazingFeature'`).
4. Branch'inizi pushlayın (`git push origin feature/AmazingFeature`).
5. Bir Pull Request açın.

## :scroll: Lisans

Bu proje MIT Lisansı altında lisanslanmıştır. Daha fazla bilgi için LICENSE dosyasına bakın.