#!/usr/bin/env python3
"""Build the 1-bit images used by the field notes variant.

The project pages keep their original colour figures. Only the hero
landscape, the About portrait, and the project index plates are reduced
to 1 bit.
"""

from pathlib import Path

from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "docs/assets/images"
OUT = SRC / "1bit"

# source, output, width, Bayer matrix size
JOBS = [
    ("hero-image.png", "hero.png", 560, 8, None),
    ("about-portrait.jpeg", "about.png", 420, 8, 3 / 4),
    ("palm-1.jpg", "palm-1.png", 280, 8, None),
    ("biosift-1.png", "biosift-1.png", 280, 8, None),
    ("flood-1.png", "flood-1.png", 280, 8, None),
    ("uhi-1.jpg", "uhi-1.png", 280, 8, None),
    ("green-1.jpg", "green-1.png", 280, 8, None),
]


def bayer(n: int) -> list[list[int]]:
    if n == 1:
        return [[0]]
    half = bayer(n // 2)
    top = [[4 * v for v in row] + [4 * v + 2 for v in row] for row in half]
    bottom = [[4 * v + 3 for v in row] + [4 * v + 1 for v in row] for row in half]
    return top + bottom


def flatten(im: Image.Image) -> Image.Image:
    im = ImageOps.exif_transpose(im)
    if im.mode in ("RGBA", "LA", "P"):
        im = im.convert("RGBA")
        bg = Image.new("RGBA", im.size, (255, 255, 255, 255))
        im = Image.alpha_composite(bg, im)
    return im.convert("RGB")


def one_bit(src: Path, dst: Path, width: int, n: int, aspect: float | None = None) -> None:
    im = flatten(Image.open(src))
    if aspect is not None:
        w, h = im.size
        if w / h > aspect:
            crop_w = round(h * aspect)
            left = (w - crop_w) // 2
            im = im.crop((left, 0, left + crop_w, h))
        else:
            crop_h = round(w / aspect)
            top = (h - crop_h) // 2
            im = im.crop((0, top, w, top + crop_h))
    w, h = im.size
    im = im.resize((width, round(h * width / w)), Image.Resampling.LANCZOS)
    gray = ImageOps.autocontrast(im.convert("L"), cutoff=1)
    matrix = bayer(n)
    out = Image.new("1", gray.size)
    src_px = gray.load()
    dst_px = out.load()
    for y in range(gray.height):
        row = matrix[y % n]
        for x in range(gray.width):
            threshold = (row[x % n] + 0.5) * 255 / (n * n)
            dst_px[x, y] = 255 if src_px[x, y] > threshold else 0
    out.save(dst, optimize=True)
    print(f"{dst.relative_to(ROOT)}  {out.width}x{out.height}")


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    for source, output, width, n, aspect in JOBS:
        one_bit(SRC / source, OUT / output, width, n, aspect)


if __name__ == "__main__":
    main()
