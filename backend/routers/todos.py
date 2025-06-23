from fastapi import APIRouter, HTTPException
from typing import List
from models import Todo, TodoCreate

router = APIRouter(
    prefix="/todos",
    tags=["todos"]
)

# メモリ内データストレージ（簡単な例のため）
todos_db = []
current_id = 1

@router.get("/", response_model=List[Todo])
async def get_todos():
    return todos_db

@router.post("/", response_model=Todo)
async def create_todo(todo: TodoCreate):
    global current_id
    new_todo = Todo(
        id=current_id,
        title=todo.title,
        description=todo.description,
        completed=todo.completed
    )
    todos_db.append(new_todo)
    current_id += 1
    return new_todo

@router.put("/{todo_id}", response_model=Todo)
async def update_todo(todo_id: int, todo: TodoCreate):
    for i, existing_todo in enumerate(todos_db):
        if existing_todo.id == todo_id:
            updated_todo = Todo(
                id=todo_id,
                title=todo.title,
                description=todo.description,
                completed=todo.completed
            )
            todos_db[i] = updated_todo
            return updated_todo
    raise HTTPException(status_code=404, detail="Todo not found")

@router.delete("/{todo_id}")
async def delete_todo(todo_id: int):
    for i, todo in enumerate(todos_db):
        if todo.id == todo_id:
            del todos_db[i]
            return {"message": "Todo deleted"}
    raise HTTPException(status_code=404, detail="Todo not found")
