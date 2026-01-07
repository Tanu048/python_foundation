# 📚 Student Management System (CLI)

A command-line based Student Management System built using **Python**.  
This project focuses on **core programming fundamentals** such as nested data structures, file handling, and modular logic — without using databases or frameworks.

---

## 🧠 Overview

This application allows users to manage student records through a **menu-driven CLI interface**.  
It supports adding, viewing, updating, and deleting student data while ensuring **data persistence across program runs**.

The project was built to strengthen understanding of how real applications manage **in-memory data vs stored data**.

---

## 🚀 Features

- Menu-driven Command Line Interface
- Nested dictionary-based data storage
- File-based data persistence
- CRUD operations (Create, Read, Update, Delete)
- Input validation and type safety
- Modular and reusable functions

---

## 🛠️ Tech Stack

- Python
- Command Line Interface (CLI)
- File I/O
- Nested Dictionaries

---

## 💻 How to Run

Clone the repository:
```bash
git clone <your-repo-link>
cd <your-folder-name>


Run the program

```bash
python main.py
```

📂 Project Structure

```
student-management-system/
│
├── student_log.txt     # Persistent storage
├── main.py             # Core logic
└── README.md           # Documentation
```
---

## 🧠 Logic Highlights

* Data Persistence Strategy
  The program loads student data from a file into a dictionary at startup and writes it back to the file before exit, mirroring real-world application state management.

* Why Nested Dictionaries
  Enables structured access to student attributes and makes the system easily extensible for future features like marks, attendance, or grades.

* Separation of Concerns
  File handling and in-memory operations are handled by separate functions (`load_data()` and `save_data()`), ensuring cleaner logic and easier debugging.

* Type Safety
  Values are explicitly converted while loading from file to prevent logical and runtime errors.

---

## 📈 Future Improvements

* Add marks, grades, and attendance tracking
* Search and filter functionality
* Export data to CSV/JSON
* GUI or Web-based version
* Database integration (SQLite/MySQL)

---


 The project was built to strengthen understanding of how real applications manage in-memory data vs stored data.
 Built while learning Python fundamentals and logical problem solving.