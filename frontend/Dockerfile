FROM node:22-alpine

WORKDIR /app

# package.jsonとpackage-lock.jsonのみを先にコピー
COPY package*.json ./

# 依存関係をLinuxコンテナ内でインストール
RUN npm ci --only=production

# アプリケーションコードをコピー（.dockerignoreでnode_modulesは除外される）
COPY . .

# アプリケーションをビルド
RUN npm run build

# ポートを公開
EXPOSE 3000

# アプリケーションを起動
CMD ["node", "build"]
