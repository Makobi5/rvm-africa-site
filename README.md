# Ronnie and Vero Ministries Africa (RVM Africa) 🌍✨

> **Transforming Lives Through Christlikeness, Education, and Sustainable Empowerment.**

[![Python](https://img.shields.io/badge/Python-3.12+-blue.svg)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-5.0+-green.svg)](https://www.djangoproject.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## 📖 About the Project
**Ronnie and Vero Ministries Africa** is a holistic mission based in Uganda, founded by **Rev. Ronnie and Veronica Baraza**. This platform serves as the digital heart of their mission—connecting spiritual outreach with tangible community development.

The ministry operates across three primary pillars:
1.  **Spiritual Growth:** Church crusades, leadership training, and discipleship.
2.  **Social Welfare:** Supporting vulnerable and orphaned children with tuition, medical care, and meals.
3.  **Economic Empowerment:** Sustainable projects including **Poultry Farming**, **Fish Farming**, and vocational skills like **Tailoring** and **Music**.

---

## 🚀 Key Features
- **Dynamic CMS:** Fully managed via Django Admin to update ministries, farming projects, and events in real-time.
- **Impact-Driven UI:** A professional, responsive interface inspired by global ministry standards (**Sky Blue & Navy Blue** theme).
- **Interactive UX:** Custom CSS3 animations including **scroll-synchronized zoom effects** for founder profiles and project cards.
- **Project Showcase:** Dedicated modules for agricultural projects to build donor trust and community engagement.
- **Event Management:** Integrated system for tracking Worship Nights, Seminars, and Medical Missions.

---

## 🛠️ Tech Stack
- **Backend:** Python 3.12+ / Django Framework
- **Frontend:** Bootstrap 5, Custom CSS3, FontAwesome
- **Image Processing:** Pillow (for high-res ministry and event posters)
- **Environment Management:** Python-Dotenv (Secured SECRET_KEY and Database credentials)
- **Database:** SQLite (Development) / PostgreSQL (Production)

---

## ⚙️ Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/rvm-africa-site.git
cd rvm-africa-site

2. Setup Virtual Environment
python -m venv venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

3. Install Dependencies
pip install -r requirements.txt

4. Environment Configuration
Create a .env file in the root directory:

SECRET_KEY=your_django_secret_key
DEBUG=True
5. Database Migrations & Superuser

python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

6. Run Server

python manage.py runserver
Visit http://127.0.0.1:8000/ to see the site live!
📁 Project Structure
code
Text
rvm_africa_site/
├── core/               # Main application logic
│   ├── models.py       # Ministry, Event, and Category schemas
│   ├── views.py        # Dynamic content rendering
│   └── templates/      # HTML5/Django templates
├── static/             # Global CSS, Images (Founders), and JS
├── media/              # User-uploaded content (Project photos)
├── rvm_project/        # Root settings and URL routing
└── manage.py           # Django CLI
🤝 Support & Contribution
This project is part of a mission to empower communities in Africa. If you'd like to contribute to the code or support the ministry's physical projects (Farming/Orphanages), please contact the team.
Developed with ❤️ for Ronnie and Vero Ministries Africa.