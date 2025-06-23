# Todo アプリケーション

SvelteKit（TypeScript）とFastAPI（APIRouter）を使用したフルスタックTodoアプリケーションです。Docker Composeで簡単に起動できます。

## 🚀 技術スタック

### フロントエンド

- **SvelteKit** - フルスタックWebフレームワーク
- **TypeScript** - 型安全な開発
- **Vite** - 高速ビルドツール


### バックエンド

- **FastAPI** - 高速なPython Webフレームワーク
- **APIRouter** - モジュール化されたルーティング
- **Pydantic** - データバリデーション


### インフラ

- **Docker** - コンテナ化
- **Docker Compose** - マルチコンテナ管理


## 🛠️ セットアップ

### 前提条件

- Docker
- Docker Compose


### インストールとセットアップ

1. **リポジトリをクローン**

```bash
git clone <repository-url>
cd todo-app
```

2. **アプリケーションを起動**

```bash
docker-compose up --build
```

3. **アクセス**
    - フロントエンド: http://localhost:3000
    - バックエンドAPI: http://localhost:8000
    - API ドキュメント: http://localhost:8000/docs

## 🎯 主な機能

- ✅ Todoの作成
- ✅ Todoの一覧表示
- ✅ Todoの完了状態切り替え
- ✅ Todoの削除
- ✅ リアルタイムなUI更新


## 📖 API仕様

### エンドポイント

| メソッド | エンドポイント | 説明 |
| :-- | :-- | :-- |
| GET | `/api/todos/` | Todo一覧取得 |
| POST | `/api/todos/` | Todo作成 |
| PUT | `/api/todos/{todo_id}` | Todo更新 |
| DELETE | `/api/todos/{todo_id}` | Todo削除 |

### データ構造

```typescript
interface Todo {
  id: number;
  title: string;
  description?: string;
  completed: boolean;
}

interface TodoCreate {
  title: string;
  description?: string;
  completed: boolean;
}
```


## 🔧 開発

### ローカル開発

**バックエンドのみ起動**:

```bash
cd backend
pip install -r requirements.txt
python main.py
```

**フロントエンドのみ起動**:

```bash
cd frontend
npm install
npm run dev
```


### Docker開発

**特定のサービスのみ起動**:

```bash
# バックエンドのみ
docker-compose up backend

# フロントエンドのみ
docker-compose up frontend
```

**ログの確認**:

```bash
# 全サービスのログ
docker-compose logs -f

# 特定のサービスのログ
docker-compose logs -f frontend
docker-compose logs -f backend
```


## 🐛 トラブルシューティング

### よくある問題

**1. esbuildプラットフォームエラー**

```
Error: You installed esbuild for another platform...
```

**解決法**: `.dockerignore`ファイルが適切に設定されていることを確認し、`docker-compose down --rmi all -v`でクリーンビルドを実行

**2. vite: not foundエラー**

```
sh: vite: not found
```

**解決法**: DockerfileでdevDependenciesも含めてインストールされていることを確認

**3. TypeScript import typeエラー**

```
Unexpected token at import type
```

**解決法**: `svelte.config.js`で`vitePreprocess()`が設定されていることを確認

### クリーンアップ

```bash
# 全てのコンテナ・イメージ・ボリュームを削除
docker-compose down --rmi all -v

# システム全体のクリーンアップ
docker system prune -a
```


## 📝 今後の改善点

- [ ] データベース統合（PostgreSQL/MongoDB）
- [ ] ユーザー認証機能
- [ ] Todoカテゴリ分類
- [ ] 期限設定機能
- [ ] テスト実装
- [ ] CI/CDパイプライン


## 🤝 コントリビューション

1. このリポジトリをフォーク
2. 機能ブランチを作成 (`git checkout -b feature/amazing-feature`)
3. 変更をコミット (`git commit -m 'Add some amazing feature'`)
4. ブランチにプッシュ (`git push origin feature/amazing-feature`)
5. プルリクエストを作成

## 📄 ライセンス

このプロジェクトは MIT License の下で公開されています。

