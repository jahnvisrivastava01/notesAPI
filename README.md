# 📝 Notes API

> A simple yet powerful REST API for creating, managing, and organizing notes, built with FastAPI and SQLite.

---

## ✨ Features

* ➕ Create notes
* 📋 View all notes
* 🔍 Retrieve a note by ID
* ✏️ Update existing notes
* 🗑️ Delete notes

---

## 🛠️ Tech Stack

* 🐍 Python
* ⚡ FastAPI
* 🗄️ SQLite
* 🔗 SQLAlchemy

---

## 📂 Project Structure

```text
notes-api-fastapi/
│
├── main.py
├── database.py
├── models.py
├── schemas.py
├── .gitignore
└── README.md
```

---

## 🚀 Getting Started

### Clone the Repository

```bash
git clone <repository-url>
cd notes-api-fastapi
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

**Windows**

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install fastapi uvicorn sqlalchemy
```

### Run the Server

```bash
uvicorn main:app --reload
```

Server running at:

```text
http://127.0.0.1:8000
```

Interactive API Docs:

```text
http://127.0.0.1:8000/docs
```

---

## 📡 API Endpoints

| Method | Endpoint      | Description    |
| ------ | ------------- | -------------- |
| GET    | `/`           | Home Route     |
| POST   | `/notes`      | Create a Note  |
| GET    | `/notes`      | Get All Notes  |
| GET    | `/notes/{id}` | Get Note by ID |
| PUT    | `/notes/{id}` | Update a Note  |
| DELETE | `/notes/{id}` | Delete a Note  |

---

## 🎯 What I Learned

* REST APIs
* CRUD Operations
* FastAPI Fundamentals
* SQLAlchemy ORM
* SQLite Database Integration
* API Testing using Thunder Client

---

## 🌱 Future Improvements

* ✅ Error Handling
* ✅ Dependency Injection
* ✅ Search Notes
* ✅ MySQL Support
* ✅ Authentication with JWT
* ✅ Docker Deployment

---

## Author
**Jahnvi Srivastava**
