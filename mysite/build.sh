#!/usr/bin/env bash
set -o errexit
pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate

# ساخت خودکار ادمین (اگر از قبل وجود نداشته باشد)
python manage.py shell -c 
"from django.contrib.auth 
import get_user_model; User = get_user_model();
User.objects.filter(username='salman').exists() or
User.objects.create_superuser('salman',
'salmanalaviasl@gmail.com', '666790Sn')"