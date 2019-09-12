# AI world

> Os: Linux 

> Python: ^3

## Backend: Django 

From `aiworld` folder, run this script below to start `backend` server:

```bash
virtualenv -p python3 venv 
source activation.sh
pip3 install -r requirements.txt
python3 manage.py runserver
```

## Frontend: VueJS

From `aiworld` folder, run this script below to start `frontend` server:

```bash
npm install 
npm run serve
```

## Core: AI model