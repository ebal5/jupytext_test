[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ebal5/jupytext_test/main?labpath=notebooks%2Fsample_notebook1.ipynb)

# JupyterLab利用プロジェクトをGitで管理する:jupytext編

[記事](https://zenn.dev/articles/e8fcb7aa4736f3) で試す内容のためのリポジトリ。

Pythonファイルやノートブックの内容は適当なサンプルとしてirisデータセットを読み込んでプロットするもの。
`src/` 配下には読み込みやプロット用の関数などが置かれており、ノートブックからはそれらを読み込んで利用する形。

このリポジトリでは、`notebooks`フォルダ配下にあるノートブックファイルにのみ出力セルの内容削除を適用するように設定してある。

## 環境ごとのセットアップ方法

注意: このリポジトリにpushしないようにしてください

### VSCode

この環境ではRyeを利用してパッケージを管理している

1. このリポジトリをzipでダウンロードあるいはフォークしてクローンする
2. リポジトリのフォルダでVSCodeを開く
3. Reopen Folder in ...
4. ryeによって必要なライブラリがインストールされる
TODO: VSCodeでの動作手順を書く

![Open as a Jupyter Notebookのメニュー](images/open_as_a_jupyter_notebook.png)

### JupyterLabをDockerで起動

この環境ではcondaを利用したパッケージ管理を行っている。

1. このリポジトリをzipでダウンロードあるいはフォークしてクローンする
2. `docker run -d -p 8888:8888 -v $(pwd):/home/jovyan/work jupyter/minimal-notebook:2023-10-20` などでJupyterLabのサーバーを起動する
3. コンテナのログからトークンをコピーする
4. `localhost:8888` を開き、先程コピーしたトークンを入力してJupyter環境に入る
5. `work`フォルダに移動する
6. ランチャーからターミナルを開く
7. `conda env update --file environment.yml` を実行する
8. extensions（パズルのピースっぽいロゴ）をクリックし `jupyterlab-git` を検索しインストールする
9. 同様に `jupytext` を検索しインストールする
10. コンテナを再起動する

## 試し方

`notebooks/` 配下のノートブックファイルを実行した後に保存し、コミットしようとしてみる、など。

## フォルダ構成

フォルダ・ファイルの利用方法想定は以下の通り。

- `.devcontainer`: VSCodeで開くときに利用するdevcontainer設定
- `notebooks/`: Jupyter Notebookファイルを格納
- `src/`: 再利用可能なPythonスクリプトを格納
- `data/`: 生データと前処理済みデータを格納（現在空）
- `models/`: 訓練済みモデルを格納（現在空）
- `reports/`: 分析レポートと生成されたグラフィックを格納（現在空）
- `requirements-dev.lock`: rye用の依存関係を記述したファイル
- `requirements.lock`: rye用の依存関係を記述したファイル
- `environment.yml`: condaの依存関係を共有するためのファイル
- `pyproject.toml`: ryeの設定管理用
- `LICENSE`: ライセンス情報を記述したファイル
- `README.md`: プロジェクトの概要と使用方法を説明するこのドキュメント
