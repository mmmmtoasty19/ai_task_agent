import os
import sqlite3
from typing import Literal

from anthropic import Anthropic
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from rich.console import Console

# Import Enviromental variables
load_dotenv()

# Initialize clients
console = Console()
client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

# Configuration
MODEL_NAME = "claude-sonnet-4-20250514"
MAX_ITERATIONS = 10  # ? Not sure if I need this

# ============================================================================
#  Database Actions
# ============================================================================


def initialize_database():
    conn = sqlite3.connect("data/tasks.db")

    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        description TEXT NOT NULL,
        priority TEXT NOT NULL,
        status TEXT NOT NULL,
        due_date TEXT,
        completed_date TEXT
        )
        """)

    return conn


# ============================================================================
# Pydantic Models
# ============================================================================


class Task(BaseModel):
    """Model for Indvidual Task"""

    description: str = Field(description="Task description")
    priority: Literal["low", "medium", "high"] = Field(
        description="priority of task", default="low"
    )
    status: Literal["in_progress", "completed", "on_hold"] = Field(
        default="in_progress", description="Status of task"
    )
    due_date: str | None = Field(default=None, description="Date for task completion")
    completed_date: str | None = Field(
        default=None, description="Date of task completion"
    )


# ============================================================================
# Basic Functions
# ============================================================================


# TODO Add error checking incase task can't be added
def add_task(conn, task: Task):
    """function to add new Task to the Database"""

    cur = conn.cursor()

    task_dict = task.model_dump()

    cur.execute(
        """INSERT INTO tasks (description, priority, status, due_date, completed_date)
           VALUES (?, ?, ?, ?, ?)""",
        (
            task_dict["description"],
            task_dict["priority"],
            task_dict["status"],
            task_dict["due_date"],
            task_dict["completed_date"],
        ),
    )

    conn.commit()


# ============================================================================
# Main Application
# ============================================================================


def main():
    conn = initialize_database()
    try:
        pass
    finally:
        conn.close()


if __name__ == "__main__":
    main()
