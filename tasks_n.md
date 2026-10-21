## Task 6: Implement `main()`

```python
def main():
    pass
```

Write a function that connects all the features together.

**Requirements:**
1. Create an empty task list.
2. Use a loop to keep displaying the menu.
3. Ask the user to select an option.
4. Call the appropriate function based on the selected option.
5. If the user selects `5`, exit the application.
6. If the user enters an invalid choice, display `Invalid choice.`

**Main menu:**

```text
===== TO-DO LIST MANAGER =====

1. Add task
2. View tasks
3. Complete task
4. Delete task
5. Exit

Enter your choice:
```

## Expected Application Interaction

```text
===== TO-DO LIST MANAGER =====

1. Add task
2. View tasks
3. Complete task
4. Delete task
5. Exit

Enter your choice: 1
Enter task title: Study Python
Task added successfully!

===== TO-DO LIST MANAGER =====

1. Add task
2. View tasks
3. Complete task
4. Delete task
5. Exit

Enter your choice: 2

===== MY TASKS =====
1. Study Python - Pending

===== TO-DO LIST MANAGER =====

1. Add task
2. View tasks
3. Complete task
4. Delete task
5. Exit

Enter your choice: 3
Enter task ID: 1
Task completed successfully!

===== TO-DO LIST MANAGER =====

1. Add task
2. View tasks
3. Complete task
4. Delete task
5. Exit

Enter your choice: 2

===== MY TASKS =====
1. Study Python - Completed

===== TO-DO LIST MANAGER =====

1. Add task
2. View tasks
3. Complete task
4. Delete task
5. Exit

Enter your choice: 5
Goodbye!
```

## Final Testing Checklist

- [ ] Add three different tasks.
- [ ] View all three tasks.
- [ ] Mark one task as completed.
- [ ] Verify that its status changes to `Completed`.
- [ ] Delete one task.
- [ ] Verify that the other tasks are still available.
- [ ] Exit the application successfully.

**Bonus challenge (if time permits):** Prevent users from adding tasks with empty titles, and ensure every new task receives a unique ID even after another task has been deleted.

**Project goal:** Build a working menu-driven Python application using six small tasks and reusable functions within 15 minutes.
