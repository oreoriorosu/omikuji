"""omikuji PDF（A4横・1ページ5枚・トンボ付き）を1枚ずつWebPへ切り出す。

使い方: python3 build_images.py ~/shared/omikuji_1106.pdf
"""
import subprocess
import sys
import tempfile
from pathlib import Path

from PIL import Image

DPI = 400
# 400dpiで実測したトンボ位置（裁ち落とし線）。1枚 56mm x 196mm。
X0, PITCH, Y0, Y1, COLS = 134, 882, 110, 3197, 5
# 上部の折り線。ここより上（タイトル・注意書き）は縦書きを90°倒して印刷されている。
FOLD_Y = 756

pdf = Path(sys.argv[1])
out = Path(__file__).parent / "docs" / "img"
out.mkdir(parents=True, exist_ok=True)

n = 0
with tempfile.TemporaryDirectory() as tmp:
    subprocess.run(["pdftoppm", "-r", str(DPI), "-png", str(pdf), f"{tmp}/p"], check=True)
    for page in sorted(Path(tmp).glob("p-*.png")):
        im = Image.open(page).convert("RGB")
        for i in range(COLS):
            n += 1
            x = X0 + i * PITCH
            im.crop((x, Y0, x + PITCH, Y1)).save(out / f"{n:02d}.webp", quality=85, method=6)
# 表紙: 全短冊で共通の上部を左に90°回して縦書きが読める向きにする
Image.open(out / "01.webp").crop((0, 0, PITCH, FOLD_Y)).rotate(90, expand=True).save(out / "cover.webp", quality=90, method=6)
print(n)
