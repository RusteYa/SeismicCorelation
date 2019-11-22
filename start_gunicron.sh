APPNAME=SeismicCorelation
APPDIR=/home/ubuntu/$APPNAME/

gunicorn $APPNAME.wsgi:application &
