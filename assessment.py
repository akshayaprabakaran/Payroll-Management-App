import dotenv

# Load environment variables for development before imports
# so the payroll job uses these environment variables
dotenv.load_dotenv(".env.development")

from jobs.process_payroll_notifications_job import ProcessPayrollNotificationsJob

if __name__ == "__main__":
    ProcessPayrollNotificationsJob.perform()
