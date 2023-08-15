from sqlalchemy import Column, Integer, String, Date, Boolean
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Employee(Base):
    __tablename__ = "employees"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    payroll_schedule = Column(String)
    start_date = Column(Date)
    end_date = Column(Date)
    is_admin = Column(Boolean)
    company_id = Column(Integer)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "payroll_schedule": self.payroll_schedule,
            "is_admin": self.is_admin,
        }

    def __eq__(self, other):
        return self.id == other.id

    def __repr__(self):
        return str(self.to_dict())


class Company(Base):
    __tablename__ = "companies"
    id = Column(Integer, primary_key=True)
    name = Column(String)
