from datetime import datetime, timedelta

# -----------------------------
# Task Class (Updated for Priority)
# -----------------------------
@dataclass
class Task:
    description: str
    time: str
    frequency: str = "once"
    completed: bool = False
    priority: str = "Medium"  # NEW FIELD: High, Medium, Low


# -----------------------------
# Scheduler (Add Priority Sorting)
# -----------------------------
class Scheduler:
    @staticmethod
    def sort_by_priority_then_time(tasks):
        """Sort tasks by priority first, then by time."""
        priority_order = {"High": 0, "Medium": 1, "Low": 2}

        from datetime import datetime
        fmt = "%H:%M"

        return sorted(
            tasks,
            key=lambda t: (
                priority_order.get(t[1].priority, 1),
                datetime.strptime(t[1].time, fmt),
            ),
        )

    # keep your other Scheduler methods below this



class Pet:
    """Represents a pet with its own task list."""

    def __init__(self, name: str, species: str):
        self.name = name
        self.species = species
        self.tasks = []

    def add_task(self, task: Task):
        """Add a task to the pet."""
        self.tasks.append(task)

    def get_tasks(self):
        """Return all tasks for this pet."""
        return self.tasks

    def __repr__(self):
        return f"{self.name} ({self.species})"


class Owner:
    """Represents an owner who manages multiple pets."""

    def __init__(self, name: str):
        self.name = name
        self.pets = []

    def add_pet(self, pet: Pet):
        """Add a pet to the owner."""
        self.pets.append(pet)

    def get_all_tasks(self):
        """Return all tasks across all pets as (pet_name, task)."""
        all_tasks = []
        for pet in self.pets:
            for task in pet.get_tasks():
                all_tasks.append((pet.name, task))
        return all_tasks

    def __repr__(self):
        return f"Owner({self.name})"


class Scheduler:
    """Handles scheduling logic like sorting, filtering, conflicts, and recurrence."""

    def sort_by_time(self, tasks):
        """Return tasks sorted by time."""
        return sorted(
            tasks,
            key=lambda item: datetime.strptime(item[1].time, "%H:%M")
        )

    def filter_tasks(self, tasks, pet_name=None, completed=None):
        """Filter tasks by pet name and/or completion status."""
        filtered = tasks

        if pet_name is not None:
            filtered = [t for t in filtered if t[0] == pet_name]

        if completed is not None:
            filtered = [t for t in filtered if t[1].completed == completed]

        return filtered

    def detect_conflicts(self, tasks):
        """Detect tasks scheduled at the same time."""
        conflicts = []
        seen_times = {}

        for pet_name, task in tasks:
            if task.time in seen_times:
                conflicts.append((seen_times[task.time], (pet_name, task)))
            else:
                seen_times[task.time] = (pet_name, task)

        return conflicts

    def handle_recurrence(self, pet: Pet):
        """Create new tasks for completed recurring tasks."""
        new_tasks = []

        for task in pet.tasks:
            if task.completed:
                next_task = task.next_occurrence()
                if next_task:
                    new_tasks.append(next_task)

        pet.tasks.extend(new_tasks)
