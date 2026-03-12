# Simple clicker

This is a small auto-clicker controlled with keyboard shortcuts.

## Install with uv

If you do not already have `uv`, install it first:

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

From the `clicker_games` folder, create the environment and install dependencies:

```powershell
uv sync
```

## Run with uv

From the `clicker_games` folder, run:

```powershell
uv run python clicker.py
```

## Controls

- Press `Num Lock` to start clicking.
- Move the mouse to stop clicking automatically.
- Press `Num Lock` again to stop the clicker manually.
- Press `Esc` to quit the program.
