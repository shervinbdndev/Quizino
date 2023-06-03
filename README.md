# یک وب اپلیکیشن برای آزمون دادن دانشجو ها

## ویژگی ها :
<br>

- سیستم ورود و خروج و ایجاد حساب کاربری دانشجو توسط ادمین
<br>
<img src='https://github.com/shervinbdndev/Quizino/blob/master/images/1st.png'>

# نکته
- ایجاد کردن حساب کاربری فقط توسط ادمین و فقط در این آدرس قابل ایجاد است
## 127.0.0.1:3000/account/register
- پس یادتون باشه که قبل از ایجاد کردن حساب کاربری دانشجو در پنل ادمین لاگین کنید و بعد وارد آدرس بالایی بشید
<img src='https://github.com/shervinbdndev/Quizino/blob/master/images/1st5.png'>
<br>

- تایمر و تعیین درجه سختی سوالات و صفحه سوالات
<br>
<img src='https://github.com/shervinbdndev/Quizino/blob/master/images/2nd.png'>
<br>

- صفحه نتایج
<br>
<img src='https://github.com/shervinbdndev/Quizino/blob/master/images/3rd.png'>
<br>

- (با کمک جاوا اسکریپت) قوانین امتحان
<br>
<img src='https://github.com/shervinbdndev/Quizino/blob/master/images/4th.png'>
<br>

- API بک اند توسعه داده شده با 
- منتهی یه مقدار مشکل داره ولی درحال درست شدنه
<br>
<img src='https://github.com/shervinbdndev/Quizino/blob/master/images/5th.png'>
<br>

## Jazzmin پنل ادمین با تم

- دارای بخش پنل ادمین برای طرح سوالات و مدیریت و آپدیت کردن سوالات و تعیین درجه سختی آنها
<br>
<img src='https://github.com/shervinbdndev/Quizino/blob/master/images/6th.png'>
<br>

- قابلیت دیدن نتایج آزمون های دانش آموزان/ دانشجویان توسط ادمین
<br>
<img src='https://github.com/shervinbdndev/Quizino/blob/master/images/7th.png'>
<br>

<br>


# کارایی که باید انجام بشه
- ارسال نتیجه امتحان توسط ایمیل که هنوز کامل نشده و فکر نکنم کاملش کنم
- تعیین کردن تاریخ برای ورود به امتحان که دانشجو قبل و بعدش نتونه دوباره ورود کنه
- اضافه کردن کتگوری درس ها  که هر درس برای خودش سوالات خودش رو داشته باشه
- دکمه ای جهت خروج از حساب کاربری محض رضای خدا
- انتخاب کردن سوالات و نمایش آنها در لیست هر آزمون برای هر دانشجو بصورت رندوم که تقلب موقوف

# آدرس ها
آدرس ها  |   شرح آدرس ها
------------- | ------------- 
127.0.0.1:3000/  |  صفحه شروع آزمون که نیازمند ورود به حساب کاربری میباشد
127.0.0.1:3000/admin  |  صفحه ورود به پنل ادمین
127.0.0.1:3000/account/login | صفحه ورود به حساب کاربری که توسط همه قابل دسترس میباشد
127.0.0.1:3000/account/register | صفحه ایجاد حساب کاربری برای دانشجو که فقط توسط ادمین قابل دسترسی است
127.0.0.1:3000/account/logout | برای خروج از حساب کاربری به این آدرس بروید
127.0.0.1:3000/result | صفحه دیدن نتایج که فقط توسط کاربرانی که وارد اکانت خود شده اند قابل دسترس است و هر دانش آموز/دانشجو میتواند نتیجه آزمون خود را ببیند


# کامند های مورد نیاز
شرح کامند ها  |   کامند ها
------------- | ------------- 
برای ایجاد کردن ادمین جدید  |   py manage.py createsuperuser
برای ثبت تغییرات جدید مدل های دیتابیس  |   py manage.py makemigrations
برای اعمال تغییرات جدید مدل های دیتابیس  |   py manage.py migrate
برای اعمال تغییرات جدید مدل های دیتابیس بعلاوه سینک کردن دیتابیس  |   py manage.py migrate --run-syncdb

## پیش نیازها
- <a href='https://www.python.org/'>Python 3.11.3</a>
- <a href='https://www.djangoproject.com/'>Django (v4.2.1)</a>
- <a href='https://www.django-rest-framework.org/'>DRF (Django Rest Framework)</a>
- <a href='https://drf-spectacular.readthedocs.io/en/latest/'>drf-spectacular</a>