# 環境
* python: 3.11


# 設定
1. 仮想環境を作成する
    ```
    conda create --name python311_streamlit_gemini_demo python=3.11
    conda activate python311_streamlit_gemini_demo
    ```

2. ライブラリをインストールする 
    ```
    pip install -r requirements.txt
    ```

3. .envファイルを作る
    .env_sampleファイルをもとに.envファイルを作成して、Gemini用APIキーを入力する
    ```
    GEMINI_API_KEY = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    ```


# 実行
1. 仮想環境を立ち上げる
    ```
    conda activate python311_streamlit_gemini_demo
    ```

2. Streamlitを実行する
    ```
    streamlit run 1_🏠_Home.py
    ```