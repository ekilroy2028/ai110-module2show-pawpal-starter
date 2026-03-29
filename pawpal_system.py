from dataclasses import dataclass, field
from datetime import date
from typing import List

# -------------------
# Task Class
# -------------------
@dataclass
class Task:
    title: str
    description: str
    due_date: date
    completed: bool = False

    def mark_complete(self):
        pass

    def update_task(self, title: str, description: str, due_date: date):
        pass


# -------------------
# Pet Class
# -------------------
@dataclass
class Pet:
    name: str
    species: str
    age: int
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task):
        pass

    def view_tasks(self):
        pass


# -------------------
# Owner Class
# -------------------
@dataclass
class Owner:
    name: str
    pets: List[Pet] = field(default_factory=list)

    def add_pet(self, pet: Pet):
        pass

    def remove_pet(self, pet: Pet):
        pass

    def view_pets(self):
        pass


# -------------------
# Scheduler Class
# -------------------
class Scheduler:
    def __init__(self):
        self.tasks: List[Task] = []

    def schedule_task(self, task: Task):
        pass

    def get_tasks_for_day(self, target_date: date):
        pass

    def get_overdue_tasks(self):
        pass