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

**Firefox・Safari** は下の専用版を使ってください。

**使えないもの**：スマホ版の Chrome・Edge など（拡張機能自体を入れられません）

## フォルダー構成

| フォルダー | 対象 |
|---|---|
| （一番上） | Chrome・Edge・Brave・Vivaldi・Opera など Chromium 系 |
| `firefox/` | Firefox（PC版 140 以降・Android版 142 以降） |
| `safari/` | Safari（Mac・iPhone・iPad） |

## Firefox で使う

**お試しで入れる（再起動すると外れます）**

1. アドレスバーに `about:debugging#/runtime/this-firefox` と入力
2. 「一時的なアドオンを読み込む」を押す
3. `firefox` フォルダーの中の `manifest.json` を選ぶ

**ずっと使う**

Firefox は Mozilla の署名がない拡張を常用できません。
[addons.mozilla.org の開発者ページ](https://addons.mozilla.org/developers/) で `firefox` フォルダーを ZIP にしてアップロードし、
「自分で配布（On your own）」を選ぶと署名済みの `.xpi` がもらえます。これをFirefoxにドラッグすると入ります。
Android版 Firefox で使う場合は、ストアで公開（On this site）する必要があります。

## Safari で使う

Safari の拡張は Mac と Xcode（無料）が必要です。Windows では作れません。

1. Mac に Xcode を入れる
2. ターミナルで次を実行（`safari` フォルダーの場所に合わせて変えてください）
   ```
   xcrun safari-web-extension-converter ./safari --app-name "重複タブ消し" --bundle-identifier com.hakusyaku-lab.jufuku-tab-keshi
   ```
3. 開いた Xcode で ▶（Run）を押すとアプリができて Safari に登録されます
4. Safari の「設定」→「拡張機能」で「重複タブ消し」をオンにする
   （署名なしで試すときは「設定」→「詳細」→「Webデベロッパ用の機能を表示」をオンにし、「開発」メニューの「未署名の拡張機能を許可」を選ぶ）

iPhone・iPad で使うには、同じ Xcode プロジェクトから iOS 版としてビルドします（Apple Developer への登録が必要です）。

**注意**：対象はボタンを押したブラウザの中のタブだけです。Edge と Chrome を両方開いていても、押した側の重複しか閉じません。

## ライセンス

MIT License
