# Project Folder Structure

```bash
C:.
├───docs
└───src
    ├───backend
    │   ├───scripts
```

## Folders

- `src`
  - Folder containing all code
- `docs`
  - Folder containing documentation
- `src/backend`
  - Folder containing backend related code(_scripts, database_)
- `src/backend/scripts`
  - Folder containing automation scripts(_these handle the logic related to the different types of download_).

## Special files

- `main.py`
  - Entry point of the project
- `src/backend/models`
  - Contains logic for configuration for sqlite database
- `src/backend/history`
  - Contains logic to do with download history (_saving ,clearing and deleting from database_).
- `src/gui`
  - Entry point for the GUI application.(_powered by flet_)
