from django.core.mail import EmailMessage
from weasyprint import HTML

from django.http.response import HttpResponse
from celery import shared_task


@shared_task
def sendler_email(subject, body, from_email, to_email, html_template=None, pdf_data=None):
    email = EmailMessage(subject=subject, body=body, to=to_email,
                         from_email=from_email)
    if pdf_data:
        fileobj = HttpResponse()
        HTML(string=pdf_data).write_pdf(fileobj)
        email.attach('order.pdf', fileobj.content, 'application/pdf')
    email.send()