# django-postman

django based command line postman

## usage

$ python manage.py runscript enviar --script-args arg1 arg2 arg3

where:
arg1 = html template filename
arg2 = recipient CSV filename
arg3 = subject

## example

python manage.py runscript enviar --script-args template.html recipients.csv "Prueba 2"
