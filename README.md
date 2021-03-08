# django-postman

django based command line postman

## usage

$ python manage.py runscript enviar --script-args arg1 arg2 arg3

where:
arg1 = html template filename
arg2 = recipient CSV filename
arg3 = subject

## example

python manage.py runscript enviar --script-args template_massive.html recipients.csv "Prueba"

. Enviar mail con estilo e imágen
. Hacer uso de variables en el template

A continuación, te indicamos los pasos para que actives tu cuenta institucional.

1. Ingresa a www.gmail.com
2. Haz login utilizando tu correo electrónico XXXXX, siendo tu password temporal el RUT (sin puntos, ni guion y sin dígito verificador)

Cuando ingreses por primera vez, se te pedirá actualizar la contraseña
