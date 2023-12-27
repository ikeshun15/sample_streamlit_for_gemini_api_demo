# minicondaで仮想環境を作る
```
conda create --name python310_streamlit_gemini_demo python=3.10
```

# 環境
* python: 3.10


# 設定
1. 仮想環境を作成する
    ```
    conda create --name python310_streamlit_gemini_demo python=3.10
    conda activate python310_streamlit_gemini_demo
    ```

2. ライブラリをインストールする 
    ```
    pip install -r requirements.txt
    ```

3. .envファイルを作る
    .env_sampleファイルをもとに.envファイルを作成して、Gemini用APIキーを入力する  


# 実行
1. 仮想環境を立ち上げる
    ```
    conda activate python310_streamlit_gemini_demo
    ```

2. Streamlitを実行する
    ```
    streamlit run 1_🏠_Home.py
    ```

3. アプリにアクセスする
    ```
    http://localhost:55501/
    ```