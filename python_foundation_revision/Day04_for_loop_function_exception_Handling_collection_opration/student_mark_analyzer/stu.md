# Project 2 – Student Marks Analyzer


## Problem Statement

Build a **Student Marks Analyzer** — a menu-driven system (like the ATM/Bank project) that lets a user add, view, analyze, and remove student records across multiple sessions, until they choose to exit.

### Initial Data

* No students exist at the start — data is built up entirely through the menu.
* Subjects are fixed: **Math, Science, English**.
* Passing marks = **40** — applies **both** per subject and on overall percentage (see status rules below).

### Menu

```
========== STUDENT MARKS ANALYZER ==========
1. Add Students Data
2. Show All Results
3. Show Topper
4. Show Pass/Fail List
5. Remove a Student
6. Exit
==============================================
```

---

## Requirements

### 1. Data Structure

* Store all student records in a single dictionary, keyed by **roll number** (not name — names can repeat, roll numbers can't).
* Each value is itself a dictionary holding that student's name, subject marks, total, average, and pass/fail status per subject and overall.

### 2. Add Students Data (Menu Option 1)
* Ask how many students the user wants to add.
  * If the number entered is 0 → ask for confirmation before cancelling the add-student panel.
  * If negative → show an error and ask again.
  * If a valid positive number → loop that many times, collecting one student's full record each time.
* For each student:
  * Ask for a roll number. It must be **unique** — if it already exists, reject it, show the existing record for that roll number, and ask again.
  * Ask for the student's name.
  * Ask for Math, Science, and English marks (accept decimals).
  * If any subject's mark is **≤ 0 or > 100**, that specific subject's mark is set to **0** — each subject is checked and corrected **independently** (an invalid Math mark should not affect whether Science or English get checked).
  * Calculate total, average, and percentage.
  * Determine **subject-wise status** (Pass/Fail, ≥ 40 per subject) for each of the three subjects.
  * Determine **overall status**: Fail if *any* subject is Fail, OR if overall percentage ≤ 40; otherwise Pass.
  * Store everything under that roll number.

### 3. Show All Results (Menu Option 2)
* Print every stored student's full record: roll number, name, each subject's mark with its Pass/Fail status, total, average, and overall status.

### 4. Show Topper (Menu Option 3)
* Find and display the student with the highest **total** marks (roll number, name, total).

### 5. Show Pass/Fail List (Menu Option 4)
* For every student, print their roll number, name, and overall Pass/Fail status.

### 6. Remove a Student (Menu Option 5)
* Ask for a roll number to remove.
* If it doesn't exist, inform the user and let them either try again or return to the main menu (their choice).
* If it exists, confirm the name being deleted, remove the record, and return to the main menu.

### 7. Exit (Menu Option 6)
* Ask for confirmation before actually closing the program.

---

## Cross-Cutting Rules (Apply Throughout)

* Every numeric input (menu choice, count of students, marks) must be wrapped in exception handling — invalid (non-numeric) input should show a clear message and re-prompt, never crash the program.
* Menu choices outside 1–6 should show an appropriate "invalid option" message and return to the menu.
* A reusable confirmation function (returns 0 for No / 1 for Yes, re-prompting on anything else or non-numeric input) should back every "are you sure?" moment (cancelling add, exiting, etc.).

---
