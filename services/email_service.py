class EmailService:
    @staticmethod
    def send_notification_per_employee(admin, employee):
        # Intentionally blank - this would be the logic that sends off the email
        # Adding a put statement to help you what happens
        print(f"Send email to Admin {admin.name} about Employee {employee.name}")

    @staticmethod
    def send_notification_per_employees(admin, employees):
        employee_names = ", ".join([employee.name for employee in employees])
        print(f"Send email to Admin {admin.name} about Employees {employee_names}")
