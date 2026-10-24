"""配布用ZIPを dist/ に作る（GitHub Actions から自動で呼ばれます）。

  JufukuTabKeshi.zip          … Chrome・Edge・Brave など（展開して「展開して読み込み」）
  JufukuTabKeshi-firefox.zip  … Firefox（addons.mozilla.org にそのままアップロードできる形）
  JufukuTabKeshi-safari.zip   … Safari（Mac で Xcode 変換に使う）

手元で試すときは:  python scripts/build_zip.py
"""
import json
import pathlib
import sys
import zipfile

ROOT = pathlib.Path(__file__).resolve().parent.parent

# (ZIP名, 元フォルダ, ZIPの中のフォルダ名 ※空なら直下)
TARGETS = [
    ("JufukuTabKeshi.zip", ".", "JufukuTabKeshi"),
    ("JufukuTabKeshi-firefox.zip", "firefox", ""),  # AMO は manifest.json が直下にある必要がある
    ("JufukuTabKeshi-safari.zip", "safari", "safari"),
]
EXTRA = ["LICENSE"]


def files_of(src: pathlib.Path) -> list[str]:
    m = json.loads((src / "manifest.json").read_text(encoding="utf-8"))
    bg = m.get("background", {})
    names = ["manifest.json"]
    if "service_worker" in bg:
        names.append(bg["service_worker"])
    names += bg.get("scripts", [])
    return names


def main() -> int:
    versions = {}
    for _, src, _ in TARGETS:
        m = json.loads((ROOT / src / "manifest.json").read_text(encoding="utf-8"))
        versions[src] = m["version"]
    if len(set(versions.values())) != 1:
        print("3つの manifest.json の version がそろっていません:", versions)
        return 1

    dist = ROOT / "dist"
    dist.mkdir(exist_ok=True)
    for zip_name, src, inner in TARGETS:
        src_dir = ROOT / src
        names = files_of(src_dir)
        missing = [n for n in names if not (src_dir / n).is_file()]
        if missing:
            print(f"{src}: 見つからないファイル {missing}")
            return 1
        with zipfile.ZipFile(dist / zip_name, "w", zipfile.ZIP_DEFLATED) as z:
            for n in names:
                z.write(src_dir / n, f"{inner}/{n}" if inner else n)
            for n in EXTRA:
                z.write(ROOT / n, f"{inner}/{n}" if inner else n)
        print(f"作成: dist/{zip_name}")
    print("バージョン", next(iter(versions.values())))
    return 0


if __name__ == "__main__":
    sys.exit(main())
