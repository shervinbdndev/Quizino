from typing import (Union, Self)
from django.conf import settings
from rest_framework import status
from django.urls.base import reverse
from django.views.generic import View
from django.core.mail import send_mail
from rest_framework.views import APIView
from django.http.request import HttpRequest
from rest_framework.response import Response
from django.shortcuts import (render, redirect)
from rest_framework.permissions import IsAuthenticated
from django.http.response import (HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect)
from .permissions import IsStaff
from .models import (Question, UserResult)
from .serializers import (QuestionsSerializer, ResultSerializer)






class Quiz(View):
    def get(self: Self, request: HttpRequest) -> Union[HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect]:
        if (request.user.is_authenticated):
            user_flag: bool = True
            if (UserResult.objects.filter(fullname=request.user.username).exists()):
                user_flag = False
            questions: Question = Question.objects.all()
            return render(
                request=request, 
                template_name='index.html', 
                context={
                    'questions': questions,
                    'flag': user_flag,
                }
            )
        else:
            return redirect(to=reverse(viewname='login_page'))

    def post(self: Self, request: HttpRequest) -> Union[HttpResponseRedirect, HttpResponsePermanentRedirect]:
        questions: Question = Question.objects.filter(status=True)
        fullname = request.user.username
        totall = 0
        score = 0
        correct = 0
        wrong = 0
        for q in questions:
            totall += 1
            if (q.answer == request.POST.get(q.question)):
                score += 10
                correct += 1
            else:
                wrong += 1
        percent = f"{score / (totall * 10) * 100:.2f}"

        UserResult.objects.create(
            fullname=fullname,
            totall=totall,
            score=score,
            percent=percent,
            correct=correct,
            wrong=wrong,
        )

        return redirect(to=reverse(viewname='result_page') + fr'?fullname={fullname}')







class Result(View):
    def get(self: Self, request: HttpRequest) -> Union[HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect]:
        if (request.user.is_authenticated):
            try:
                fullname = request.GET['fullname']
                user_object: UserResult = UserResult.objects.get(fullname=fullname)
                return render(
                    request=request,
                    template_name='quiz_app/result.html',
                    context={
                        'user': user_object,
                    }
                )
            except:
                return redirect(to=reverse(viewname='quiz_page'))
        else:
            return redirect(to=reverse(viewname='login_page'))






# def send_email(request: HttpRequest) -> Union[HttpResponseRedirect, HttpResponsePermanentRedirect]:
#     if (request.user.is_authenticated):
#         if (UserResult.objects.filter(fullname=request.user.username).exists()):
#             name = request.user.username
#             user_result: UserResult = UserResult.objects.get(fullname=name)

#             send_mail(
#                 subject='نتایج امتحان',
#                 message=f'''
#                 نام: {user_result}
#                 تعداد سوالات: {user_result.totall}
#                 امتیاز شما: {user_result.score}
#                 درصد: {user_result.percent}%
#                 تعداد جواب های درست: {user_result.correct}
#                 تعداد جواب های غلط: {user_result.wrong}
#                 تاریخ: {user_result.created_at.date()}
#                 ''',
#                 from_email=settings.EMAIL_HOST_USER,
#                 recipient_list=[request.user.email],
#             )
#             return redirect(to=reverse(viewname='result_page'))
#         else:
#             return redirect(to=reverse(viewname='quiz_page'))
#     else:
#         return redirect(to=reverse(viewname='login_page'))








class QuestionListView(APIView):
    permission_classes = [IsAuthenticated, IsStaff]

    def get(self: Self, request: HttpRequest) -> Response:
        questions_list: Question = Question.objects.filter(status=True)
        if (len(questions_list) == 0):
            return Response('هنوز سوالی طرح نشده', status=status.HTTP_204_NO_CONTENT)
        else:
            serializer = QuestionsSerializer(instance=questions_list, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)








class QuestionAddView(APIView):
    permission_classes = [IsAuthenticated, IsStaff]

    def post(self: Self, request: HttpRequest) -> Response:
        serializer: QuestionsSerializer = QuestionsSerializer(data=request.data)
        if (serializer.is_valid()):
            serializer.save()
            return Response({"response": "با موفقیت ذخیره شد"}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)








class QuestionUpdateView(APIView):
    permission_classes = [IsAuthenticated, IsStaff]

    def post(self: Self, request: HttpRequest, pk: int) -> Response:
        instance: Question = Question.objects.get(id=pk)
        serializer: QuestionsSerializer = QuestionsSerializer(data=request.data, partial=True)
        if (serializer.is_valid()):
            serializer.update(instance=instance, validated_data=serializer.validated_data)
            return Response({"response": "بروزرسانی شد"}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)







class QuestionDeleteView(APIView):
    permission_classes = [IsAuthenticated, IsStaff]

    def delete(self: Self, request: HttpRequest, pk: int) -> Response:
        instance: Question = Question.objects.get(id=pk)
        instance.delete()
        return Response({"response": "سوال حذف شد"}, status=status.HTTP_200_OK)








class ResultView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self: Self, request: HttpRequest) -> Response:
        try:
            instance: UserResult = UserResult.objects.get(fullname=request.user)
        except:
            return Response({'Error': 'نتیجه ای وجود ندارد'}, status=status.HTTP_204_NO_CONTENT)
        serializer = ResultSerializer(instance=instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
