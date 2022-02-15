from django.core.mail import send_mail
from django.conf import settings


def send_feedback(name, subject, email, message):
    content = ''
    content += 'NAME: ' + name + '\n'
    content += 'SUBJECT: ' + subject + '\n'
    content += 'EMAIL: ' + email + '\n'
    content += 'MESSAGE: ' + message + '\n'
    send_mail(
        subject + ' - Feedback from ' + name,
        content,
        None,
        [settings.EMAIL_TARGET],
        fail_silently=False,
    )
