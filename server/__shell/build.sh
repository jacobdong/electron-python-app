#pyinstaller --add-data "__static:__static" --target-architecture "universal2" app.py
source ./__venv/bin/activate
pyinstaller --add-data "__static:__static" --distpath ../__dist/server app.py