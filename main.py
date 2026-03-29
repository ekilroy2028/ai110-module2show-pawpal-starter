from pawpal_system import Owner, Pet, Task, Scheduler


def main():
    owner = Owner("Elizabeth")

    # Create pets
    bella = Pet("Bella", "Dog")
    milo = Pet("Milo", "Cat")

    owner.add_pet(bella)
    owner.add_pet(milo)

    # Add tasks with different times
    bella.add_task(Task("Morning Walk", "08:00", "daily"))
    bella.add_task(Task("Breakfast", "07:30"))
    milo.add_task(Task("Vet Appointment", "09:15"))

    # Use Scheduler to get today's schedule
    schedule = Scheduler.get_todays_schedule(owner)

    print("\n🐾 TODAY'S SCHEDULE\n")
    for pet_name, task in schedule:
        print(f"{task.time} — {pet_name}: {task.description} ({'done' if task.completed else 'pending'})")


if __name__ == "__main__":
    main()
