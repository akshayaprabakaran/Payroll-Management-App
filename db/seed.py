import dotenv

# Load environment variables for development before imports
# so the session file uses these environment variables
dotenv.load_dotenv(".env.development")

from datetime import datetime

from connect import session, engine
from models import Company, Employee, Base

# reset the database
Base.metadata.drop_all(engine)
print("db is reset!")

# create all the tables
Base.metadata.create_all(engine)

companies = [{"name": "Muggles Inc."}, {"name": "Hogwarts"}]

company_1_employees = [
    {
        "name": "Frank Bryce",
        "payroll_schedule": "bi-weekly",
        "start_date": datetime.today(),
        "is_admin": True,
        "company_id": 1,
    },
    {
        "name": "Tobias Snape",
        "payroll_schedule": "monthly",
        "start_date": datetime.today(),
        "is_admin": False,
        "company_id": 1,
    },
    {
        "name": "Vernon Dursley",
        "payroll_schedule": "bi-weekly",
        "start_date": datetime.today(),
        "is_admin": False,
        "company_id": 1,
    },
]

company_2_employees = [
    {
        "name": "Dumbledore",
        "payroll_schedule": "bi-monthly",
        "start_date": datetime.today(),
        "is_admin": True,
        "company_id": 2,
    },
    {
        "name": "Harry",
        "payroll_schedule": "bi-monthly",
        "start_date": datetime.today(),
        "is_admin": False,
        "company_id": 2,
    },
    {
        "name": "Ron",
        "payroll_schedule": "bi-monthly",
        "start_date": datetime.today(),
        "is_admin": False,
        "company_id": 2,
    },
]

for company in companies:
    session.add(Company(**company))

for employee in company_1_employees:
    session.add(Employee(**employee))

for employee in company_2_employees:
    session.add(Employee(**employee))

session.commit()
print("db is seeded!")
