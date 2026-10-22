# 重複タブ消し（JufukuTabKeshi）

Microsoft Edge / Google Chrome 用の拡張機能です。
ツールバーのボタンを押すと、同じページのタブを1つだけ残して閉じます。

## 動き

- すべてのウィンドウのタブが対象です
- 残すタブの優先順：固定タブ → 今見ているタブ → 左側のタブ
- URL の `#〜` 部分や末尾の `/` だけが違うタブは同じページとみなします
- 閉じたタブの数をアイコンに数秒表示します

## 入れ方（Edge）

1. このリポジトリをダウンロードして展開する（Code → Download ZIP）
2. アドレスバーに `edge://extensions` と入力
3. 「開発者モード」をオンにする
4. 「展開して読み込み」で、`manifest.json` があるフォルダーを選ぶ

Chrome の場合は `chrome://extensions` で同じ手順です。

## ライセンス

MIT License
