import dotenv

# load environment variables for testing before running code
dotenv.load_dotenv(".env.test")

from datetime import datetime

import pytest

from db.connect import session
from db.models import Employee, Company


@pytest.fixture(autouse=True)
def cleanup():
    session.query(Employee).delete()
    session.query(Company).delete()


@pytest.fixture()
def company():
    company = Company(id=1, name="Name")
    session.add(company)
    session.commit()
    return company


@pytest.fixture()
def monthly_employees(company):
    harry = Employee(
        name="Harry",
        payroll_schedule="monthly",
        start_date=datetime(2022, 1, 1),
        is_admin=False,
        company_id=company.id,
    )
    hermione = Employee(
        name="Hermione",
        payroll_schedule="monthly",
        start_date=datetime(2022, 1, 1),
        is_admin=True,
        company_id=company.id,
    )
    session.add(harry)
    session.add(hermione)
    session.commit()
    return [harry, hermione]


@pytest.fixture()
def bi_weekly_employees(company):
    harry = Employee(
        name="Harry",
        payroll_schedule="bi-weekly",
        start_date=datetime(2023, 1, 3),
        is_admin=False,
        company_id=company.id,
    )
    hermione = Employee(
        name="Hermione",
        payroll_schedule="bi-weekly",
        start_date=datetime(2023, 1, 3),
        is_admin=True,
        company_id=company.id,
    )
    session.add(harry)
    session.add(hermione)
    session.commit()
    return [harry, hermione]


@pytest.fixture()
def bi_monthly_employees(company):
    harry = Employee(
        name="Harry",
        payroll_schedule="bi-monthly",
        start_date=datetime(2022, 1, 1),
        is_admin=False,
        company_id=company.id,
    )
    hermione = Employee(
        name="Hermione",
        payroll_schedule="bi-monthly",
        start_date=datetime(2022, 1, 1),
        is_admin=True,
        company_id=company.id,
    )
    session.add(harry)
    session.add(hermione)
    session.commit()
    return [harry, hermione]
