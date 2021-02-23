from django.core.mail import EmailMessage
from django.template import Context
from django.template.loader import render_to_string, get_template
from django.core.mail import EmailMessage
from django.conf import settings
from email.mime.image import MIMEImage
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
    with open(path_recipients, encoding='utf-8', newline='') as f:
        reader = csv.reader(f)
        recipients = list(reader)

    image_filename='logo_uaysen_01.jpg'

    json_context = {
        'user': 'alumn@',
        'image_filename': image_filename
    }
    path_html_template = os.path.join(settings.BASE_DIR, path_template)
    message = get_template(path_html_template).render(json_context)

    email = EmailMessage(
        mail_title,
        message,
        'no-responder@uaysen.cl',
        ['gitlab@uaysen.cl'],
        [recipient[0] for recipient in recipients],
        reply_to=['no-responder@uaysen.cl'],
    )
    with open(os.path.join(settings.BASE_DIR, 'static/'+image_filename), mode='rb') as f:
        image = MIMEImage(f.read())
        email.attach(image)
        image.add_header('Content-ID', f"<{image_filename}>")
    
    email.content_subtype = "html"
    email.send()
    