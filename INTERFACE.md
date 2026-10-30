# Game <-> Interpreter Interface (DRAFT v0)

Both devs must agree on this before implementing against it. Change it via PR, reviewed by both.

## Principles

- The interpreter never touches game state directly. It can only call approved **game actions** exposed by the simulation.
- The simulation owns inventories, timers, and output permission. Scripts can request; the game decides.
- The interpreter enforces execution limits (max instructions, loop protection) and reports errors as data, not crashes.

## Interpreter -> Game: actions (initial proposal)

| Action | Meaning | Rules enforced by the game |
|---|---|---|
| `move(direction)` | Move the player one tile | Must stay inside the map |
| `mine()` | Start/continue mining the adjacent resource | Timer/progress handled by the game |
| `pick_up()` / `drop()` | Carry items | Respect carrying capacity (starts at 1) |
| `insert(building)` | Put the carried item into a building | Player must be adjacent |
| `building.<function>()` | Call a function exposed by a building script (e.g. `smelter.start()`) | Player must be adjacent; building rules apply |

(Names and signatures are placeholders: finalize in Phase 0.)

## Game -> Interpreter: results

Every action returns a result the script can inspect:

```
{ ok: bool, value: any | null, error: string | null }
```

## Interpreter API (to be implemented by Dev B)

```
parse(source: str) -> Program | SyntaxErrors   # with line/column and readable messages
run(program, api, limits) -> RunResult          # api = the approved actions above
validate(building_script, tests) -> ValidationReport
```

- `limits`: max instructions, max call depth, wall-clock budget.
- `RunResult`: status (`finished` | `error` | `limit_exceeded`), error info, actions requested.

## Building script standard (to be defined)

Every building script exposes a standard set of functions (for example `start()`, `tick()`, input/output slot access). The simulation drives time; the script cannot set the timer or emit an output the simulation hasn't allowed.

## Validation (to decide)

Fixed tests vs hidden tests vs simulation, or a combination. Must not be bypassable by changing a displayed timer only.

## Open questions

- Tick model: does the interpreter run per game tick or as a coroutine that yields on actions?
- How are `import` and cross-script calls (`Player.py` -> `Smelter.py`) resolved?
- Which language features exist at the start vs. unlockable (variables, functions, `time()`, loops, conditions, lists, imports, parameters)?
