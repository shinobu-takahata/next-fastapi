# AWS LambdaのPythonランタイム環境に適したベースイメージを使用
FROM public.ecr.aws/lambda/python:3.9

# 必要なパッケージをインストールするためのワーキングディレクトリを設定
WORKDIR /var/task

# パッケージをコピーし、依存関係をインストール
COPY ./backend/requirements.txt .
RUN python -m pip install -r requirements.txt

# バックエンドアプリケーションのコードをコピー
COPY ./backend /var/task

# Lambda関数として起動するためのハンドラを指定
CMD ["api/main.handler"]
