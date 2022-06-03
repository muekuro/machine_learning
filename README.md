# machine_learning
機械学習の勉強

## TensorFlowについて
筆者はM1 Macのため、仮想環境を構築し、実装を行なっている。
追記、.ipynbでの開発に切り替えたため、jupyterを使用している。

### 導入方法
1. コマンドラインツールをインストール<br>
    ``` bash
    xcode-select --install
    ```
    インストールが完了したら```xcode-select -v```でバージョンを確認し、表示されたら完了。

2. Miniforgeをインストール<br>
    もし、Rosetta経由でIntel版のAnacondaをインストールしているなら、アンインストールしてください。<br>[公式ドキュメント](https://github.com/conda-forge/miniforge)に行き、ダウンロードする。
    ``` bash
    # ダウンロードしたシェルスクリプトを実行
    bash Miniforge3-MacOSX-arm64 sh
    ```
    
3. conda仮想環境を作成<br>
    ライブラリ同士の干渉を避けるため、bashとは別に仮想環境を準備する。<br>M1 Macには、TensorFlowを使うためのyamlファイルが準備されているので活用する。
    ``` bash
    wget -P ~/Downloads https://raw.githubusercontent.com/mwidjaja1/DSOnMacARM/main/environment.yml
    ```
    ダウンロードが完了したら、仮想環境を作成する。
    ``` bash
    # bash環境に移動
    source ~/.zshrc
    # m1_mac_tensorflow仮想環境を作成(名前は可変)
    conda env create --file=environment.yml --name m1_mac_tensorflow
    # 仮想環境を使うために有効化
    conda activate m1_mac_tensorflow
    # いらないファイルの削除
    rm environment yml
    ```
4. tensorflowのインストール<br>
    ```
    conda install -c apple tensorflow-deps
    ```

5. jupterについて<br>
    web上で行えるipynb開発
    ```
    conda install jupyter -y
    jupyter notebook # 起動
    ```

6. その他 おすすめライブラリ<br>
    Pythonライブラリをインストールするには、```conda install [Library] -y```を入力するだけです。
    ``` bash
    conda install jupyter -y
    conda install matplotlib -y
    conda install scikit-learn -y
    conda install opencv -y
    conda install pandas -y
    ```

[参考サイト](https://tech-diary.net/how-to-install-tensorflow-on-m1-mac/#index_id4)