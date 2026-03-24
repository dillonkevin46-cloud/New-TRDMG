Markdown

# Tradecore Management System (TRDMG)

An enterprise-grade Ticketing, Notification, and KPI Performance Management Platform built for Tradecore. This system acts as a centralized hub for staff to manage their daily workflows and for management to track performance, handle SLA ticketing, and generate automated performance reports.

## 🚀 Key Features

### 📋 Ticketing & Workflow Management (Todo App)
* **Smart Dashboards:** Dedicated views for Daily, Weekly, and Monthly tasks filtered by the user's role.
* **Interactive Kanban Board:** A Monday.com-style visual board with drag-and-drop functionality (powered by SortableJS and seamless AJAX backend updates).
* **Advanced Global Search:** Filter tasks instantly by keyword, description, or status across all views.
* **Ticket Lifecycles:** Full ticket detail views, commenting system, and file attachment support for robust issue tracking. Time-tracking automatically pauses and resumes based on status changes (e.g., Reopened tickets).
* **Private Daily Notes:** A personal, secure scratchpad for every user with instant AJAX checklist toggles.

### 📊 Performance Tracking (KPI App)
* **Staff Daily Pulse:** A streamlined bulk-evaluation form allowing managers to rate all active objectives for a staff member in seconds. 
* **Automated PDF Reporting:** Generate beautifully styled, downloadable PDF performance reports complete with metric charts using `WeasyPrint`.
* **Custom Date Ranges:** Filter KPI generation to specific weeks, months, or quarters for precise performance reviews.

### 🔔 Global Infrastructure
* **Role-Based Access Control (RBAC):** Distinct permissions and views for 'Staff' and 'Management' users.
* **Real-time Notifications:** Global notification bell alerting managers to ticket updates and status changes.
* **Modern UI/UX:** Clean, responsive, minimalist interface built entirely with Tailwind CSS and custom company branding.

---

## 🛠️ Technology Stack

* **Backend:** Python 3.14+, Django 5.1+
* **Database:** PostgreSQL (`psycopg2`)
* **Frontend:** HTML5, Tailwind CSS (via CDN), vanilla JavaScript (ES6)
* **Libraries:** `Sortable.js` (Drag & Drop), `WeasyPrint` & `pydyf` (PDF Generation)
* **Production Deployment:** Waitress (Windows WSGI Server), WhiteNoise (Static File Management)

---

## 💻 Local Development Setup

### Prerequisites
* Python 3.14 or higher
* PostgreSQL installed and running locally
* A PostgreSQL database named `TRDMG_DB`

### Installation Steps

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd TRDMG_V1.0
Create and activate a virtual environment:

Bash

python -m venv .venv
# On Windows:
.\.venv\Scripts\Activate
# On macOS/Linux:
source .venv/bin/activate
Install dependencies:

Bash

pip install -r requirements.txt
Configure your Database (settings.py):
Ensure your local PostgreSQL credentials (username/password) match the configuration in tradecore/settings.py.

Run Migrations:
Build the database tables.

Bash

python manage.py migrate
Create an Admin Account:
Use our custom management command to safely generate the initial Superuser/Management account.

Bash

python manage.py setup_admin
Run the Development Server:

Bash

python manage.py runserver
Access the app at http://127.0.0.1:8000

🌍 Production Deployment (Windows Server)
This application is configured for production deployment on a Windows environment using Waitress and WhiteNoise.

Configure Production Settings:
Ensure tradecore/settings.py has DEBUG = False and ALLOWED_HOSTS = ['*'] (or your specific server IP).

Collect Static Files:
Gather all CSS, JS, and images into the production folder.

Bash

python manage.py collectstatic --clear
Start the Waitress Server:
Run the application on port 3000.

Bash

waitress-serve --port=3000 tradecore.wsgi:application
⚙️ Automating Server Startup (Windows)
To ensure the server starts automatically when the host machine reboots:

A batch script (start_server.bat) is located in the root directory.

Open Windows Task Scheduler.

Create a task to run the batch script At startup.

Ensure it is set to "Run whether user is logged on or not" and "Run with highest privileges".

Set the "Start in" directory to the absolute path of the project folder.

📁 Project Structure
tradecore/ - Core Django settings, routing, and WSGI/ASGI configurations.

accounts/ - Custom User models, Authentication, and Role management.

todo/ - Ticketing system, Kanban boards, Private notes, and attachments.

kpi/ - Objectives, Evaluations, Daily Pulse forms, and PDF Report generation.

templates/ - Global HTML templates and UI components.

static/ - Custom images, branding, and local static assets.

Built by the Tradecore Internal Development Team.