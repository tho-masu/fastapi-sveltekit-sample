# ビルドステージ - devDependenciesも含めてインストール
FROM node:22-alpine AS builder

WORKDIR /app

# package.jsonとpackage-lock.jsonをコピー
COPY package*.json ./

# ビルドに必要なdevDependencies（vite等）も含めてインストール
RUN npm ci

# アプリケーションコードをコピー
COPY . .

# アプリケーションをビルド（ここでviteが必要）
RUN npm run build

# プロダクションステージ - 本番用の軽量イメージ
FROM node:22-alpine AS production

WORKDIR /app

# 非rootユーザーを作成
RUN addgroup --system --gid 1001 nodejs && \
    adduser --system --uid 1001 sveltekit

# package.jsonをコピー（所有者を指定）
COPY --chown=sveltekit:nodejs package*.json ./

# 本番用依存関係のみインストール
RUN npm ci --only=production && npm cache clean --force

# ビルド済みファイルをコピー（所有者を指定）
COPY --chown=sveltekit:nodejs --from=builder /app/build ./build

# 非rootユーザーに切り替え
USER sveltekit

# ポートを公開
EXPOSE 3000

# アプリケーションを起動
CMD ["node", "build"]
