<script lang="ts">
    import { onMount } from 'svelte';
    import type { Todo } from '$lib/types';
    import { fetchTodos, createTodo, updateTodo, deleteTodo } from '$lib/api';

    let todos: Todo[] = [];
    let newTodoTitle = '';
    let newTodoDescription = '';
    let loading = false;

    onMount(async () => {
        await loadTodos();
    });

    async function loadTodos(): Promise<void> {
        try {
            loading = true;
            todos = await fetchTodos();
        } catch (error) {
            console.error('Error loading todos:', error);
        } finally {
            loading = false;
        }
    }

    async function addTodo(): Promise<void> {
        if (!newTodoTitle.trim()) return;
        
        try {
            const newTodo = await createTodo({
                title: newTodoTitle,
                description: newTodoDescription,
                completed: false
            });
            todos = [...todos, newTodo];
            newTodoTitle = '';
            newTodoDescription = '';
        } catch (error) {
            console.error('Error creating todo:', error);
        }
    }

    async function toggleTodo(todo: Todo): Promise<void> {
        try {
            const updatedTodo = await updateTodo(todo.id, {
                ...todo,
                completed: !todo.completed
            });
            todos = todos.map(t => t.id === todo.id ? updatedTodo : t);
        } catch (error) {
            console.error('Error updating todo:', error);
        }
    }

    async function removeTodo(id: number): Promise<void> {
        try {
            await deleteTodo(id);
            todos = todos.filter(t => t.id !== id);
        } catch (error) {
            console.error('Error deleting todo:', error);
        }
    }
</script>

<main>
    <h1>Todo アプリケーション</h1>
    
    <div class="add-todo">
        <input
            bind:value={newTodoTitle}
            placeholder="Todo タイトル"
            on:keydown={(e) => e.key === 'Enter' && addTodo()}
        />
        <input
            bind:value={newTodoDescription}
            placeholder="説明（オプション）"
        />
        <button on:click={addTodo}>追加</button>
    </div>

    {#if loading}
        <p>読み込み中...</p>
    {:else if todos.length === 0}
        <p>Todoがありません。</p>
    {:else}
        <ul class="todo-list">
            {#each todos as todo (todo.id)}
                <li class="todo-item" class:completed={todo.completed}>
                    <input
                        type="checkbox"
                        checked={todo.completed}
                        on:change={() => toggleTodo(todo)}
                    />
                    <div class="todo-content">
                        <h3>{todo.title}</h3>
                        {#if todo.description}
                            <p>{todo.description}</p>
                        {/if}
                    </div>
                    <button on:click={() => removeTodo(todo.id)}>削除</button>
                </li>
            {/each}
        </ul>
    {/if}
</main>

<style>
    main {
        max-width: 600px;
        margin: 0 auto;
        padding: 20px;
    }

    .add-todo {
        display: flex;
        gap: 10px;
        margin-bottom: 20px;
    }

    .add-todo input {
        flex: 1;
        padding: 10px;
        border: 1px solid #ddd;
        border-radius: 4px;
    }

    .add-todo button {
        padding: 10px 20px;
        background-color: #007bff;
        color: white;
        border: none;
        border-radius: 4px;
        cursor: pointer;
    }

    .todo-list {
        list-style: none;
        padding: 0;
    }

    .todo-item {
        display: flex;
        align-items: center;
        gap: 10px;
        padding: 15px;
        border: 1px solid #ddd;
        border-radius: 4px;
        margin-bottom: 10px;
    }

    .todo-item.completed {
        opacity: 0.6;
        text-decoration: line-through;
    }

    .todo-content {
        flex: 1;
    }

    .todo-content h3 {
        margin: 0 0 5px 0;
    }

    .todo-content p {
        margin: 0;
        color: #666;
        font-size: 0.9em;
    }

    button {
        padding: 5px 10px;
        background-color: #dc3545;
        color: white;
        border: none;
        border-radius: 4px;
        cursor: pointer;
    }
</style>
