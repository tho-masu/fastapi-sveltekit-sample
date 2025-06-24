import type { Todo, TodoCreate } from './types';

// Docker環境とローカル開発環境の両方に対応
const { protocol, hostname } = window.location;
const API_BASE = typeof window !== 'undefined' 
  ? `${protocol}//${hostname}:8000/api`  // ブラウザから直接
  : 'http://backend:8000/api';   // サーバーサイドから

export async function fetchTodos(): Promise<Todo[]> {
    const response = await fetch(`${API_BASE}/todos/`);
    if (!response.ok) {
        throw new Error('Failed to fetch todos');
    }
    return response.json();
}

export async function createTodo(todo: TodoCreate): Promise<Todo> {
    const response = await fetch(`${API_BASE}/todos/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(todo),
    });
    if (!response.ok) {
        throw new Error('Failed to create todo');
    }
    return response.json();
}

export async function updateTodo(id: number, todo: TodoCreate): Promise<Todo> {
    const response = await fetch(`${API_BASE}/todos/${id}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(todo),
    });
    if (!response.ok) {
        throw new Error('Failed to update todo');
    }
    return response.json();
}

export async function deleteTodo(id: number): Promise<void> {
    const response = await fetch(`${API_BASE}/todos/${id}`, {
        method: 'DELETE',
    });
    if (!response.ok) {
        throw new Error('Failed to delete todo');
    }
}
