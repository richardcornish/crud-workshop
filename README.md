# CRUD workshop

## Pre-requisites

- [Python](https://www.python.org)
- [SQLite](https://www.sqlite.org/)
- [Git](https://git-scm.com/)

## Installation

1. Clone the repository.

```
git clone
```

2. Create and activate the virtual environment.

```
cd crud-workshop/
python -m venv venv --upgrade-deps
source venv/bin/activate
```

3. Install the requirements.

```
pip install -r requirements.txt
```

4. Migrate the database

```
python manage.py migrate
```

5. Run the local server.

```
python manage.py runserver
```
Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/).
