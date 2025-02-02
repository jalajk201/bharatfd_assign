# FAQ API (Django + DRF)

## Features
- Store FAQs with multilingual support.
- Supports ?lang= query parameter.
- Uses Redis caching.
- Admin panel for easy management.

## Setup
```bash
git clone <repo_url>
cd faq_project
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver