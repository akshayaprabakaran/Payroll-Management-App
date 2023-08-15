from unittest.mock import call

from freezegun import freeze_time

from jobs.process_payroll_notifications_job import ProcessPayrollNotificationsJob


@freeze_time("2023-01-01")
def test_monthly_notifications_first_of_month(mocker, monthly_employees):
    send_notifications = mocker.patch(
        "services.email_service.EmailService.send_notification_per_employees"
    )
    ProcessPayrollNotificationsJob.perform()
    send_notifications.assert_has_calls(
        [call(monthly_employees[1], [monthly_employees[0], monthly_employees[1]])]
    )


@freeze_time("2023-01-02")
def test_monthly_notifications_not_on_first_day_of_month(mocker, monthly_employees):
    send_notification = mocker.patch(
        "services.email_service.EmailService.send_notification_per_employees"
    )
    ProcessPayrollNotificationsJob.perform()
    send_notification.assert_not_called()


@freeze_time("2023-01-12")
def test_bi_weekly_notification_on_following_thursday(mocker, bi_weekly_employees):
    send_notification = mocker.patch(
        "services.email_service.EmailService.send_notification_per_employees"
    )
    ProcessPayrollNotificationsJob.perform()
    send_notification.assert_has_calls(
        [call(bi_weekly_employees[1], [bi_weekly_employees[0], bi_weekly_employees[1]])]
    )


@freeze_time("2023-01-13")
def test_bi_weekly_notifications_not_on_thursday(mocker, bi_weekly_employees):
    send_notification = mocker.patch(
        "services.email_service.EmailService.send_notification_per_employees"
    )
    ProcessPayrollNotificationsJob.perform()
    send_notification.assert_not_called()


@freeze_time("2023-01-15")
def test_bi_monthly_notifications_middle_of_month(mocker, bi_monthly_employees):
    send_notification = mocker.patch(
        "services.email_service.EmailService.send_notification_per_employees"
    )
    ProcessPayrollNotificationsJob.perform()
    send_notification.assert_has_calls(
        [
            call(
                bi_monthly_employees[1],
                [bi_monthly_employees[0], bi_monthly_employees[1]],
            )
        ]
    )


@freeze_time("2023-01-31")
def test_bi_monthly_notifications_end_of_month(mocker, bi_monthly_employees):
    send_notification = mocker.patch(
        "services.email_service.EmailService.send_notification_per_employees"
    )
    ProcessPayrollNotificationsJob.perform()
    send_notification.assert_has_calls(
        [
            call(
                bi_monthly_employees[1],
                [bi_monthly_employees[0], bi_monthly_employees[1]],
            )
        ]
    )


@freeze_time("2023-01-01")
def test_bi_monthly_notifications_first_day_of_month(mocker, bi_monthly_employees):
    send_notification = mocker.patch(
        "services.email_service.EmailService.send_notification_per_employees"
    )
    ProcessPayrollNotificationsJob.perform()
    send_notification.assert_not_called()
