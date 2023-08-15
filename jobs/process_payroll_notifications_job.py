from db.models import Employee
from db.connect import session
from services.email_service import EmailService
import datetime


class PayrollNotificationProcessor:
    def __init__(self, employee):
        self.employee = employee
        self.today = datetime.date.today()
        self.days_diff = (self.today - self.employee.start_date).days
        self.week_number = (self.days_diff // 7) + 1
        self.is_even_week = self.week_number % 2 == 0
        self.next_month_number = (self.today.month % 12) + 1
        self.first_day_of_next_month = self.today.replace(
            day=1, month=self.next_month_number
        )
        self.last_day_of_month = self.first_day_of_next_month - datetime.timedelta(
            days=1
        )
        self.is_last_day_of_month = self.today == self.last_day_of_month

    def is_payday(self):
        if (
            (self.employee.payroll_schedule == "bi-weekly")
            and (self.today.weekday() == 3)
            and self.is_even_week
        ):
            return True
        elif (self.employee.payroll_schedule == "bi-monthly") and (
            self.today.day == 15 or self.is_last_day_of_month
        ):
            return True
        elif (self.employee.payroll_schedule == "monthly") and (self.today.day == 1):
            return True
        return False

    def send_notifications(self, payday_employees):
        all_admins = (
            session.query(Employee)
            .filter_by(company_id=self.employee.company_id, is_admin=True)
            .all()
        )

        for admin in all_admins:
            EmailService.send_notification_per_employees(admin, payday_employees)


class ProcessPayrollNotificationsJob:
    @staticmethod
    def perform():
        employees = session.query(Employee).all()
        payday_employees = []

        for employee in employees:
            if employee.end_date is None or employee.end_date > datetime.date.today():
                processor = PayrollNotificationProcessor(employee)
                if processor.is_payday():
                    payday_employees.append(employee)

        if payday_employees:
            processor.send_notifications(payday_employees)
