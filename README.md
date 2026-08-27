# QR Hunt

A simple Flask boilerplate for building apps that load and display JSON data.

## Project Structure

```
qr_hunt/
├── app.py                 # Main Flask entry point
├── config.py              # App configuration
├── requirements.txt       # Python dependencies
├── .env.example           # Example environment variables
├── data/
│   └── items.json         # Example JSON data file
├── templates/
│   ├── base.html          # Shared layout
│   ├── index.html         # Home / items list page
│   ├── item.html          # Single item detail page
│   └── error.html         # Error page
├── static/
│   ├── css/
│   │   └── style.css      # Basic styles
│   └── js/
│       └── app.js         # Basic JavaScript
└── utils/
    ├── __init__.py        # Package exports
    └── json_loader.py     # Helper for loading JSON files
```

## Setup

1. Create a virtual environment:

```bash
python3 -m venv venv
```

2. Activate the virtual environment:

```bash
# Linux / macOS
source venv/bin/activate

# Windows
venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. (Optional) Create a `.env` file from the example:

```bash
cp .env.example .env
```

## Run the App

```bash
python app.py
```

Then open your browser and go to:

```text
http://127.0.0.1:5000
```

## Available Routes

- `/` - Home page showing all items from `data/items.json`
- `/items` - Alias view of all items
- `/items/<id>` - Detail page for a single item

## How It Works

- The app reads data from `data/items.json` using `utils/json_loader.py`.
- Routes display the full list of items and individual item details.
- Missing or invalid JSON files are handled gracefully with error messages and safe defaults.

## Extending the App

- Add more JSON files in the `data/` folder.
- Update `utils/json_loader.py` if you need custom parsing logic.
- Add new routes in `app.py` and templates in `templates/`.