from rest_framework.authtoken import views
from django.urls import path
from.views import (Quiz, Result, send_email, QuestionListView, QuestionAddView, QuestionUpdateView, QuestionDeleteView, ResultView)

urlpatterns = [
    path(
        route='',
        view=Quiz.as_view(),
        name='quiz_page',
    ),
    
    path(
        route='result',
        view=Result.as_view(),
        name='result_page',
    ),
    
    path(
        route='receive-result',
        view=send_email,
        name='send_email',
    ),
    
    path(
        route='api/authentication',
        view=views.obtain_auth_token,
        name='Api_Auth',
    ),
    
    path(
        route='api/questions',
        view=QuestionListView.as_view(),
        name='questionList_api',
    ),
    
    path(
        route='api/question/add',
        view=QuestionAddView.as_view(),
        name='QuestionAdd_api',
    ),
    
    path(
        route='api/question/update/<int:pk>',
        view=QuestionUpdateView.as_view(),
        name='QuestionUpdate_api',
    ),
    
    path(
        route='api/question/delete/<int:pk>',
        view=QuestionDeleteView.as_view(),
        name='QuestionDelete_api',
    ),
    
    path(
        route='api/userresult',
        view=ResultView.as_view(),
        name='UserResult_api',
    ),
]
