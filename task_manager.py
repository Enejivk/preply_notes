# Python Project Assignment: Terminal-Based To-Do List Manager

Complete Project Guide — Function-by-Function Implementation

## Project overview

You have been assigned to build a fully functional Terminal-Based To-Do List Manager using Python.

This project will test your understanding of Python concepts you have already learned, including:

- Variables, data types, and type conversion
- Lists and dictionaries
- Conditional statements and loops
- Functions, parameters, arguments, and return values
- String methods
- File handling
- Working with JSON
- Exception handling

Your application should allow users to create tasks, view existing tasks, update them, mark them as completed, delete them, search for tasks, filter tasks, and view task statistics.

All tasks must be saved in a JSON file so that users do not lose their tasks when they close the application.

## Project rules

1. Every major operation must be implemented inside a function.
2. Use the exact function names and parameters provided in each assignment.
3. Implement the functions in the order given, because some functions depend on earlier ones.
4. Do not use external Python packages. You may use built-in modules such as `json` and `os`.
5. Do not store tasks in separate variables. Store all tasks inside one list of dictionaries.
6. Each function must have one clearly defined responsibility. Avoid unnecessarily combining unrelated operations.
7. Test each function before moving to the next task.
8. The application must operate entirely through the terminal.

## Understanding the task data

Each task will be represented by a dictionary containing five keys.

```
task = {    "id": 1,    "title": "Complete Python Assignment",    "description": "Practice Python functions",    "priority": "High",    "completed": False}
```

The application will store multiple tasks inside a list.

```
tasks = [    {        "id": 1,        "title": "Complete Python Assignment",        "description": "Practice Python functions",        "priority": "High",        "completed": False    },    {        "id": 2,        "title": "Read a book",        "description": "Read 20 pages",        "priority": "Medium",        "completed": True    }]
```

The meaning of each field is:

| Key           | Data type | Purpose                                |
| ------------- | --------- | -------------------------------------- |
| `id`          | Integer   | Identifies each task                   |
| `title`       | String    | Name of the task                       |
| `description` | String    | Additional information                 |
| `priority`    | String    | `High`, `Medium`, or `Low`             |
| `completed`   | Boolean   | `True` if completed, otherwise `False` |

In the JSON file, Python's `True` and `False` values will be represented as `true` and `false`.

# Phase 1 — File handling and data persistence

The first phase focuses on loading tasks from a file and saving tasks into a file.

## Task 1: Implement `load_tasks()`

File Handling + JSON

Function signature

```
def load_tasks():    pass
```

### Objective

Create a function that retrieves previously saved tasks from a JSON file.

The application will use a file named `tasks.json`.

When the application starts, this function should check whether the file exists and, if available, load its content into Python.

### Requirements

1. Check whether `tasks.json` exists in the application's working directory.
2. If the file exists, open it in read mode.
3. Read the JSON data and convert it into a Python data structure.
4. Return the list of tasks obtained from the file.
5. If the file does not exist, return an empty list.
6. If the file contains invalid JSON or cannot be read, display a helpful error message and return an empty list.
7. Ensure the file is closed after reading.

### Expected input

This function does not receive any arguments and must not ask the user to type anything.

Its input comes from the contents of `tasks.json`.

Example file content:

```
[
    {
        "id": 1,
        "title": "Study Python",
        "description": "Revise functions",
        "priority": "High",
        "completed": false
    }
]
```

### Expected output

The function must return a Python list, not a JSON string.

For example:

```
result = load_tasks()print(result)
```

Expected output:

```
[    {        'id': 1,        'title': 'Study Python',        'description': 'Revise functions',        'priority': 'High',        'completed': False    }]
```

If the file does not exist, the returned result should be:

```
[]
```

### What the function must NOT do

- Must not create a new task.
- Must not modify existing tasks.
- Must not save data to the file.
- Must not ask the user for input.
- Must not terminate the application simply because the file is missing.

### Completion checklist

- Loads valid JSON successfully.
- Returns an empty list if the file is missing.
- Handles invalid JSON without crashing.
- Returns the loaded data.

## Task 2: Implement `save_tasks(tasks)`

File Handling + JSON

Function signature

```
def save_tasks(tasks):    pass
```

### Objective

Create a function that saves the current list of tasks into `tasks.json`.

This function will be reused whenever a task is added, updated, completed, or deleted.

### Requirements

1. Accept a list of task dictionaries as an argument.
2. Open `tasks.json` in write mode.
3. Convert the list of dictionaries into JSON.
4. Write the JSON data into the file.
5. Format the JSON with an indentation of four spaces so the file is easy to read.
6. If the file does not exist, it should be created automatically.
7. If the file already exists, its contents should be replaced with the current list of tasks.

### Expected input

```
tasks = [    {        "id": 1,        "title": "Buy groceries",        "description": "Buy rice and eggs",        "priority": "Medium",        "completed": False    }]save_tasks(tasks)
```

### Expected output

The function does not need to return anything.

Instead, the file `tasks.json` should contain:

```
[
    {
        "id": 1,
        "title": "Buy groceries",
        "description": "Buy rice and eggs",
        "priority": "Medium",
        "completed": false
    }
]
```

### What the function must NOT do

- Must not ask the user for task information.
- Must not add tasks automatically.
- Must not change task IDs.
- Must not modify the list it receives.
- Must not display the entire list of tasks.

### Completion checklist

- Creates `tasks.json` when needed.
- Saves valid JSON.
- Uses four-space indentation.
- Replaces outdated file contents.
- Does not modify the original task list.

# Phase 2 — Reusable input functions

These functions will be used in several parts of the application to collect and validate user input.

## Task 3: Implement `get_valid_text(message)`

Function signature

```
def get_valid_text(message):    pass
```

### Objective

Create a reusable function that requests text from the user and ensures that the user does not submit an empty value.

This will be useful when asking for task titles and search keywords.

### Requirements

1. Accept a string argument named `message`.
2. Display the supplied message as an input prompt.
3. Collect a text value from the user.
4. Remove unnecessary whitespace from the beginning and end of the input.
5. Check whether the remaining text is empty.
6. If it is empty, show an error and request input again.
7. Continue requesting input until valid text is entered.
8. Return the valid text.

### Expected input and output

Example 1:

```
title = get_valid_text("Enter task title: ")
```

Terminal interaction:

```
Enter task title:
This field cannot be empty.

Enter task title: Learn Python
```

Expected returned value:

```
"Learn Python"
```

Example 2:

User enters:

```
    Buy groceries    
```

Expected returned value:

```
"Buy groceries"
```

### What the function must NOT do

- Must not accept empty text.
- Must not return a value containing only spaces.
- Must not create a task dictionary.
- Must not write anything to the JSON file.
- Must not permanently store the input.

## Task 4: Implement `get_task_id()`

Function signature

```
def get_task_id():    pass
```

### Objective

Create a function that collects a numeric task ID from the user.

The function should reject invalid input and keep requesting another value until the user enters a valid non-negative whole number.

### Requirements

1. Display the message `Enter task ID:`.
2. Collect input from the user.
3. Remove surrounding whitespace.
4. Check whether the input consists only of digits.
5. If valid, convert the input into an integer and return it.
6. If invalid, display an error message.
7. Repeat until the user provides valid input.

### Expected input and output

Example terminal interaction

Enter task ID: abc Please enter a valid number.  Enter task ID: 2.5 Please enter a valid number.  Enter task ID: 3

Expected returned value:

```
3
```

### What the function must NOT do

- Must not return a string.
- Must not accept decimal numbers such as `2.5`.
- Must not search for the task in the task list.
- Must not check whether the provided ID actually exists.
- Must not modify any task.

Important: Checking whether the task ID exists will be handled by a different function. This function only validates the format of the ID.

## Task 5: Implement `get_priority()`

Function signature

```
def get_priority():    pass
```

### Objective

Create a function that allows users to choose the priority level of a task.

The application must support exactly three priorities: High, Medium, and Low.

### Requirements

Display the following options:

```
Choose priority:

1. High
2. Medium
3. Low

Enter choice:
```

The function must return the appropriate string based on the user's selection.

| User input | Returned value |
| ---------- | -------------- |
| `"1"`      | `"High"`       |
| `"2"`      | `"Medium"`     |
| `"3"`      | `"Low"`        |

If the user enters anything else, show an error and ask again.

### Expected input and output

```
priority = get_priority()print(priority)
```

If the user chooses `2`:

```
Medium
```

### What the function must NOT do

- Must not return the numeric menu choice.
- Must not create a task.
- Must not save anything to the JSON file.
- Must not accept priorities outside the three provided choices.

# Phase 3 — Task helper functions

These functions provide reusable operations for finding, identifying, and displaying tasks.

## Task 6: Implement `generate_task_id(tasks)`

Function signature

```
def generate_task_id(tasks):    pass
```

### Objective

Every task requires a unique ID so it can be identified when the user wants to update, complete, or delete it.

Create a function that generates the next available task ID based on the IDs currently stored in the task list.

### Requirements

1. Accept the list of tasks.
2. If the list is empty, return `1`.
3. If the list contains tasks, inspect their IDs.
4. Determine the highest existing task ID.
5. Generate an ID that is one number greater than the highest existing ID.
6. Return the generated integer.

### Expected input and output

Example 1:

```
tasks = []print(generate_task_id(tasks))
```

Expected output:

```
1
```

Example 2:

```
tasks = [    {"id": 1},    {"id": 2},    {"id": 5}]print(generate_task_id(tasks))
```

Expected output:

```
6
```

Example 3:

```
tasks = [    {"id": 10},    {"id": 3},    {"id": 7}]
```

Expected returned value:

```
11
```

### What the function must NOT do

- Must not use the number of tasks as the task ID.
- Must not change existing task IDs.
- Must not create a new task.
- Must not save anything to a file.
- Must not ask the user for an ID.

Note: This project uses the highest existing ID plus one. IDs may therefore be reused if the highest-numbered task is deleted. A permanently increasing ID system can be implemented as an optional improvement.

## Task 7: Implement `find_task(tasks, task_id)`

Function signature

```
def find_task(tasks, task_id):    pass
```

### Objective

Create a reusable function that searches the list of tasks for a task with a specific ID.

Several other functions will depend on this function, including updating tasks, deleting tasks, and completing tasks.

### Requirements

1. Accept the list of tasks.
2. Accept the ID of the task being searched for.
3. Examine the tasks to find one whose `id` matches the supplied ID.
4. If a match is found, return the entire task dictionary.
5. If no match exists, return `None`.

### Expected input

```
tasks = [    {        "id": 1,        "title": "Study Python"    },    {        "id": 2,        "title": "Read a book"    }]
```

Example 1:

```
result = find_task(tasks, 2)print(result)
```

Expected output:

```
{    'id': 2,    'title': 'Read a book'}
```

Example 2:

```
result = find_task(tasks, 9)print(result)
```

Expected output:

```
None
```

### What the function must NOT do

- Must not return only the task title.
- Must not return the task's position in the list.
- Must not ask the user to enter an ID.
- Must not delete or update any tasks.
- Must not print the task instead of returning it.

## Task 8: Implement `display_task(task)`

Function signature

```
def display_task(task):    pass
```

### Objective

Create a function that displays the details of one task in a readable format.

### Requirements

1. Accept a single task dictionary.
2. Display its ID, title, description, priority, and status.
3. Display `Completed` when the `completed` value is `True`.
4. Display `Pending` when the `completed` value is `False`.
5. Use separator lines to make each task easy to read.

### Expected input

```
task = {    "id": 3,    "title": "Learn JSON",    "description": "Practice JSON file handling",    "priority": "High",    "completed": False}display_task(task)
```

### Expected output

```
----------------------------------------
ID: 3
Title: Learn JSON
Description: Practice JSON file handling
Priority: High
Status: Pending
----------------------------------------
```

### What the function must NOT do

- Must not accept an entire list of tasks.
- Must not change the task status.
- Must not save anything to a file.
- Must not return formatted task data instead of displaying it.

## Task 9: Implement `display_task_list(tasks)`

Function signature

```
def display_task_list(tasks):    pass
```

### Objective

Create a reusable function that displays multiple tasks.

Unlike the previous function, which displays one task, this function should be able to display an entire list.

### Requirements

1. Accept a list of task dictionaries.
2. Check whether the list is empty.
3. If empty, display `No tasks found.`
4. Otherwise, display every task in the list.
5. Reuse the `display_task()` function for displaying each individual task.

### Expected input

```
tasks = [    {        "id": 1,        "title": "Study Python",        "description": "Revise loops",        "priority": "High",        "completed": False    },    {        "id": 2,        "title": "Go shopping",        "description": "Buy food",        "priority": "Low",        "completed": True    }]
```

### Expected output

```
----------------------------------------
ID: 1
Title: Study Python
Description: Revise loops
Priority: High
Status: Pending
----------------------------------------
----------------------------------------
ID: 2
Title: Go shopping
Description: Buy food
Priority: Low
Status: Completed
----------------------------------------
```

For an empty list:

```
No tasks found.
```

### What the function must NOT do

- Must not change the order of the list.
- Must not delete any tasks.
- Must not prompt the user for input.
- Must not save tasks.
- Must not duplicate the formatting logic already handled by `display_task()`.

# Phase 4 — Creating and viewing tasks

In this phase, you will begin building the actual features that users will interact with.

## Task 10: Implement `add_task(tasks)`

Function signature

```
def add_task(tasks):    pass
```

### Objective

Create a function that allows users to add a new task to the application.

Each new task must be represented as a dictionary containing all five required fields.

### Requirements

1. Display the heading `ADD NEW TASK`.
2. Ask the user to enter a task title. The title cannot be empty.
3. Ask the user to enter a description. The description may be empty.
4. Allow the user to select a priority: High, Medium, or Low.
5. Generate a unique ID for the new task.
6. Set the new task's completion status to `False` because a newly created task has not yet been completed.
7. Store all the collected information in a dictionary.
8. Add the dictionary to the existing list of tasks.
9. Save the updated list to the JSON file.
10. Display a message confirming that the task was added.

### Functions you must reuse

- `get_valid_text()`
- `get_priority()`
- `generate_task_id()`
- `save_tasks()`

### Expected input

Assume the list of tasks is initially empty.

```
tasks = []add_task(tasks)
```

Example terminal interaction:

```
===== ADD NEW TASK =====

Enter task title: Complete Python Homework
Enter description: Solve 10 Python questions

Choose priority:
1. High
2. Medium
3. Low

Enter choice: 1

Task added successfully!
```

### Expected result

After the function finishes, the `tasks` list should contain:

```
[    {        "id": 1,        "title": "Complete Python Homework",        "description": "Solve 10 Python questions",        "priority": "High",        "completed": False    }]
```

The same task should be saved in `tasks.json`.

### What the function must NOT do

- Must not generate an ID already used by an existing task.
- Must not mark a newly created task as completed.
- Must not remove any existing tasks.
- Must not replace the entire list with only the new task.
- Must not duplicate logic that already exists in reusable helper functions.

### Challenge

Add three tasks consecutively. Verify that all three tasks exist in the JSON file, have different IDs, and have their completion statuses set to `False`.

## Task 11: Implement `view_tasks(tasks)`

Function signature

```
def view_tasks(tasks):    pass
```

### Objective

Allow the user to view every task currently stored in the application.

This function should serve as the main entry point for displaying all tasks.

### Requirements

1. Accept a list of tasks.
2. Display the heading `ALL TASKS`.
3. Display all tasks with their details.
4. If the list is empty, display an appropriate message.
5. Reuse the function that was previously created for displaying a list of tasks.

### Expected input

```
tasks = [    {        "id": 1,        "title": "Study Python",        "description": "Practice functions",        "priority": "High",        "completed": False    },    {        "id": 2,        "title": "Clean room",        "description": "Organize desk",        "priority": "Low",        "completed": True    }]view_tasks(tasks)
```

### Expected output

```
===== ALL TASKS =====

----------------------------------------
ID: 1
Title: Study Python
Description: Practice functions
Priority: High
Status: Pending
----------------------------------------

----------------------------------------
ID: 2
Title: Clean room
Description: Organize desk
Priority: Low
Status: Completed
----------------------------------------
```

### What the function must NOT do

- Must not ask the user to select a particular task.
- Must not edit or delete tasks.
- Must not filter out completed or pending tasks.
- Must not write to the JSON file.
- Must not recreate formatting logic already defined in helper functions.

# Phase 5 — Updating task information

## Task 12: Implement `complete_task(tasks)`

Function signature

```
def complete_task(tasks):    pass
```

### Objective

Allow a user to mark an existing task as completed.

For example, when a student finishes an assignment, they should be able to find the assignment using its task ID and update its status.

### Requirements

1. Display the heading `COMPLETE TASK`.
2. Check whether the task list is empty.
3. If empty, display `No tasks available.` and stop the operation.
4. Otherwise, display all existing tasks.
5. Ask the user to enter the ID of the task they want to complete.
6. Find the task matching the supplied ID.
7. If the task does not exist, display `Task not found.`
8. If the task is already completed, display `This task is already completed.`
9. Otherwise, change its `completed` value from `False` to `True`.
10. Save the updated task list to the JSON file.
11. Display a success message.

### Functions you must reuse

- `display_task_list()`
- `get_task_id()`
- `find_task()`
- `save_tasks()`

### Expected input

```
tasks = [    {        "id": 1,        "title": "Read a book",        "description": "Read chapter 5",        "priority": "Medium",        "completed": False    }]
```

Terminal interaction:

```
===== COMPLETE TASK =====

ID: 1
Title: Read a book
Description: Read chapter 5
Priority: Medium
Status: Pending

Enter task ID: 1

Task marked as completed!
```

### Expected result

```
{    "id": 1,    "title": "Read a book",    "description": "Read chapter 5",    "priority": "Medium",    "completed": True}
```

The updated value must also appear in `tasks.json`.

### Edge cases to test

| Situation                            | Expected behavior              |
| ------------------------------------ | ------------------------------ |
| No tasks exist                       | Display `No tasks available.`  |
| User enters a nonexistent ID         | Display `Task not found.`      |
| Task is already completed            | Display an informative message |
| Task is pending                      | Mark it completed and save     |
| User enters letters instead of an ID | Reject the input and ask again |

### What the function must NOT do

- Must not create a new task.
- Must not remove an existing task.
- Must not change the task title, description, or priority.
- Must not mark every task as completed.
- Must not save changes if no task was updated.

## Task 13: Implement `update_task_title(task)`

Function signature

```
def update_task_title(task):    pass
```

### Objective

Create a function that changes the title of an existing task.

### Requirements

1. Accept a single task dictionary.
2. Ask the user to enter a new title.
3. Ensure the new title is not empty.
4. Replace the current title with the new title.

### Expected input

```
task = {    "id": 1,    "title": "Read a book",    "description": "Read chapter 5",    "priority": "Medium",    "completed": False}
```

Terminal interaction:

```
Enter new title: Read Python Documentation
```

### Expected result

The title should change to:

```
"Read Python Documentation"
```

All other task fields must remain unchanged.

### What the function must NOT do

- Must not change the task ID.
- Must not modify the description or priority.
- Must not change the completion status.
- Must not save the task directly to the JSON file.

Important: The main update function will handle saving changes. This helper is only responsible for modifying the title.

## Task 14: Implement `update_task_description(task)`

Function signature

```
def update_task_description(task):    pass
```

### Objective

Allow users to change the description of an existing task.

### Requirements

1. Accept one task dictionary.
2. Ask the user to enter a new description.
3. Remove unnecessary spaces at the beginning and end.
4. Replace the existing description with the new description.
5. Allow the user to provide an empty description.

### Expected input

Existing task:

```
{    "id": 2,    "title": "Go shopping",    "description": "Buy milk",    "priority": "Low",    "completed": False}
```

Terminal interaction:

```
Enter new description: Buy milk, rice and eggs
```

### Expected result

```
"description": "Buy milk, rice and eggs"
```

### What the function must NOT do

- Must not change the task title.
- Must not modify the task ID.
- Must not reject an empty description.
- Must not write directly to the JSON file.

## Task 15: Implement `update_task_priority(task)`

Function signature

```
def update_task_priority(task):    pass
```

### Objective

Allow users to change a task's priority.

For example, a task previously classified as Low priority may become urgent and need to be changed to High priority.

### Requirements

1. Accept one task dictionary.
2. Display the priority selection menu.
3. Allow the user to choose a new priority.
4. Ensure that the selected priority is valid.
5. Replace the current priority with the selected priority.
6. Reuse the existing function responsible for priority selection.

### Expected input

Existing value:

```
"priority": "Low"
```

Terminal interaction:

```
Choose priority:
1. High
2. Medium
3. Low

Enter choice: 1
```

### Expected result

```
"priority": "High"
```

### What the function must NOT do

- Must not modify other task fields.
- Must not create an entirely new task.
- Must not duplicate the priority selection logic.
- Must not save the task directly to the JSON file.

## Task 16: Implement `show_update_menu()`

Function signature

```
def show_update_menu():    pass
```

### Objective

Create a function that displays the available options for updating an existing task.

### Requirements

Display the following menu:

```
What would you like to update?

1. Title
2. Description
3. Priority
4. Cancel
```

### Expected input

No function arguments are required.

```
show_update_menu()
```

### Expected output

The menu should appear in the terminal exactly as specified.

### What the function must NOT do

- Must not modify a task.
- Must not save anything.
- Must not ask for a task ID.
- Must not process the user's menu choice.
- Must not return a task dictionary.

## Task 17: Implement `update_task(tasks)`

Function signature

```
def update_task(tasks):    pass
```

### Objective

Combine the previously created update functions into one complete feature that allows users to edit an existing task.

This function should coordinate the update process rather than performing every individual operation itself.

### Requirements

1. Display the heading `UPDATE TASK`.
2. Check whether the task list is empty.
3. If no tasks exist, display `No tasks available.` and stop.
4. Display all existing tasks.
5. Ask the user to enter a task ID.
6. Search for the task using its ID.
7. If the task cannot be found, display `Task not found.` and stop.
8. Display the update menu.
9. Ask the user which field they want to update.
10. Call the correct update helper function based on the selected option.
11. If the user chooses Cancel, stop without making changes.
12. If the user enters an invalid menu option, display an error and stop.
13. If a valid update was performed, save the modified list to `tasks.json`.
14. Display `Task updated successfully!`

### Functions you must reuse

- `display_task_list()`
- `get_task_id()`
- `find_task()`
- `show_update_menu()`
- `update_task_title()`
- `update_task_description()`
- `update_task_priority()`
- `save_tasks()`

### Expected input

Assume the user already has the following task:

```
{    "id": 2,    "title": "Study Python",    "description": "Revise dictionaries",    "priority": "Low",    "completed": False}
```

Terminal interaction:

```
===== UPDATE TASK =====

Enter task ID: 2

What would you like to update?

1. Title
2. Description
3. Priority
4. Cancel

Enter your choice: 3

Choose priority:
1. High
2. Medium
3. Low

Enter choice: 1

Task updated successfully!
```

### Expected result

```
{    "id": 2,    "title": "Study Python",    "description": "Revise dictionaries",    "priority": "High",    "completed": False}
```

Only the priority should change.

### What the function must NOT do

- Must not modify tasks that do not match the selected ID.
- Must not change a task's ID.
- Must not delete the task.
- Must not make changes when the user selects Cancel.
- Must not perform multiple different update operations for one menu choice.

# Phase 6 — Deleting tasks

## Task 18: Implement `delete_task(tasks)`

Function signature

```
def delete_task(tasks):    pass
```

### Objective

Create a function that permanently removes a selected task from the task list and updates the JSON file.

Since deletion removes stored information, the user must confirm the action before the task is deleted.

### Requirements

1. Display the heading `DELETE TASK`.
2. Check whether any tasks exist.
3. If no tasks exist, display a message and stop.
4. Display the existing tasks.
5. Ask the user for the ID of the task they wish to delete.
6. Find the task matching that ID.
7. If no matching task exists, display `Task not found.`
8. If the task exists, display a confirmation message that includes its title.
9. Ask the user to type `yes` or `no`.
10. Accept `yes` regardless of capitalization and surrounding spaces.
11. If the user enters `yes`, remove the selected task.
12. Save the updated task list into `tasks.json`.
13. Display `Task deleted successfully!`
14. If the user enters anything other than `yes`, cancel the operation.

### Expected input

```
tasks = [    {        "id": 1,        "title": "Study Python",        "description": "Practice loops",        "priority": "High",        "completed": False    },    {        "id": 2,        "title": "Buy groceries",        "description": "Buy rice",        "priority": "Low",        "completed": False    }]
```

Terminal interaction:

```
===== DELETE TASK =====

Enter task ID: 2

Are you sure you want to delete 'Buy groceries'? (yes/no): yes

Task deleted successfully!
```

### Expected result

The task with ID `2` must no longer exist.

```
[    {        "id": 1,        "title": "Study Python",        "description": "Practice loops",        "priority": "High",        "completed": False    }]
```

The deleted task must also disappear from `tasks.json`.

### Edge cases

| Situation                      | Expected behavior             |
| ------------------------------ | ----------------------------- |
| Task list is empty             | Display a message and stop    |
| Task ID does not exist         | Display `Task not found.`     |
| User enters `no`               | Cancel deletion               |
| User enters `YES`              | Delete the task               |
| User enters `maybe`            | Cancel deletion               |
| Valid task ID and confirmation | Delete only the matching task |

### What the function must NOT do

- Must not delete a task without confirmation.
- Must not delete every task in the list.
- Must not delete another task with a different ID.
- Must not automatically renumber the remaining task IDs.
- Must not update the JSON file if deletion was cancelled.

# Phase 7 — Searching for tasks

## Task 19: Implement `search_tasks(tasks)`

Function signature

```
def search_tasks(tasks):    pass
```

### Objective

Build a feature that allows users to search for tasks by entering a keyword.

The keyword should be compared against both task titles and descriptions.

The search must be case-insensitive.

For example, searching for `python` should find tasks containing `Python`, `PYTHON`, or `python`.

### Requirements

1. Display the heading `SEARCH TASKS`.
2. Ask the user to enter a search keyword.
3. Ensure that the keyword is not empty.
4. Search through the task list.
5. Check whether the keyword appears anywhere inside each task's title or description.
6. Ignore differences between uppercase and lowercase letters.
7. Collect all matching tasks into a separate list.
8. Display the number of matching tasks.
9. Display the details of each matching task.
10. If no tasks match, display `No tasks found.`

### Functions you must reuse

- `get_valid_text()`
- `display_task_list()`

### Expected input

```
tasks = [    {        "id": 1,        "title": "Learn Python",        "description": "Study functions",        "priority": "High",        "completed": False    },    {        "id": 2,        "title": "Buy groceries",        "description": "Buy milk and eggs",        "priority": "Low",        "completed": False    },    {        "id": 3,        "title": "Complete assignment",        "description": "Solve Python questions",        "priority": "Medium",        "completed": True    }]
```

Terminal interaction:

```
===== SEARCH TASKS =====

Enter search keyword: python
```

### Expected output

```
Found 2 matching task(s).

----------------------------------------
ID: 1
Title: Learn Python
Description: Study functions
Priority: High
Status: Pending
----------------------------------------

----------------------------------------
ID: 3
Title: Complete assignment
Description: Solve Python questions
Priority: Medium
Status: Completed
----------------------------------------
```

### Additional test cases

| Search keyword | Expected matching IDs |
| -------------- | --------------------- |
| `python`       | 1, 3                  |
| `PYTHON`       | 1, 3                  |
| `milk`         | 2                     |
| `assignment`   | 3                     |
| `JavaScript`   | No matches            |

### What the function must NOT do

- Must not permanently modify task titles or descriptions to lowercase.
- Must not delete tasks that don't match.
- Must not change task statuses.
- Must not search only titles while ignoring descriptions.
- Must not save the search results to the JSON file.
- Must not change the original task list.

# Phase 8 — Filtering tasks

Filtering is different from searching.

Searching finds tasks containing a specific keyword. Filtering finds tasks that meet a specific condition, such as being completed or having High priority.

## Task 20: Implement `show_filter_menu()`

Function signature

```
def show_filter_menu():    pass
```

### Objective

Create a function responsible for displaying the available task filtering options.

### Requirements

Display this menu:

```
===== FILTER TASKS =====

1. Pending tasks
2. Completed tasks
3. High priority tasks
4. Medium priority tasks
5. Low priority tasks
6. Cancel
```

### Expected input

This function takes no arguments.

```
show_filter_menu()
```

### Expected output

The filtering options should appear in the terminal.

### What the function must NOT do

- Must not collect user input.
- Must not filter any tasks.
- Must not change task information.
- Must not return a list of tasks.

## Task 21: Implement `filter_by_status(tasks, completed)`

Function signature

```
def filter_by_status(tasks, completed):    pass
```

### Objective

Create a reusable function that filters tasks according to their completion status.

The function must support both completed and pending tasks.

### Requirements

1. Accept the list of tasks.
2. Accept a Boolean argument named `completed`.
3. Examine each task's completion status.
4. Collect tasks whose status matches the supplied Boolean value.
5. Return a new list containing only matching tasks.
6. Return an empty list when no matches exist.

### Expected input

```
tasks = [    {"id": 1, "completed": True},    {"id": 2, "completed": False},    {"id": 3, "completed": True},    {"id": 4, "completed": False}]
```

Example 1:

```
result = filter_by_status(tasks, True)print(result)
```

Expected output:

```
[    {"id": 1, "completed": True},    {"id": 3, "completed": True}]
```

Example 2:

```
result = filter_by_status(tasks, False)print(result)
```

Expected output:

```
[    {"id": 2, "completed": False},    {"id": 4, "completed": False}]
```

### What the function must NOT do

- Must not ask the user for input.
- Must not print the matching tasks.
- Must not return only task IDs.
- Must not modify any completion status.
- Must not remove unmatched tasks from the original list.

## Task 22: Implement `filter_by_priority(tasks, priority)`

Function signature

```
def filter_by_priority(tasks, priority):    pass
```

### Objective

Create a reusable function that returns tasks matching a specific priority level.

### Requirements

1. Accept the list of tasks.
2. Accept a priority string.
3. Examine the `priority` field in every task.
4. Find all tasks whose priority matches the supplied value.
5. Return a new list of matching task dictionaries.
6. Return an empty list when no match exists.

For this function, valid priority arguments will be `High`, `Medium`, and `Low`, using that exact capitalization.

### Expected input

```
tasks = [    {"id": 1, "priority": "High"},    {"id": 2, "priority": "Low"},    {"id": 3, "priority": "High"},    {"id": 4, "priority": "Medium"}]
```

Example:

```
result = filter_by_priority(tasks, "High")print(result)
```

Expected output:

```
[    {"id": 1, "priority": "High"},    {"id": 3, "priority": "High"}]
```

### What the function must NOT do

- Must not change a task's priority.
- Must not delete any tasks.
- Must not ask the user for a priority.
- Must not print the matching tasks.
- Must not save the filtered list to a file.

## Task 23: Implement `filter_tasks(tasks)`

Function signature

```
def filter_tasks(tasks):    pass
```

### Objective

Combine the filtering functions into one complete feature that users can interact with.

This function will be responsible for displaying the filter menu, collecting the user's choice, selecting the appropriate filter, and displaying the results.

### Requirements

1. Display the filtering menu.
2. Ask the user to select a filtering option.
3. If the user chooses option `1`, find all pending tasks.
4. If the user chooses option `2`, find all completed tasks.
5. If the user chooses option `3`, find all High priority tasks.
6. If the user chooses option `4`, find all Medium priority tasks.
7. If the user chooses option `5`, find all Low priority tasks.
8. If the user chooses option `6`, cancel and return without displaying results.
9. If the user enters an invalid option, display `Invalid choice.` and stop.
10. For valid filtering options, display all matching tasks.

### Functions you must reuse

- `show_filter_menu()`
- `filter_by_status()`
- `filter_by_priority()`
- `display_task_list()`

### Expected input

Suppose the task list contains:

| ID | Title             | Priority | Status    |
| -- | ----------------- | -------- | --------- |
| 1  | Study Python      | High     | Pending   |
| 2  | Read a book       | Low      | Completed |
| 3  | Buy groceries     | Medium   | Pending   |
| 4  | Finish assignment | High     | Completed |
| 5  | Clean room        | Low      | Pending   |

Terminal interaction:

```
===== FILTER TASKS =====

1. Pending tasks
2. Completed tasks
3. High priority tasks
4. Medium priority tasks
5. Low priority tasks
6. Cancel

Enter your choice: 3
```

### Expected output

The application should display the complete details of tasks with IDs `1` and `4`, because both have High priority.

### Additional test cases

| Selected option | Expected matching IDs           |
| --------------- | ------------------------------- |
| `1` Pending     | 1, 3, 5                         |
| `2` Completed   | 2, 4                            |
| `3` High        | 1, 4                            |
| `4` Medium      | 3                               |
| `5` Low         | 2, 5                            |
| `6` Cancel      | Return without displaying tasks |

### What the function must NOT do

- Must not modify task statuses.
- Must not change task priorities.
- Must not delete tasks that fail the filter condition.
- Must not save filtered results to the JSON file.
- Must not duplicate filtering logic already handled by helper functions.

# Phase 9 — Task statistics

Your application should provide users with an overview of their productivity.

For example, a user should be able to see how many tasks they have created and what percentage they have completed.

## Task 24: Implement `count_completed_tasks(tasks)`

Function signature

```
def count_completed_tasks(tasks):    pass
```

### Objective

Create a function that counts the number of completed tasks.

### Requirements

1. Accept the list of tasks.
2. Examine the completion status of every task.
3. Count only tasks whose `completed` value is `True`.
4. Return the total count as an integer.
5. Return `0` when the list is empty or contains no completed tasks.

### Expected input

```
tasks = [    {"id": 1, "completed": True},    {"id": 2, "completed": False},    {"id": 3, "completed": True},    {"id": 4, "completed": True}]
```

Example:

```
result = count_completed_tasks(tasks)print(result)
```

Expected output:

```
3
```

### What the function must NOT do

- Must not count pending tasks.
- Must not return a list of completed tasks.
- Must not print the number instead of returning it.
- Must not modify any task.

## Task 25: Implement `count_pending_tasks(tasks)`

Function signature

```
def count_pending_tasks(tasks):    pass
```

### Objective

Create a function that counts tasks that have not yet been completed.

### Requirements

1. Accept the task list.
2. Examine every task.
3. Count only tasks whose `completed` value is `False`.
4. Return the total as an integer.
5. Return `0` if no pending tasks exist.

### Expected input

```
tasks = [    {"id": 1, "completed": True},    {"id": 2, "completed": False},    {"id": 3, "completed": False},    {"id": 4, "completed": True}]
```

Expected output:

```
print(count_pending_tasks(tasks))
```

```
2
```

### What the function must NOT do

- Must not count completed tasks.
- Must not change any task's status.
- Must not ask the user for input.
- Must not print instead of returning the count.

## Task 26: Implement `calculate_completion_percentage(tasks)`

Function signature

```
def calculate_completion_percentage(tasks):    pass
```

### Objective

Calculate the percentage of tasks that have been completed.

The calculation should be based on the total number of tasks and the number of completed tasks.

### Formula

\\[ \text{Completion percentage}=\frac{\text{Completed tasks}}{\text{Total tasks}}\times100 \\]

### Requirements

1. Accept a list of tasks.
2. Determine the total number of tasks.
3. Determine how many tasks are completed.
4. Calculate the completion percentage.
5. Return the result as a number.
6. If the list is empty, return `0` to avoid division by zero.

### Expected input and output

Example 1:

```
tasks = [    {"completed": True},    {"completed": True},    {"completed": False},    {"completed": False}]print(calculate_completion_percentage(tasks))
```

Expected output:

```
50.0
```

Example 2:

```
tasks = [    {"completed": True},    {"completed": True},    {"completed": True},    {"completed": False}]
```

Expected returned value:

```
75.0
```

Example 3:

```
tasks = []
```

Expected returned value:

```
0
```

### What the function must NOT do

- Must not modify task statuses.
- Must not return a string containing `%`.
- Must not print the result instead of returning it.
- Must not crash when the list is empty.
- Must not ask the user to enter the total number of tasks.

## Task 27: Implement `show_statistics(tasks)`

Function signature

```
def show_statistics(tasks):    pass
```

### Objective

Create a feature that displays a summary of the user's tasks.

It must provide information about the total number of tasks, completed tasks, pending tasks, and completion percentage.

### Requirements

1. Display the heading `TASK STATISTICS`.
2. Determine the total number of tasks.
3. Calculate the number of completed tasks.
4. Calculate the number of pending tasks.
5. Calculate the completion percentage.
6. Display each statistic with a clear label.
7. Format the completion percentage to one decimal place.

### Functions you must reuse

- `count_completed_tasks()`
- `count_pending_tasks()`
- `calculate_completion_percentage()`

### Expected input

Suppose there are eight tasks, of which six are completed and two are pending.

### Expected output

```
===== TASK STATISTICS =====

Total tasks: 8
Completed tasks: 6
Pending tasks: 2
Completion rate: 75.0%
```

If no tasks exist:

```
===== TASK STATISTICS =====

Total tasks: 0
Completed tasks: 0
Pending tasks: 0
Completion rate: 0.0%
```

### What the function must NOT do

- Must not ask the user for the task counts.
- Must not modify tasks.
- Must not save anything to the file.
- Must not automatically mark tasks as completed.
- Must not recalculate all statistics using duplicated counting logic.

# Phase 10 — Building the main application

You have now implemented the individual features of your To-Do List Manager.

Your final responsibility is to connect all these functions to create one working application.

## Task 28: Implement `show_main_menu()`

Function signature

```
def show_main_menu():    pass
```

### Objective

Create the main menu users will see whenever the application starts or finishes performing an operation.

### Requirements

Your function must display the following menu:

```
========================================
           MY TASK MANAGER
========================================

1. Add a new task
2. View all tasks
3. Mark task as completed
4. Update a task
5. Delete a task
6. Search tasks
7. Filter tasks
8. View task statistics
9. Exit

========================================
```

### Expected input

```
show_main_menu()
```

The function does not take any arguments.

### Expected output

The menu should appear in the terminal.

### What the function must NOT do

- Must not ask the user to select an option.
- Must not create, modify, or delete tasks.
- Must not load or save the JSON file.
- Must not call any task management function.

## Task 29: Implement `process_menu_choice(choice, tasks)`

Function signature

```
def process_menu_choice(choice, tasks):    pass
```

### Objective

Create a function that receives the user's menu selection and performs the appropriate operation.

This function is responsible for deciding which previously implemented feature should run.

### Requirements

1. Accept two arguments: `choice` and `tasks`.
2. The `choice` argument will be a string representing the user's selection.
3. Check the user's choice and call the corresponding function.
4. If the user enters `"1"`, call the function responsible for adding a task.
5. If the user enters `"2"`, display all tasks.
6. Continue mapping every menu option to its appropriate function.
7. If the user enters `"9"`, display a goodbye message and return `False`.
8. For all other choices, including invalid choices, return `True` after handling them.
9. For invalid choices, display an error message.

### Expected input and behavior

| Input choice | Expected operation     | Returned value |
| ------------ | ---------------------- | -------------- |
| `"1"`        | Add a task             | `True`         |
| `"2"`        | View all tasks         | `True`         |
| `"3"`        | Complete a task        | `True`         |
| `"4"`        | Update a task          | `True`         |
| `"5"`        | Delete a task          | `True`         |
| `"6"`        | Search tasks           | `True`         |
| `"7"`        | Filter tasks           | `True`         |
| `"8"`        | Show statistics        | `True`         |
| `"9"`        | Exit application       | `False`        |
| `"15"`       | Display invalid choice | `True`         |

Example:

```
tasks = []result = process_menu_choice("9", tasks)print(result)
```

Expected output:

```
Thank you for using Task Manager!
False
```

### What the function must NOT do

- Must not create its own task list.
- Must not load the JSON file repeatedly.
- Must not contain the full implementation of every feature.
- Must not ask the user to enter their main menu choice.
- Must not terminate the entire Python program directly.

Important: This function must return a Boolean value because the next function will use that value to decide whether the application should continue running.

## Task 30: Implement `main()`

Function signature

```
def main():    pass
```

### Objective

This is the final task.

Create the function that brings the entire application together.

It will serve as the main entry point and control the overall operation of your To-Do List Manager.

### Requirements

1. When the application starts, load previously saved tasks from `tasks.json`.
2. Store the loaded tasks in a variable.
3. Start a loop that keeps the application running.
4. Display the main menu.
5. Ask the user to select an option between `1` and `9`.
6. Pass the selected option and the task list to `process_menu_choice()`.
7. Use the Boolean result returned by `process_menu_choice()` to determine whether the loop should continue.
8. After completing an operation, show the main menu again.
9. Continue until the user chooses option `9`.
10. When the user exits, stop the loop and allow the program to end normally.

### Functions you must reuse

- `load_tasks()`
- `show_main_menu()`
- `process_menu_choice()`

### Expected input and output

Example terminal interaction:

```
========================================
           MY TASK MANAGER
========================================

1. Add a new task
2. View all tasks
3. Mark task as completed
4. Update a task
5. Delete a task
6. Search tasks
7. Filter tasks
8. View task statistics
9. Exit

========================================

Enter your choice (1-9): 2

===== ALL TASKS =====

No tasks found.


========================================
           MY TASK MANAGER
========================================

1. Add a new task
2. View all tasks
3. Mark task as completed
4. Update a task
5. Delete a task
6. Search tasks
7. Filter tasks
8. View task statistics
9. Exit

========================================

Enter your choice (1-9): 9

Thank you for using Task Manager!
```

### What the function must NOT do

- Must not duplicate the task management functions.
- Must not create a new empty task list every time the menu appears.
- Must not load the JSON file on every loop iteration.
- Must not terminate after completing just one operation.
- Must not continue displaying the menu after the user chooses Exit.

### Final requirement

Configure your Python file so that `main()` runs when the program is executed directly.

# Phase 11 — Final project testing

After implementing all 30 tasks, you must test the application from beginning to end.

Do not consider the project complete simply because it runs without syntax errors.

Your program must produce the correct results.

## Final testing checklist

Project test progress

0/34 passed

Test 1 — Creating tasks

0/4

Start the program with no existing JSON file.

Add three tasks with different priorities.

Verify that the tasks have distinct IDs.

Verify that the tasks have been saved to tasks.json.

Test 2 — Saving and loading

0/4

Create multiple tasks and exit the application.

Restart the application.

Verify that previously created tasks are still available.

Confirm that JSON Boolean values are loaded correctly.

Test 3 — Completing and updating

0/5

Mark one pending task as completed.

Try completing the same task again.

Update another task's title.

Update a task's description and priority.

Verify that all changes remain after restarting.

Test 4 — Deleting

0/5

Attempt to delete a nonexistent task.

Choose No when asked to confirm deletion.

Confirm that the task was not deleted.

Delete an existing task by confirming Yes.

Verify that other tasks remain unchanged.

Test 5 — Searching and filtering

0/6

Search for a keyword that exists in a title.

Search for a keyword that exists only in a description.

Test a search with different capitalization.

Filter completed and pending tasks.

Filter High, Medium, and Low priority tasks.

Verify that filtering does not delete any tasks.

Test 6 — Statistics and validation

0/6

Check statistics for an empty task list.

Check statistics with both completed and pending tasks.

Verify that completion percentage is correct.

Try entering invalid task IDs.

Try entering invalid menu choices.

Try submitting an empty task title.

Test 7 — Application lifecycle

0/4

Perform several operations without restarting.

Exit through menu option 9.

Restart the program and confirm that data persists.

Verify that the application does not crash when tasks.json is missing.

&#x20;Reset checklist

## Final submission requirements

Your completed project must contain:

```
todo_project/
│
├── main.py
│
└── tasks.json
```

The `tasks.json` file will be created by the application when tasks are first saved, so it does not need to exist before the program runs.

Your application must satisfy all the following conditions:

- All 30 assigned functions are implemented.
- Every menu option works correctly.
- The project uses lists and dictionaries to manage task information.
- Tasks are saved and loaded through JSON.
- Data remains available after restarting the program.
- The application handles expected invalid user input.
- Functions reuse previously implemented helpers.
- The user can perform multiple operations in one application session.

## Bonus challenges — Optional

Complete these only after the main application is fully working.

1. Reopen a completed task: Allow a user to change a completed task back to Pending.
2. Task deadlines: Allow users to assign due dates to tasks and display them when viewing tasks.
3. Sort tasks: Allow users to display High priority tasks first, followed by Medium and Low priority tasks.
4. Clear completed tasks: Allow users to remove all completed tasks, but ask for confirmation before proceeding.
5. Permanent unique IDs: Improve the ID generation system so previously used task IDs are never reused, even after their tasks are deleted.
6. Protect invalid saved data: Check that the JSON file contains a list of valid task dictionaries before the application attempts to use it.

Project completion goal: By completing these 30 functions in order, you will have built a fully functional Python To-Do List Manager from scratch.

You should be able to explain what every function does, why it exists, what arguments it receives, what it returns, and how it works together with the other functions in the application.
