from django.core.mail import EmailMessage
from django.template import Context
from django.template.loader import render_to_string, get_template
from django.core.mail import EmailMessage
from django.conf import settings
from smtplib import SMTPException
from email.mime.image import MIMEImage
import logging
import os
import csv

def run(*args):
    if len(args) != 3 :
        print('''
    Modo de uso de este script:

    $ python manage.py runscript enviar --script-args arg1 arg2 arg3

    donde:
    arg1 = Nombre del archivo de la plantilla. Debe estar en el directorio raíz. Ejemeplo: template.html
    arg2 = Nombre de CSV con los destinatarios. Cada fila del archivo debe tener <email>,<nombre del destinatario>
    arg3 = Título del correo

    JGED.-
        ''')
        return

    path_template = args[0]
    path_recipients = args[1]
    mail_title = args[2]

    recipients = []
    with open(path_recipients, encoding='iso-8859-1', newline='') as f:
        reader = csv.reader(f)
        recipients = list(reader)

    image_filename='logo_uaysen_01.jpg'
    es_header = True
    for recipient in recipients :
        if es_header :
            es_header = False
            continue
        alumno = recipient[4]
        alumno_mail_personal = recipient[6]
        json_context = {
            'nombre_alumno' : alumno.title(),
            'email_institucional' : recipient[5],
            'image_filename': image_filename
        }
        path_html_template = os.path.join(settings.BASE_DIR, path_template)
        message = get_template(path_html_template).render(json_context)

        print(alumno, end=",")
        print(alumno_mail_personal, end=",")
        print(recipient[5])
        
        email = EmailMessage(
            mail_title,
            message,
            'no-responder@uaysen.cl',
            [alumno_mail_personal],
            ['jose.espina@uaysen.cl'],
            reply_to=['no-responder@uaysen.cl'],
        )
        with open(os.path.join(settings.BASE_DIR, 'static/'+image_filename), mode='rb') as f:
            image = MIMEImage(f.read())
            email.attach(image)
            image.add_header('Content-ID', f"<{image_filename}>")
        email.content_subtype = "html"

        try:
            email.send()
        except SMTPException as e:
            logging.error('This is an error message', e)
        
    return
    