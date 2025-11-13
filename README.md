# Gesunde Impulse Web Application

## 🌱 Overview
This Django-based web application was developed as a **warm-up project** for **Gesunde Impulse**.  
The concept demonstrates how a person can develop **skills** and **attributes** through **completing tasks**, visualized dynamically using a radar chart.

---

## 💡 Concept
- A **person has tasks** – completing them increases skills.  
- A **person has skills** – skills influence and level up attributes.  
- A **person has attributes** – these represent personal growth areas such as strength, endurance, intelligence, creativity, etc.

This web app helps visualize growth and learning through everyday actions.

---

## Features
**Task List**  
- Displays all available tasks as clickable items.  
- Each task can be marked as **completed**.  

**Dynamic Progress System**  
- Completing a task increases the **related skill**.  
- Each skill contributes to its corresponding **attribute**.  
- Relationships and level increments are **fully configurable** via the Django Admin interface.

**Radar Chart Visualization**  
- Shows an interactive chart of **skills and attributes**.  
- Automatically updates as tasks are completed.  

 **User-Configurable Relationships**  
- Each task → skill → attribute link and level increment can be customized in the admin panel.  

---

## 🏗️ Project Structure

gesunde_impulse/
├── manage.py
├── db.sqlite3
├── gesunde_impulse/
│ ├── settings.py
│ ├── urls.py
│ ├── wsgi.py
│ └── asgi.py
└── main/
├── admin.py
├── apps.py
├── models.py
├── urls.py
├── views.py
├── Templates/
│ ├── home.html
│ └── task_list.html
├── static/
│ └── main/
│ └── style.css
└── migrations/

yaml
Copy code

---

## ⚙️ Installation & Setup

### 1️⃣ Clone or Download
```bash
git clone https://github.com/your-username/gesunde_impulse.git
cd gesunde_impulse
2️⃣ Create Virtual Environment
bash
Copy code
python -m venv venv
source venv/bin/activate      # on macOS/Linux
venv\Scripts\activate         # on Windows
3️⃣ Install Dependencies
bash
Copy code
pip install django matplotlib
4️⃣ Run Migrations
bash
Copy code
python manage.py makemigrations
python manage.py migrate
5️⃣ Create Superuser (for admin access)
bash
Copy code
python manage.py createsuperuser
6️⃣ Run the Development Server
bash
Copy code
python manage.py runserver
🧠 How It Works
Go to the Admin Panel (/admin)

Add Attributes, Skills, and Tasks

Configure their relationships and increment values

Open /tasks/ to view the Task List

Click on tasks to mark them complete

Open / (home) to view the Radar Chart update dynamically

🧰 Technologies Used
Python 3.10+

Django 5.x

Matplotlib (for radar chart visualization)

HTML5, CSS3

SQLite3 (default database)

🎨 UI Overview
🗒️ Task List
Displays all tasks:

✅ Completed tasks show a checkmark.

⏳ Incomplete tasks can be clicked to mark as completed.

📈 Radar Chart
Displays:

Skill levels (inner ring)

Attribute levels (outer ring)

Automatically updates on task completion.

🧑‍💻 Code Highlights
models.py
Defines three main entities:

Task → connected to Skill

Skill → connected to Attribute

Both contain increment fields for configurability.

views.py
Handles:

Task completion logic

Dynamic skill and attribute updates

Rendering of radar chart and task list

admin.py
Allows easy configuration of:

Relationships

Level increments

Real-time editing of skill and information of tasks

Add gamification (XP, badges, levels)

🧑‍💼
