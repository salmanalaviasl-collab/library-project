#!/usr/bin/env bash

# 1. نصب پکیج‌ها
pip install -r requirements.txt

# 2. جمع‌آوری فایل‌های استاتیک (برای درست شدن CSSها)
python manage.py collectstatic --no-input

# 3. اجرای مهاجرت‌های دیتابیس
python manage.py migrate

# 4. ساخت ادمین (با استفاده از متغیرهایی که تو رندر ساختی)
python manage.py createsuperuser --no-input || true