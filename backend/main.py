from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import todos

app = FastAPI(title="Todo API", version="1.0.0")

# CORS設定を更新（Docker環境用）
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",  # Docker frontend
        "http://frontend:3000",   # Docker internal
        "http://localhost:5173",  # 開発時SvelteKit
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# APIRouterをメインアプリに追加
app.include_router(todos.router, prefix="/api")

@app.get("/")
async def root():
    return {"message": "Todo API is running"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
