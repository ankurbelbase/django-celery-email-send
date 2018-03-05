from django.template import Context
from django.template.loader import get_template, render_to_string

from django.core.mail import send_mail

def send_feedback_email():
	subject = "I am an HTML email"
	to = ['me.ankur49@gmail.com', 'sumz.stha01@gmail.com']
	from_email = 'email_address'

	ctx = {
        'user': 'ankur',
        'purchase': 'vehicle',
    }

	message = render_to_string('core/email/email.txt', ctx)
	send_mail(subject, message, from_email, to)