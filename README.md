# TheStackOverflowed

A factory game where you automate your factory by editing and repairing code, written in a restricted Python-like language that the game interprets itself.

> Status: early prototype. Target is roughly 100 combined development hours for two developers.

## Core loop

Move, mine, carry, insert resources, run machines, collect outputs, expand.

## Project rules

- Build a small playable prototype before adding lots of content.
- Keep the **game simulation** separate from the **custom interpreter**.
- Agree on interfaces between the two (see `INTERFACE.md`) before implementing them independently.
- Never run player code with `exec()` / `eval()`. `Player.py` and building scripts are simulated scripts, not real Python files.
- The simulation owns the important facts: inventories, elapsed processing time, and whether a building may output an item.
- Every building must obey game rules and pass validation tests.
- Integrate regularly; don't wait until the end to combine both halves.

## Team split

| Area | Owner | Scope |
|---|---|---|
| Game / Factory | Dev A | Window, grid, player movement, mining, inventory, interaction range, building placement, economy, map expansion, UI |
| Language / Buildings | Dev B | Parser, interpreter, `Player.py` execution, building module interface, `Smelter.py`, validation, execution safety |
| Both | | Shared API, integration, tutorial and progression design, playtesting, deciding what to cut |

## Roadmap

- [ ] **Phase 0**: agree on the design (loop, visuals, starting factory, economy, unlocks, first missions, interface, repo and task board)
- [ ] **Phase 1**: minimum game foundation. *Milestone 1:* move around a 5x5 factory, mine, carry one item, insert it into a smelter, activate it through code
- [ ] **Phase 2**: building scripts and validation. *Milestone 2:* edit the smelter's code and have the game validate it
- [ ] **Phase 3**: progression and unlocks. *Milestone 3:* earn resources, buy a language feature or map expansion, use it
- [ ] **Phase 4**: first playable chapter. *Milestone 4:* a new player can repair the smelter and finish a short task sequence
- [ ] **Phase 5**: polish, testing, presentation

Optional after the core prototype: more ores and materials, conveyors, more advanced Python concepts, efficiency stats and leaderboards, more maps and buildings.

## Workflow

- Work on feature branches, open PRs into `main`, and have the other dev review anything touching the interface.
- Track tasks on the shared issue board, one issue per checklist item.
- Integrate at least once per development session or at agreed milestones.
- Keep a list of deliberately postponed features.

## Setup

Everything is pure Python (3.11+ recommended).

- **Game:** `pygame-ce` for window, grid, input and drawing.
- **Interpreter:** built on the standard library `ast` module. Player scripts are parsed with `ast.parse()` and run by our own tree-walker that only accepts whitelisted node types. We never call `exec()`, `eval()` or `compile()` on player code.
- **Tests:** `pytest`.

```
python -m venv .venv
.venv\Scripts\activate        # Windows
source .venv/bin/activate     # macOS / Linux
pip install -r requirements.txt
```

Run instructions will be added once `main.py` exists.

## Project Organisation:

thestackoverflowed/
├── README.md
├── INTERFACE.md
├── requirements.txt
├── .gitignore
├── main.py                  # entry point: starts the game
│
├── game/                    # Dev A: simulation + rendering
│   ├── __init__.py
│   ├── world.py             # grid, map, expansion
│   ├── player.py            # position, inventory, mining
│   ├── buildings.py         # Building base class, Smelter state, slots, timers
│   ├── economy.py           # resources, money, shop/unlocks
│   ├── actions.py           # the approved actions exposed to scripts
│   └── ui/
│       ├── renderer.py      # drawing the map, player, machines
│       ├── hud.py           # inventories, status messages
│       └── editor.py        # in-game code editor
│
├── interpreter/             # Dev B: no pygame imports in here
│   ├── __init__.py
│   ├── parser.py            # ast.parse wrapper + friendly errors
│   ├── evaluator.py         # whitelisted tree-walker
│   ├── features.py          # which syntax is unlocked (the whitelist)
│   ├── limits.py            # instruction counter, loop protection
│   ├── errors.py            # ScriptError types with line numbers
│   └── validation.py        # runs building tests against a script
│
├── scripts/                 # default player-facing scripts (the simulated .py files)
│   ├── Player.py
│   └── Smelter.py
│
├── assets/                  # sprites, sounds, fonts
│
└── tests/
    ├── test_interpreter.py
    ├── test_smelter_rules.py
    └── test_integration.py