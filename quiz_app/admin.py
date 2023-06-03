from django.contrib import admin
from .models import (Question, UserResult)
from django.contrib.auth.models import Group


class ResultAdmin(admin.ModelAdmin):
    readonly_fields = (
        'fullname',
        'totall',
        'score',
        'percent',
        'correct',
        'wrong',
        'created_at',
    )
    list_display = ('fullname', 'percent', 'score', 'totall')
    list_filter = ('percent',)
    search_fields = ('fullname',)


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer', 'status')
    list_filter = ('status',)


admin.site.register(Question, QuestionAdmin)
admin.site.register(UserResult, ResultAdmin)
admin.site.unregister(Group)