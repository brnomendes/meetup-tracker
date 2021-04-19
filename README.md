# Meetup Tracker

Meetup Tracker is a project for tracking [meetup.com](meetup.com) groups and their events. The requested data from the [meetup.com](meetup.com) API is saved in a local database, and only synchronized with [meetup.com](meetup.com) again when requested by the user.

# Development

The project is separated into `backend` and `frontend`. The backend made in `Python + Django` you can find in the `meetup` path, and the frontend made in `Typescript + Angular` you can find in the `frontend` path.

A preview of the application can be seen at https://brnomendes-meetup.herokuapp.com/

## Guide for Pull Requests authors and reviewers:

This repository strongly suggests that you read and use the [Code Reviewer’s Guide](https://google.github.io/eng-practices/review/reviewer/) and [Change Author’s Guide](https://google.github.io/eng-practices/review/developer/) maintained by Google.
For more information you can check [Google Engineering Practices Documentation](https://google.github.io/eng-practices/).

# Backend

This section contains details on the development of the backend, all commands must be executed in the `meetup` path. By default, in development the backend uses `SQLite` as a database.

## Create a Python Virtual Environment and Install the Dependencies

Install `virtualenv`, create and active the `venv` environment:

```
$ pip install virtualenv
$ virtualenv venv

$ source venv/bin/activate # Activate on Mac OS / Linux
$ venv\Scripts\activate    # Activate on Windows
```

After the virtual environment is activated, install the dependencies:

```
$ pip install -r requirements.txt
```

## Create and Apply Migrations

If you made any modifications in the models, you must create the migrations running:

```
$ python manage.py makemigrations
```

To apply the existing migrations, run:

```
$ python manage.py migrate
```

## Create an Admin User

After applying the migrations for the first time, you must create an admin user to access the django site admin. To do this, run:

```
$ python manage.py createsuperuser
```

## Raise Server in Development Mode

To run the backend in development mode, run:

```
$ python manage.py runserver
```

After the backend is running you can access `localhost:8000/admin` to access the django site admin.

## Run Tests

This project uses `pytest` as a testing tool for the backend, to execute it:

```console
$ pytest
```

## Run Check Tools

This project follows pre-defined standards, so for you to make a contribution you must check that your code is in accordance with the standards, for this run the following tools (in the future it must be replaced by a single command using pre-commit):

```console
$ black meetup tracker
$ isort meetup tracker
```

# Frontend

This section contains details on the development of the frontend, all commands must be executed in the `frontend` path.

## Install the Dependencies

After you have installed npm, install the dependencies:

```
$ npm i
```

## Raise Server in Development Mode

To run the frontend in development mode, run:

```
$ npm serve
```

After the frontend is running you can access `localhost:4200` to access the application.

## Run Tests

This project uses `Karma + Jasmine` as a testing tool for the frontend, to execute it:

```console
$ npm test
```

# License

Meetup Tracker was developed by Bruno Mendes (2021) and is under the [MIT License](https://github.com/brnomendes/meetup-tracker/blob/master/LICENSE).
