# Tiny Python Toys

Seven small command-line programs for learning Python. Python 3.10+ is recommended;
runtime dependencies are limited to the standard library.

## Run

```bash
git clone https://github.com/AlvanHarriSon/Tiny-Python-Toys.git
cd Tiny-Python-Toys
python Tiny-Python-Toys/number_guessing_game.py.py
python Tiny-Python-Toys/password_generator.py.py
python Tiny-Python-Toys/simple_calculator.py.py
```

The existing `.py.py` filenames are retained for compatibility. Each program can
also be loaded without launching its interactive prompt.

| Script in `Tiny-Python-Toys/` | Behavior |
| --- | --- |
| `number_guessing_game.py.py` | Three difficulty levels and number hints |
| `rock_paper_scissors.py.py` | Rock-paper-scissors with a session scoreboard |
| `password_generator.py.py` | Cryptographic randomness; optional digits and symbols |
| `simple_calculator.py.py` | Bounded arithmetic, parentheses, powers, `sqrt(x)` and `math.sqrt(x)` |
| `todo_list.py.py` | Add, remove and complete tasks in memory |
| `quick_sort.py.py` | Recursive quicksort demonstration |
| `student_manager.py.py` | Student class demonstration |

The calculator accepts numbers and arithmetic, not arbitrary Python code.
Expressions are limited to 1,000 characters, 100 AST nodes, exponent magnitude
1,000, and finite real results with magnitude at most 1e100. Password length must
be an integer of at least four. Strength ratings are a simple teaching heuristic.
Tasks and game scores are not persisted after exit.

## Test

```bash
python -m unittest discover -s tests -v
python -m pip install -r requirements-dev.txt
python -m ruff check . --select E9,F63,F7,F82
```

Tests cover import safety, arithmetic and rejection of executable input, password
options, sorting, task completion, and game scoring. See `QUALITY_REVIEW.md`
for the engineering review and validation limits. Licensed under MIT.
