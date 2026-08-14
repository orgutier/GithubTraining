# Hands-on practice suite

Companion exercises for the **Python for Testing & APIs** training deck
(`python-testing-api-presentation.html`). This is graded, runnable practice:
you write real implementations, and a pytest suite tells you whether they're
correct.

## Architecture

```
hands-on/
├── conftest.py            shared fixtures (e.g. base_url)
├── pytest.ini              marker registration + test discovery config
├── requirements.txt
├── exercises/               <- YOU EDIT THESE
│   ├── fundamentals.py      Part 1: variables, control flow, functions, errors
│   ├── oop.py                Part 2: dataclasses, context managers, decorators
│   └── apis.py                Part 5: the requests library
└── tests/                   <- DO NOT EDIT — this is what grades you
    ├── test_fundamentals.py
    ├── test_oop.py
    └── test_apis.py
```

Every function in `exercises/` is a stub: it either raises
`NotImplementedError` or has a `# TODO` comment describing exactly what to
build, mirroring the exercises described on the deck's Practical Exercise
panels. The `tests/` package is the answer key, expressed as pytest tests —
implement each stub until its tests turn green.

Each exercise module maps to one custom pytest **marker**, matching the
deck's parts, so a single topic can be run in isolation instead of the whole
suite at once — useful for an instructor spot-checking one skill, or a
trainee focusing on the part they're behind on:

| Marker         | Deck part                                      | Run it with                |
|-----------------|-------------------------------------------------|------------------------------|
| `fundamentals` | Part 1 — core language fundamentals            | `pytest -m fundamentals -v` |
| `oop`          | Part 2 — dataclasses, context managers, decorators | `pytest -m oop -v`      |
| `apis`         | Part 5 — the requests library                  | `pytest -m apis -v`         |

`tests/test_apis.py` never makes a real network call — it uses the
`responses` library to intercept `requests` calls, exactly as taught in
Part 6 of the deck.

## Getting started

```bash
cd hands-on
pip install -r requirements.txt

pytest -v                          # run everything
pytest -m fundamentals -v          # just Part 1
pytest -m "fundamentals or oop" -v # combine markers
pytest -k test_add -v              # run one test by name
pytest --collect-only -q           # list every test without running it
```

## Workflow

1. Open `exercises/fundamentals.py`. Pick a function, delete its
   `raise NotImplementedError(...)`, and implement it.
2. Run `pytest -m fundamentals -v` and watch tests go from red to green,
   one at a time.
3. Repeat for `exercises/oop.py` (`pytest -m oop -v`) and
   `exercises/apis.py` (`pytest -m apis -v`).
4. Once every marker is green, run the whole suite: `pytest -v`.
5. Optional stretch: run `pytest -v --cov=exercises --cov-report=term-missing`
   (after `pip install pytest-cov`) and see whether your own tests-of-your-
   understanding would have caught anything these tests didn't.

## Why this shape

This mirrors a real-world pattern: implementation code lives separately
from the tests that verify it, and markers let you (or CI) select a slice
of the suite instead of an all-or-nothing run — the same technique covered
on the deck's "pytest in CI" slide (`--maxfail=1`, selective runs, etc.).
