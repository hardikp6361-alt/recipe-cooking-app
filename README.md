# Simple Recipe & Cooking App

A beginner-friendly first-year Python project that helps users find simple recipes, view ingredients and cooking steps, and save favourite recipes.

## Main Features

1. Choose a recipe from a list.
2. Search recipes by name or ingredient.
3. View ingredients and cooking instructions.
4. Add recipes to favourites.
5. View saved favourites.
6. Handle invalid searches with a simple message.

## Example Recipes

- Vegetable Fried Rice
- Paneer Butter Masala
- Masala Pasta
- Aloo Paratha
- Vegetable Sandwich
- Lemon Rice
- Tomato Pasta
- Veggie Maggi

## Technologies

- Python
- Tkinter
- Basic lists and dictionaries
- Functions
- File handling
- Simple searching

No external Python packages are required.

## How to Run

Install Python 3.10 or newer.

Open this project folder in VS Code and run:

```bash
python main.py
```

## Testing

Run:

```bash
python -m unittest discover -s tests -v
```

## Project Structure

```text
Simple_Recipe_Cooking_App/
│
├── main.py
├── requirements.txt
├── README.md
├── statement.md
│
├── cooking_app/
│   ├── __init__.py
│   ├── recipes.py
│   ├── search.py
│   ├── favourites.py
│   ├── validation.py
│   └── ui.py
│
├── tests/
│   └── test_project.py
│
└── docs/
    ├── diagrams.md
    └── project_report.md
```

## How It Works

The recipes are stored in a Python dictionary. The user selects or searches for a recipe. The program then displays its ingredients and cooking steps.

Favourites are stored in a simple text file called `favourites.txt`.

This is an educational beginner project, not a professional recipe database.
