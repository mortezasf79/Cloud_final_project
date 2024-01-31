# مرحله یک - نصب وابستگی‌ها
FROM python:3.9-alpine AS build

# نصب وابستگی‌های بنیانی
RUN apk add --no-cache build-base

# کپی کردن فایل‌های مورد نیاز
COPY requirements.txt .

# نصب وابستگی‌ها
RUN pip install --no-cache-dir -r requirements.txt --user

# مرحله دو - اجرای برنامه
FROM python:3.9-alpine

# نصب وابستگی‌های بنیانی
RUN apk add --no-cache libstdc++

# کپی کردن فایل‌های مورد نیاز
COPY --from=build /root/.local /root/.local
COPY . /app

# تنظیم مسیر کاری به پوشه /app
WORKDIR /app

# تنظیم متغیر PATH
ENV PATH=/root/.local/bin:$PATH

# تنظیمات پیش‌فرض برای Flask
ENV FLASK_APP=base_api.py
ENV FLASK_RUN_HOST=0.0.0.0

# اجرای برنامه
CMD ["flask", "run"]