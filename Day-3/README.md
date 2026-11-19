# Day 3: JSON Files and Study Progress

## What I worked on

Today I practised working with JSON data in Python, saving and loading data from files, and keeping study progress between program runs. I also continued practising small Python functions and unit tests.

## What I built and practised

- Used Python's `json` module to write data to a JSON file and load it back.
- Used `pathlib.Path` to represent file paths.
- Practised saving and loading study progress, marking a day complete, and calculating a completion percentage.
- Added progress tracking to the study-planner program.
- Practised functions for counting vowels, checking odd numbers, finding the largest number, removing duplicates, and counting character frequency.
- Used `unittest` to test weekly schedule creation and empty-subject validation.

## Project files

- `app.py` — study planner with weekly scheduling and progress tracking
- `progress.py` — JSON progress-file helpers and completion calculations
- `progress.json` — example progress data
- `json_excerise.py` — saving and loading sample contacts as JSON
- `excerise.json` — sample contact data
- `excerise.py` — Python function exercises
- `test_app.py` — unit tests for the planner

## Run the program and tests

From this directory:

```bash
./venv/bin/python app.py
./venv/bin/python -m unittest -v
```

## Concepts practised

- JSON serialization and deserialization with `json.dump()` and `json.load()`
- Reading and writing files with UTF-8 encoding
- `pathlib.Path`
- Lists, dictionaries, loops, and functions
- Basic persistence: keeping data in a file between runs
- Unit testing with `unittest`

## Reflection

Today I learned that Python objects can be stored in JSON files and loaded back for later use. I also started connecting file-based progress tracking to my study planner.

## Next steps

- Handle missing or malformed JSON files consistently.
- Check that loaded JSON has the expected type and structure.
- Add unit tests for saving, loading, and marking progress complete.
