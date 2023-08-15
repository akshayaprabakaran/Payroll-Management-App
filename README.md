## Language & Tools

- Python v3.x
- [Pip](https://pip.pypa.io/en/stable/getting-started/) - as a package installer for Python
- [Flask-SQLAlchemy](https://www.sqlalchemy.org/) and [SQLite](https://www.sqlite.org/) for the database
- [Pytest](https://docs.pytest.org/en/7.2.x/)

Before continuing to the next steps, you'll need Python v3.x and pip installed on your computer.

### Project Setup

The following instructions are used to run and use the application. These instructions are written for a Mac/Linux/WSL (Windows Subsystem for Linux) environment. If you are running on Windows and not using WSL, you might need to modify the commands slightly to remove and run the correct files.

```bash
# install requirements
# we recommend using a virtualenv to avoid conflicts with other environments
$ pip install -r requirements.txt

# refresh seed data to make data relevant to today 
$ python db/seed.py

# Run example scenario
$ python assessment.py

# Run tests:
$ python -m pytest -s

# Run the linter to clean up your code
$ python -m black .
```

# About the Project

This is a python project that mimics aspects of a larger Python back-end.

## Debugging in Python 

You can also append a filename and method to your pytest command to run
only that test. e.g. `python -m pytest tests/test_process_payroll_notifications_job.py::test_bi_weekly_notification_on_following_thursday -s`. 
When a test fails, pytest gives you this command format for the specific failure at the bottom of its output.
