# 📝 To-Do File Manager (CLI)

A command-line based To-Do File Manager built using Python.  
This project focuses on core programming fundamentals such as file handling, string manipulation, and modular logic — without using databases or external frameworks.

---

## 🧠 Overview

This application allows users to manage daily tasks through a menu-driven CLI interface.  
It supports adding tasks, viewing the task list, marking tasks as completed, and deleting tasks while ensuring data persistence using a text file.

The project was built to strengthen understanding of how simple file-based systems can manage real-world data.

---

## 🚀 Features

- Menu-driven Command Line Interface  
- Add new tasks to a file  
- View all saved tasks  
- Mark tasks as completed  
- Delete tasks from the list  
- File-based data persistence  
- Case-insensitive task matching  

---

## 🛠️ Tech Stack

- Python  
- Command Line Interface (CLI)  
- File I/O  
- String manipulation  

---

## 💻 How to Run

Clone the repository:

```bash
git clone https://github.com/Tanu048/python_foundation
cd todo_file_manager
```

Run the program:
```bash
Copy code
python todo.py
```
---

## 📂 Project Structure
```
to-do-file-manager/
│
├── task.txt        # Task storage file
└── todo.py         # Core application logic
```
---
## 🧠 Logic Highlights

* File-Based Persistence Strategy
  All tasks are stored in a text file. The program reads from and writes to the file for every operation, ensuring tasks remain saved even after the program exits.

* Task Status Representation
  Tasks are marked as incomplete [ ] or completed [x], simulating real-world task tracking systems.

* Case-Insensitive Matching
  Task completion and deletion logic ignores letter casing, improving usability and reducing input errors.

* Separation of Concerns
  Each task operation (add, list, complete, delete) is handled by a dedicated function, keeping the code modular and readable.

---

## 📈 Future Improvements

* Add task priorities and deadlines
* Prevent duplicate tasks
* Search and filter tasks
* Store tasks in JSON/CSV format
* GUI or Web-based version
* Database integration

---

Built while learning Python fundamentals, file handling, and logical problem solving.

---