# Simple Recipe & Cooking App — Project Report

## 1. Cover Page

**Project:** Simple Recipe & Cooking App  
**Student Name:** ____________________  
**Registration Number:** ____________________  
**Course:** ____________________  
**Faculty:** ____________________  
**Academic Year:** 2026–27

---

## 2. Introduction

Cooking is an everyday activity, but beginner cooks often need a simple way to find ingredients and cooking instructions. This project creates a small Python desktop application that provides recipes in an easy-to-read format.

The project is designed as a first-year, first-semester programming project and focuses on basic Python concepts.

## 3. Problem Statement

Beginner cooks may have difficulty finding simple recipes and remembering all the required ingredients and steps. The proposed application keeps a small collection of recipes in one place and allows users to search for them.

## 4. Objectives

- Learn how to use Python dictionaries and lists.
- Create a simple graphical user interface.
- Implement searching.
- Display structured recipe information.
- Use file handling to save favourite recipes.
- Practice modular programming.
- Write simple tests.

## 5. Functional Requirements

### FR1 — Recipe Selection
The user can select a recipe from the list.

### FR2 — Recipe Search
The user can search by recipe name or ingredient.

### FR3 — Recipe Details
The application displays cooking time, difficulty, ingredients and steps.

### FR4 — Favourites
The user can save a recipe to a favourites file.

### FR5 — Favourite Viewing
The user can view saved favourite recipes.

### FR6 — Error Handling
The application informs the user when a search has no results or no recipe has been selected.

## 6. Non-Functional Requirements

### Usability
The interface is simple and readable.

### Performance
The application uses a small local recipe collection, so searches are fast.

### Reliability
The application checks whether a recipe exists before saving it.

### Maintainability
The program is divided into separate Python files.

### Portability
The application uses Python and Tkinter without external frameworks.

## 7. System Architecture

The application uses a simple modular architecture:

User → Tkinter GUI → Recipe/Search modules → Favourites text file.

## 8. Design Diagrams

Architecture, workflow, use-case, sequence and module diagrams are included in `docs/diagrams.md`.

## 9. Design Decisions & Rationale

### Why Python?
Python is easy for beginners to learn and provides simple data structures and GUI support.

### Why Tkinter?
Tkinter is available with Python and allows a desktop GUI to be built without an external GUI framework.

### Why dictionaries?
Dictionaries make it easy to associate each recipe name with its ingredients, cooking time, difficulty and steps.

### Why a text file?
A text file is enough for a small project and demonstrates basic file handling without adding unnecessary database complexity.

## 10. Implementation Details

The main modules are:

- `main.py` — starts the application.
- `recipes.py` — stores recipe data.
- `search.py` — searches recipe names and ingredients.
- `favourites.py` — saves and reads favourite recipes.
- `validation.py` — performs simple checks.
- `ui.py` — creates the GUI.
- `test_project.py` — contains unit tests.

## 11. Screenshots / Results

Add screenshots of:

1. Main application.
2. Recipe list.
3. Search result.
4. Recipe ingredients and cooking steps.
5. Favourite recipes.
6. Successful test output.

## 12. Testing Approach

Python's `unittest` module is used.

The tests check:

- recipes are available;
- valid recipes are recognized;
- invalid recipes are rejected;
- searching by recipe name works;
- searching by ingredient works;
- search text is cleaned correctly.

Run:

```bash
python -m unittest discover -s tests -v
```

## 13. Challenges Faced

- Organizing recipe information in dictionaries.
- Displaying multiple pieces of recipe information in the GUI.
- Implementing search by both name and ingredient.
- Saving favourites using file handling.
- Organizing code into separate modules.

## 14. Learnings & Key Takeaways

The project helped demonstrate:

- Python dictionaries
- Python lists
- Functions
- Conditional statements
- Loops
- String handling
- File handling
- GUI programming
- Basic testing
- Modular programming

## 15. Future Enhancements

- Add recipe images.
- Add more recipes.
- Add vegetarian/non-vegetarian categories.
- Add cooking timers.
- Add ingredient quantity adjustment.
- Add nutritional information.
- Add a database for a larger recipe collection.

## 16. References

1. VITyarthi — Build Your Own Project guidelines.
2. Python documentation.
3. Tkinter documentation.
