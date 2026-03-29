# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- Briefly describe your initial UML design.
- What classes did you include, and what responsibilities did you assign to each?
My initial design centered on four core classes: **Owner**, **Pet**, **Task**, and **Scheduler**. I wanted a clean separation of responsibilities: Owners manage pets, pets manage tasks, and the Scheduler handles all the “thinking” — sorting, filtering, conflict detection, and recurrence. This structure felt intuitive and aligned well with the real-world relationships the app 

**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.
As I moved from UML to implementation, I made a few adjustments. The biggest shift was simplifying the Scheduler so it never stores state; instead, it operates purely on data passed into it. Copilot initially suggested embedding scheduling logic inside the Owner class, but that felt like a violation of separation of concerns. I kept the logic centralized and modular, which made testing and UI integration much cleaner.
---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?
To make the scheduler feel genuinely useful rather than just a container for tasks, I implemented four core algorithmic features: sorting, filtering, recurrence, and conflict detection. Each one addressed a specific limitation I noticed during the CLI-first testing phase.

**Sorting** was the first improvement. Without it, tasks appeared in the order they were added, which felt arbitrary and unhelpful. Implementing a time-based sort using `datetime.strptime` immediately made the schedule feel more like a real agenda.

**Filtering** came next. As soon as I added multiple pets and several tasks, it became clear that I needed a way to view tasks by pet or by completion status. The filtering method is intentionally simple—just a couple of list comprehensions—but it adds a lot of usability.

**Recurring tasks** were the most interesting feature to design. I wanted the system to feel “alive,” meaning that completing a daily or weekly task should automatically generate the next occurrence. I kept the recurrence logic lightweight by reusing the same time and description, which works well for predictable routines like feeding or walks.

Finally, **conflict detection** helps surface potential scheduling issues. The algorithm checks for tasks that share the same time and returns pairs of conflicts. It’s not a full calendar engine, but it’s enough to warn the user when two pets need attention simultaneously.

Together, these features transform PawPal+ from a static list manager into a small but capable scheduling assistant.
**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?
One tradeoff I made in the scheduling logic was keeping conflict detection intentionally simple. The system only checks for exact time matches, not overlapping durations or multi-step tasks. This keeps the algorithm lightweight and easy to understand, but it means the scheduler won’t catch more complex conflicts. For the scope of this project, clarity and maintainability felt more important than implementing a full calendar-style overlap engine.
---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
