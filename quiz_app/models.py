from django.db import models






class Question(models.Model):
    CHOISES: list = [
        ('option1', 'گزینه اول'),
        ('option2', 'گزینه دوم'),
        ('option3', 'گزینه سوم'),
        ('option4', 'گزینه چهارم'),
    ]
    
    SCALES: list = [
        (1, 'آسان'),
        (2, 'متوسط'),
        (3, 'سخت'),
    ]
    
    question = models.CharField(max_length=200, unique=True, verbose_name='سوال')
    option1 = models.CharField(max_length=50, verbose_name='گزینه اول')
    option2 = models.CharField(max_length=50, verbose_name='گزینه دوم')
    option3 = models.CharField(max_length=50, verbose_name='گزینه سوم')
    option4 = models.CharField(max_length=50, verbose_name='گزینه چهارم')
    answer = models.CharField(max_length=10, choices=CHOISES, verbose_name='پاسخ', help_text='گزینه درست را انتخاب کنید')
    scale = models.IntegerField(choices=SCALES ,null=True, verbose_name='سطح سختی سوال')
    status = models.BooleanField(default=False, help_text='وضعیت انتشار سوال', verbose_name='وضعیت')

    def __str__(self):
        super(Question, self).__str__()
        return self.question

    class Meta:
        verbose_name = 'سوال'
        verbose_name_plural = 'سوالات'







class UserResult(models.Model):
    fullname = models.CharField(max_length=20, verbose_name='نام و نام خانوادگی')
    totall = models.PositiveSmallIntegerField(default=0, verbose_name='کل سوالات')
    score = models.PositiveSmallIntegerField(default=0, verbose_name='امتیاز')
    percent = models.FloatField(max_length=5, verbose_name='درصد')
    correct = models.PositiveSmallIntegerField(default=0, verbose_name='تعداد سوالات درست')
    wrong = models.PositiveSmallIntegerField(default=0, verbose_name='تعداد سوالات غلط')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد ')

    def __str__(self):
        super(UserResult, self).__str__()
        return self.fullname

    class Meta:
        verbose_name = 'نتیجه'
        verbose_name_plural = 'نتایج'
