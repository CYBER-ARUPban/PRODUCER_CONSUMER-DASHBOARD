[readme.md](https://github.com/user-attachments/files/24249876/readme.md)
# Producer–Consumer Simulation (C + Python + Web UI)

This project demonstrates the **Producer–Consumer problem** using a **C-based circular buffer**, exposed through a **Python Flask API**, and visualized via a **web frontend (HTML/JS)**.

It is designed for **Operating Systems / Networking / System Programming** practicals to show how low-level C logic can be safely accessed from higher-level applications.

---

## 🔧 Project Architecture

```
Frontend (index.html)
        │
        ▼
Flask REST API (api.py)
        │  (ctypes)
        ▼
C Shared Library (pc.c → pc.so)
```

- **C** handles the actual producer–consumer logic using a circular buffer
- **Python (Flask)** exposes the logic via REST APIs
- **HTML/JS** interacts with the API and displays buffer state

---

## 📁 Project Files

| File | Description |
|----|----|
| `pc.c` | C implementation of Producer–Consumer using a circular buffer |
| `pc.so` | Compiled shared library from `pc.c` |
| `api.py` | Flask API that calls C functions using `ctypes` |
| `index.html` | Frontend UI to produce/consume items |
| `requirements.txt` | Python dependencies |

---

## ⚙️ Buffer Details

- Buffer Type: Circular Queue
- Buffer Size: **5**
- Empty Slot Value: `-1`
- Items Produced: Random integers (10–99)

---

## 🧪 API Endpoints

### `GET /status`
Returns current buffer state

```json
{
  "buffer": [23, 45, -1, -1, -1],
  "capacity": 5,
  "count": 2
}
```

---

### `POST /produce`
Produces a random item

**Success:**
```json
{
  "status": "success",
  "produced": 56,
  "buffer": [23, 45, 56, -1, -1]
}
```

**Failure (Buffer Full):**
```json
{
  "error": "Buffer is FULL"
}
```

---

### `GET /consume`
Consumes one item from the buffer

**Success:**
```json
{
  "status": "success",
  "consumed": 23,
  "buffer": [-1, 45, 56, -1, -1]
}
```

**Failure (Buffer Empty):**
```json
{
  "error": "Buffer is EMPTY"
}
```

---

## 🚀 How to Run the Project

### 1️⃣ Compile the C Code

```bash
gcc -shared -o pc.so -fPIC pc.c
```

> Ensure `pc.so` is in the same directory as `api.py`

---

### 2️⃣ Install Python Dependencies

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Start the Flask Server

```bash
python api.py
```

Server will run at:
```
http://localhost:5000
```

---

### 4️⃣ Open the Frontend

Open `index.html` in your browser.

---

## 🔐 CORS Support

CORS is enabled in Flask to allow browser-based API calls:

```python
from flask_cors import CORS
CORS(app)
```

---

## 🎯 Learning Outcomes

- Understand Producer–Consumer problem
- Circular buffer implementation in C
- Creating shared libraries (`.so`)
- Calling C code from Python using `ctypes`
- Building REST APIs with Flask
- Frontend–Backend integration

---

## 📚 Suitable For

- OS Lab / System Programming Lab
- Computer Networks Lab
- Mini-project demonstration
- Practical exams & viva

---

## 🧑‍💻 Author

**Arup Banerjee**

---

## ✅ License

This project is for **educational use only**.

