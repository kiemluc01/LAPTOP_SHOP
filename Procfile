release: pip install GDAL==3.2.0
python manage.py collectstatic
web: gunicorn LAPTOP_SHOP.wsgi --log-file -