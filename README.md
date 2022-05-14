# Rider Unofficial Japanese Translate Plugin
JetBrains Riderの非公式日本語化プラグイン

## プラグイン生成
プラグインを生成するには、Python 3以上 (3.9以上推奨) が必要となります。

生成する方法は、**既存の翻訳プラグインにパッチを当てる方法**(推奨) と、**一からビルドする方法** があります。

### パッチを当てる (推奨)
1. パッチを当てる元となる [JetBrains公式日本語言語パック](https://plugins.jetbrains.com/plugin/13964-japanese-language-pack------) を準備してください。
2. コマンドラインで、`python patch.py /path/to/langpack` を実行してください。
3. 正しくパッチが当てられると、`rider-jpn.zip` が生成されますので、そのプラグインをIDEにインストールしてください。

### ビルドする
1. コマンドラインで `python build.py` を実行してください。
2. 正しくビルドされると、`rider-jpn.zip` が生成されますので、そのプラグインをIDEにインストールしてください。