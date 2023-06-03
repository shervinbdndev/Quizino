from rest_framework import serializers
from .models import (Question, UserResult)



class QuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        exclude = ('status',)
        read_only_fields = ('id',)
        



class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserResult
        exclude = ('created_at', 'id')