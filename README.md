# Gesunde Impulse

A Django-based personal development app that uses **Tasks**, **Skills**, and **Attributes** to visualize your growth with a dynamic **Radar Chart**.

This README includes:

* Project overview
* Features
* Technology stack
* Installation guide (with a full **step-by-step Ubuntu setup**)
* Usage instructions

---

## 🚀 Project Overview

**Gesunde Impulse** helps you track and improve personal growth through a gamified system of tasks, skill progression, and attribute development. Completing tasks increases the associated skills and attributes, and updates a radar chart visualization in real time.

---

## 🧰 Features

### ✅ Task System

* Add tasks via the admin panel
* Each task contributes to a specific **Skill**
* Completing tasks automatically updates the skill and attribute levels

### 📊 Radar Chart Visualization

* Inner ring: **Skill Levels**
* Outer ring: **Attribute Levels**
* Automatically re-renders when tasks are completed

### 🧠 Admin Customization

* Configure relationships between **Tasks → Skills → Attributes**
* Set increment values for precise control
* Edit skill/attribute details in real time

---

## 🛠️ Technologies Used

* **Python 3.10+**
* **Django 5.x**
* **Matplotlib** (radar chart generation)
* **HTML5 / CSS3**
* **SQLite3** (default database)

---

## 🖥️ Step-by-Step Installation Guide (Ubuntu)

Below is a complete setup guide for Ubuntu 20.04 / 22.04 / 24.04.

---

## 1️⃣ Update Packages

```bash
sudo apt update && sudo apt upgrade -y
```

---

## 2️⃣ Install Required System Dependencies

Matplotlib needs several low-level packages:

```bash
sudo apt install -y \
  python3 python3-venv python3-pip python3-dev build-essential \
  libfreetype6-dev libpng-dev pkg-config libjpeg-dev zlib1g-dev tk-dev
```

---

## 3️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/gesunde_impulse.git
cd gesunde_impulse
```

---

## 4️⃣ Create & Activate a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

Upgrade pip:

```bash
pip install --upgrade pip
```

---

## 5️⃣ Install Python Dependencies

If you have a `requirements.txt`, use it:

```bash
pip install -r requirements.txt
```

Otherwise install manually:

```bash
pip install django matplotlib
```

> **Important for servers:** Matplotlib must use a headless backend.
> Add this before any pyplot imports:

```python
import matplotlib
matplotlib.use('Agg')
```

---

## 6️⃣ Run Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## 7️⃣ Create a Superuser

```bash
python manage.py createsuperuser
```

Follow the prompts.

---

## 8️⃣ Collect Static Files (optional)

```bash
python manage.py collectstatic --noinput
```

---

## 9️⃣ Run the Development Server

Local development:

```bash
python manage.py runserver
```

Access on LAN:

```bash
python manage.py runserver 0.0.0.0:8000
```

Visit:

* App → [http://localhost:8000/](http://localhost:8000/)
* Admin → [http://localhost:8000/admin/](http://localhost:8000/admin/)

---

## 🔧 (Optional) Allow External Access

If UFW firewall is active:

```bash
sudo ufw allow 8000/tcp
```

---

## 🧠 How It Works

### Admin Panel (/admin)

1. Add **Attributes** (e.g., Strength, Focus)
2. Add **Skills** linked to attributes (e.g., Weightlifting, Study Habits)
3. Add **Tasks** linked to skills (e.g., "Read 20 pages", "Gym Session")
4. Set increment values for each

### User App

* Open `/tasks/` → See task list
* Click task → Marks completed and updates stats
* Open `/` → See updated radar chart

---

## 🎮 Optional Ideas for Expansion

* XP / Level system
* Badges and achievements
* Streak tracking
* User accounts and profiles

---

## 📄 License

Add your license here (MIT recommended).

---

If you want, I can also create a:

* **Dockerfile**
* **docker-compose.yml**
* **nginx + gunicorn production setup**
* **requirements.txt**

Just let me know!
