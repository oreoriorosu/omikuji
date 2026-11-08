# omikuji

詩片のおみくじ（studio yaneura）をQRコードから引くための静的サイト。アクセスごとに80枚から1枚をランダム表示する。

- 公開: GitHub Pages（`main` ブランチの `docs/`）→ https://oreoriorosu.github.io/omikuji/
- 画像の再生成: `python3 build_images.py <omikuji.pdf>`（A4横・1ページ5枚・トンボ付きPDFを前提に、400dpiで裁ち線どおり切り出して `docs/img/NN.webp` に出力する）
- 枚数を変えたら `docs/index.html` の `COUNT` も合わせる。
