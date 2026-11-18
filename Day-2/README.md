# Day 2: Building a Weekly Study Planner

## What I worked on

Today I extended my Python study planner so it can schedule subjects across the days I plan to study. I also practised splitting comma-separated text into a list.

## What the planner does

- Accepts weekly study hours and the number of study days.
- Accepts subject names and assigns them to the selected days.
- Rotates through the subjects when there are more study days than subjects.
- Rejects an invalid number of study days or an empty subject list.

## Python concepts practised

- Lists and dictionaries
- `str.split()` and `str.strip()`
- List comprehensions
- Loops and the modulo operator (`%`) for rotating through subjects
- Raising and testing `ValueError`
- Unit tests with Python's `unittest` module

## Project files

- `app.py` — study planner and weekly subject scheduling
- `test_app.py` — tests for weekly schedule creation and empty-subject validation
- `excerise.py` — practice splitting and trimming comma-separated subject names

## Run the program and tests

From this directory:

```bash
./venv/bin/python app.py
./venv/bin/python -m unittest -v
```

## Reflection

Today I practised turning user input into useful Python data structures and using a dictionary to represent a weekly schedule. I also continued learning how tests can check expected behavior and invalid input.

## Next steps

- Validate the subject count and reject blank subject names.
- Improve input handling so invalid entries do not unexpectedly stop the program.
- Add tests for invalid study days and schedules with more days than subjects.
