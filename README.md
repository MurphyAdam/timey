# Timey multi-user, multi-project time tracking and project management.

This is a simple multi-user, multi-project time tracking and project management with written in Django, DRF.
Interactions through API.

## Requirments

This project is written in `Python 3.9` using `django 3.2.8` and `django-rest-framework 3.12.4`
with a SQLITE file database.

## Install

Please create a virtual environment and install the project requirements found in the file `requirements.txt`.

## Run

For the sake of testing, the database has been populated by two user accounts, one admin, one non-admin.

Test credintials:

- account type: Admin
    email: timey@test.com
    password: @timey1234

- account type: Regular user (non-admin/ staff previliges)

    email: user1@test.com
    password: @user1234

## Tests

Tests have been written for each of the apps: accounts, projects, tracker.
To run the tests, please run `python manage.py test`

