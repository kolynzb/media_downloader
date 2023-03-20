# Project Folder Structure

```bash
C:.
├───.vscode
├───docs
└───src
    ├───backend
    │   ├───scripts
    └───gui
        ├───assets
        │   ├───fonts
        │   └───images
        ├───screens
        └───widgets
```

## Folders

- `src`
  - Folder containing all code
- `docs`
  - Folder containing documentation
- `./src/backend`
  - Folder containing backend related code(_scripts, database_)
- `./src/backend/scripts`

  - Folder containing automation scripts(_these handle the logic related to the different types of download_).

- `./src/gui/`
  - Folder contains all the UI/frontend code.
- `./src/gui/widgets/`
  - Folder contains all the UI/frontend components or widgets.
- `./src/gui/screens/`
  - Folder contains all the UI/frontend screens or pages.
- `./src/gui/assets/`
  - Folder contains all static/assests files like images, fonts.
- `.vscode`
  - Folder contains my preferred vscode settings.

## Special files

- `./src/main.py`
  - Entry point of the project.
- `./src/backend/models`
  - Contains logic for configuration for sqlite database.
- `./src/backend/history`
  - Contains logic to do with download history (_saving ,clearing and deleting from database_).
- `src/gui/app`
  - Entry point for the GUI application.(_powered by flet_)
- `./setup.cfg`
  - Flake8 settings or configuration.
- `./requirements.txt`
  - Contains project dependencies or third party packages.
- `./runtime.txt`
  - Contains python version used when creating project.
- `./tut.md`
  - File containing the links and resources used in this project.
- `./downloads.db`
  - This is your sqlite database (_appears after running the project atleast once_)
