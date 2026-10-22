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

## 対応ブラウザ

タブの一覧取得と閉じる操作だけを使っているので、Chromium 系のブラウザ（PC版）ならほぼそのまま使えます。

| ブラウザ | 拡張機能ページ |
|---|---|
| Google Chrome | `chrome://extensions` |
| Microsoft Edge | `edge://extensions` |
| Brave | `brave://extensions` |
| Vivaldi | `vivaldi://extensions` |
| Opera | `opera://extensions`（右上の「開発者モード」から） |
| Arc などその他の Chromium 系 | たいてい同じ手順で使えます |

**使えないもの**

- スマホ版（Android・iPhone）の Chrome や Edge など：拡張機能自体を入れられません
- Firefox・Safari：Chromium 系ではないため、そのままでは入りません

**注意**：対象はボタンを押したブラウザの中のタブだけです。Edge と Chrome を両方開いていても、押した側の重複しか閉じません。

## ライセンス

MIT License
