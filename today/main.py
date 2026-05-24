from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Task(BaseModel):
    id: int
    title: str
    subject: str
    description: Optional[str] = None
    priority: str = "medium"
    deadline: Optional[str] = None
    completed: bool = False
    created: str


class TaskCreate(BaseModel):
    title: str
    subject: str
    description: Optional[str] = None
    priority: str = "medium"
    deadline: Optional[str] = None


# Fake database
tasks = [
    Task(
        id=1,
        title="Build REST API",
        subject="Python",
        description="Create a RESTful API using FastAPI with proper error handling",
        priority="high",
        deadline="2026-05-28T14:00:00",
        completed=False,
        created="2026-05-24T09:00:00"
    ),
    Task(
        id=2,
        title="DOM Manipulation Tutorial",
        subject="JavaScript",
        description="Learn and implement DOM manipulation techniques",
        priority="medium",
        deadline="2026-05-26T18:00:00",
        completed=True,
        created="2026-05-20T10:30:00"
    ),
    Task(
        id=3,
        title="Object-Oriented Programming",
        subject="Java",
        description="Study inheritance, polymorphism, and encapsulation concepts",
        priority="high",
        deadline="2026-05-29T16:00:00",
        completed=False,
        created="2026-05-22T08:15:00"
    ),
    Task(
        id=4,
        title="Implement Quick Sort",
        subject="C++",
        description="Write and optimize the Quick Sort algorithm implementation",
        priority="medium",
        deadline="2026-05-27T12:00:00",
        completed=False,
        created="2026-05-23T11:45:00"
    ),
    Task(
        id=5,
        title="Concurrency Patterns",
        subject="Go",
        description="Explore goroutines and channels for concurrent programming",
        priority="low",
        deadline="2026-05-30T10:00:00",
        completed=False,
        created="2026-05-24T13:20:00"
    ),
    Task(
        id=6,
        title="Data Structures Review",
        subject="Python",
        description="Review lists, dictionaries, sets, and their operations",
        priority="medium",
        deadline="2026-05-25T20:00:00",
        completed=True,
        created="2026-05-18T14:00:00"
    ),
    Task(
        id=7,
        title="Async/Await Practice",
        subject="JavaScript",
        description="Practice async functions and promise handling",
        priority="high",
        deadline="2026-05-24T23:59:00",
        completed=False,
        created="2026-05-23T16:30:00"
    ),
    Task(
        id=8,
        title="Exception Handling",
        subject="Java",
        description="Implement try-catch blocks and custom exceptions",
        priority="low",
        deadline="2026-05-31T15:00:00",
        completed=False,
        created="2026-05-24T09:45:00"
    ),
    Task(
        id=9,
        title="Memory Management",
        subject="C++",
        description="Study pointers, references, and memory allocation",
        priority="high",
        deadline="2026-05-28T17:00:00",
        completed=False,
        created="2026-05-21T10:00:00"
    ),
    Task(
        id=10,
        title="Web Framework Basics",
        subject="Go",
        description="Learn basics of Go web frameworks like Gin or Echo",
        priority="medium",
        deadline="2026-05-29T11:00:00",
        completed=True,
        created="2026-05-19T12:30:00"
    ),
]


@app.get("/")
def home():
    return {
        "message": "Task API is running"
    }


@app.get("/tasks")
def get_tasks():
    return tasks


@app.get("/tasks/{task_id}")
def get_task(task_id: int):

    for task in tasks:

        if task.id == task_id:
            return task

    raise HTTPException(
        status_code=404,
        detail="Task not found"
    )


@app.post("/tasks")
def create_task(task: TaskCreate):
    new_task = Task(
        id=len(tasks) + 1,
        title=task.title,
        subject=task.subject,
        description=task.description,
        priority=task.priority,
        deadline=task.deadline,
        completed=False,
        created=datetime.now().isoformat()
    )

    tasks.append(new_task)

    return {
        "message": "Task created successfully",
        "task": new_task
    }


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for index, task in enumerate(tasks):
        if task.id == task_id:
            deleted_task = tasks.pop(index)
            return {
                "message": "Task deleted successfully",
                "task": deleted_task
            }

    raise HTTPException(
        status_code=404,
        detail="Task not found"
    )


@app.put("/tasks/{task_id}/complete")
def complete_task(task_id: int):
    for task in tasks:
        if task.id == task_id:
            task.completed = not task.completed
            return {
                "message": "Task updated successfully",
                "task": task
            }

    raise HTTPException(
        status_code=404,
        detail="Task not found"
    )


@app.get("/tasks/filter/today")
def get_today_tasks():
    today = datetime.now().strftime("%Y-%m-%d")
    today_tasks = [task for task in tasks if task.deadline and task.deadline.startswith(today)]
    return today_tasks


@app.get("/tasks/filter/completed")
def get_completed_tasks(completed: bool = True):
    return [task for task in tasks if task.completed == completed]


@app.get("/tasks/filter/priority/{priority}")
def get_tasks_by_priority(priority: str):
    return [task for task in tasks if task.priority == priority.lower()]


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True)