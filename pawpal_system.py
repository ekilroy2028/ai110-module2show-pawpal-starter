from dataclasses import dataclass, field
from datetime import datetime, timedelta
from typing import List, Optional


@dataclass
class Task:
    """Represents a single scheduled activity for a pet."""
    description: str
    time: str  # "HH:MM"
    frequency: str = "once"  # once, daily, weekly
    completed: bool = False

    def mark_complete(self):
        """Mark task as complete and return next occurrence if recurring."""
        self.completed = True
        return self.next_occurrence()

    def next_occurrence(self):
        """Generate next occurrence for recurring tasks."""
        if self.frequency == "daily":
            return Task(self.description, self.time, self.frequency)

        if self.frequency == "weekly":
            return Task(self.description, self.time, self.frequency)

        return None


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
    def sort_by_time(tasks):
        """Sort tasks by HH:MM time."""
        return sorted(tasks, key=lambda t: datetime.strptime(t[1].time, "%H:%M"))

    @staticmethod
    def filter_tasks(tasks, pet_name=None, completed=None):
        """Filter tasks by pet name or completion status."""
        filtered = tasks
        if pet_name:
            filtered = [t for t in filtered if t[0] == pet_name]
        if completed is not None:
            filtered = [t for t in filtered if t[1].completed == completed]
        return filtered

    @staticmethod
    def detect_conflicts(tasks):
        """Return list of conflicting task pairs."""
        seen = {}
        conflicts = []

        for pet_name, task in tasks:
            if task.time in seen:
                conflicts.append((seen[task.time], (pet_name, task)))
            else:
                seen[task.time] = (pet_name, task)

        return conflicts

    @staticmethod
    def handle_recurrence(pet: Pet):
        """Add next occurrences for completed recurring tasks."""
        new_tasks = []
        for task in pet.tasks:
            if task.completed:
                next_task = task.next_occurrence()
                if next_task:
                    new_tasks.append(next_task)
        pet.tasks.extend(new_tasks)
