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

    from dataclasses import dataclass, field
from datetime import datetime
from typing import List


@dataclass
class Task:
    """Represents a single scheduled activity for a pet."""
    description: str
    time: str  # "HH:MM"
    frequency: str = "once"  # once, daily, weekly
    completed: bool = False

    def mark_complete(self):
        """Mark this task as complete."""
        self.completed = True


@dataclass
class Pet:
    """Represents a pet and its associated tasks."""
    name: str
    species: str
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task):
        """Add a task to this pet."""
        self.tasks.append(task)

    def get_tasks(self) -> List[Task]:
        """Return all tasks for this pet."""
        return self.tasks


@dataclass
class Owner:
    """Represents an owner who manages multiple pets."""
    name: str
    pets: List[Pet] = field(default_factory=list)

    def add_pet(self, pet: Pet):
        """Add a pet to this owner."""
        self.pets.append(pet)

    def get_all_tasks(self):
        """Return a list of (pet_name, task) tuples for all pets."""
        tasks = []
        for pet in self.pets:
            for task in pet.tasks:
                tasks.append((pet.name, task))
        return tasks


class Scheduler:
    """The brain that organizes and retrieves tasks across pets."""

    @staticmethod
    def get_todays_schedule(owner: Owner):
        """Return all tasks for an owner, sorted by time."""
        tasks = owner.get_all_tasks()
        return sorted(tasks, key=lambda t: datetime.strptime(t[1].time, "%H:%M"))
