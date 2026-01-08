# 🐍 Python Mini-Projects Collection

> A curated collection of practical utilities, classic mini-games, and fundamental algorithms implemented in Python.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Active-success)
![License](https://img.shields.io/badge/License-MIT-green)
![Level](https://img.shields.io/badge/Level-Beginner%20Friendly-orange)

## 📖 Introduction

Welcome to my Python code playground! 
This repository documents my journey in learning Python, featuring a variety of scripts ranging from command-line tools to interactive games.

Each project focuses on specific programming concepts, including **File I/O**, **Algorithm Logic**, **Object-Oriented Programming (OOP)**, and **Data Processing**. Whether you are a fellow learner or looking for simple script references, feel free to explore!

---

## 📂 Project List

### 🛠️ Utilities

| File Name | Description | Key Highlights |
| :--- | :--- | :--- |
| **`todo_list.py`** | **CLI Task Manager** | Implements full **CRUD** (Create, Read, Update, Delete) logic with task completion tracking. |
| **`password_generator.py`** | **Secure Password Generator** | Supports custom lengths and includes a **Strength Detection Algorithm** (Weak/Medium/Strong). |
| **`simple_calculator.py`** | **Simple Calculator** | Based on `eval`, supporting basic arithmetic plus complex operations like powers and square roots. |

### 🎮 Games

| File Name | Description | Key Highlights |
| :--- | :--- | :--- |
| **`number_guessing_game.py`** | **Number Guessing Game** | Features **3 Difficulty Levels** (Easy/Medium/Hard) and an intelligent hint system. |
| **`rock_paper_scissors.py`** | **Rock, Paper, Scissors** | A classic game featuring a **Live Scoreboard** to track wins, losses, and draws. |

### 🧠 Algorithms & OOP

| File Name | Description | Key Highlights |
| :--- | :--- | :--- |
| **`student_manager.py`** | **Student Info System** | **OOP Practice**: Defines a `Student` class to simulate behaviors like introducing oneself and taking exams. |
| **`quick_sort.py`** | **Quick Sort Algorithm** | A classic implementation of the efficient sorting algorithm using **Recursion**. |

### 🎨 Visuals

* **`rose_flower.html`**: A frontend HTML file that renders a digital rose in the browser.

---

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone [https://github.com/YourUsername/Your-Repository-Name.git](https://github.com/YourUsername/Your-Repository-Name.git)
cd Your-Repository-Name

```

### 2. Run a Script

Ensure you have Python 3.x installed. Run any script using the terminal:

```bash
# Run the Number Guessing Game
python number_guessing_game.py

# Run the Password Generator
python password_generator.py

```

---

## 💡 Code Snippets

### Object-Oriented Programming (OOP)

From `student_manager.py`:

```python
class Student:
    def __init__(self, name, age, major, university, grade):
        self.name = name
        self.university = university
    
    def introduce(self):
        # Simulates a student introduction
        return f"Hello, I am {self.name} from {self.university}..."

```

### Recursive Algorithm

From `quick_sort.py`:

```python
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    # Recursive calls to sort sub-arrays
    return quicksort(left) + [pivot] + quicksort(right)

```

---

## 🤝 Contributing

Contributions are welcome! If you have ideas for improvements or find any bugs, feel free to open an **Issue** or submit a **Pull Request**.

Let's learn and grow together! 🌱

## 📄 License

This project is licensed under the MIT License.
