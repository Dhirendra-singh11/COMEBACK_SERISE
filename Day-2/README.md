# Day 1: Restarting My IT Journey

## What I did today

Today I started rebuilding my foundation in Python and software development by creating a small study-planner project.

### Project goal
Build a simple program that helps a learner plan study time based on:
- total weekly study hours
- number of days available per week
- average study time per day

### What I built
I created a Python script named `app.py` with functions to:
- validate weekly study hours
- validate the number of study days
- calculate average study hours per day
- run the planner in a CLI program

I also wrote `test_app.py` to test the core logic using `unittest`.

### Main learning points
- Python function design
- input validation with `if` conditions
- raising custom `ValueError` exceptions
- writing and running unit tests
- basic command-line interaction with `input()` and `print()`
- organizing a small project with separate files

### Example logic
The planner calculates:

```python
avg_hours_per_day = weekly_hours / study_days
```

and validates that:
- weekly hours are not less than 1
- weekly hours do not exceed 168
- study days are between 1 and 7

### Files created
- `app.py` — main program
- `test_app.py` — unit tests
- `README.md` — daily summary

### Commands used
```bash
python3 app.py
python3 -m unittest -v test_app.py
```

### Reflection
This was a good start because it helped me restart my programming habit without trying to do too much. I focused on core skills instead of jumping into advanced AI or backend projects too early.

### Next step for tomorrow
- improve the planner with better error messages
- learn more about Python functions and testing
- build a second small project with a bit more complexity

### Progress status
- [x] Python basics started
- [x] Project created
- [x] Unit tests added
- [x] GitHub repo/folder organized
- [ ] Next project planning

---

This is my Day 1 note and a small restart in my learning journey.
