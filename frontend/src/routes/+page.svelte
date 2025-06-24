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

<main class="max-w-2xl mx-auto p-6">
    <h1 class="text-3xl font-bold text-gray-800 mb-8 text-center">Todo アプリケーション</h1>
    
    <div class="bg-white rounded-lg shadow-md p-6 mb-6">
        <div class="flex flex-col sm:flex-row gap-3 mb-4">
            <input
                bind:value={newTodoTitle}
                placeholder="Todo タイトル"
                class="flex-1 px-4 py-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500 focus:border-transparent outline-none"
                on:keydown={(e) => e.key === 'Enter' && addTodo()}
            />
            <input
                bind:value={newTodoDescription}
                placeholder="説明（オプション）"
                class="flex-1 px-4 py-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500 focus:border-transparent outline-none"
            />
            <button 
                on:click={addTodo}
                class="px-6 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700 focus:ring-2 focus:ring-blue-500 focus:ring-offset-2 transition-colors duration-200 font-medium"
            >
                追加
            </button>
        </div>
    </div>

    {#if loading}
        <div class="flex justify-center items-center py-8">
            <div class="animate-spin rounded-full h-8 w-8 border-b-2 border-blue-600"></div>
            <span class="ml-3 text-gray-600">読み込み中...</span>
        </div>
    {:else if todos.length === 0}
        <div class="text-center py-12">
            <div class="text-gray-400 text-6xl mb-4">📝</div>
            <p class="text-gray-500 text-lg">Todoがありません。</p>
            <p class="text-gray-400 text-sm mt-2">上のフォームから新しいTodoを追加してみてください。</p>
        </div>
    {:else}
        <div class="space-y-3">
            {#each todos as todo (todo.id)}
                <div class="bg-white rounded-lg shadow-sm border border-gray-200 p-4 hover:shadow-md transition-shadow duration-200" class:opacity-60={todo.completed}>
                    <div class="flex items-start gap-4">
                        <input
                            type="checkbox"
                            checked={todo.completed}
                            on:change={() => toggleTodo(todo)}
                            class="mt-1 w-5 h-5 text-blue-600 rounded focus:ring-blue-500 focus:ring-2"
                        />
                        <div class="flex-1 min-w-0" class:line-through={todo.completed}>
                            <h3 class="text-lg font-medium text-gray-900 mb-1">{todo.title}</h3>
                            {#if todo.description}
                                <p class="text-gray-600 text-sm">{todo.description}</p>
                            {/if}
                        </div>
                        <button 
                            on:click={() => removeTodo(todo.id)}
                            class="px-3 py-1 text-sm bg-red-100 text-red-700 rounded-md hover:bg-red-200 focus:ring-2 focus:ring-red-500 focus:ring-offset-2 transition-colors duration-200"
                        >
                            削除
                        </button>
                    </div>
                </div>
            {/each}
        </div>
    {/if}
</main>
