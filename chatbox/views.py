from django.shortcuts import render
import json
from . import HandleString as hs
from rest_framework.views import APIView
from rest_framework.response import Response
from django.templatetags.static import static
from rest_framework import status

# Create your views here.s
class ChatAI(APIView):
    def get(self, request):
        with open('chatbox/{}'.format(static("data/history.json")),encoding='utf-8') as file:
            data = json.load(file)
        return Response(data)
    
    def post(self, request):
        with open('chatbox/{}'.format(static("data/AI.json")),encoding='utf-8') as file:
            data = json.load(file)
        answer = "Tôi không hiểu câu hỏi của bạn"
        for intent in data["intents"]:
            for questions in intent['questions']:
                if hs.special_characters(hs.no_accent_vietnamese(request.data['question'])).find(hs.special_characters(hs.no_accent_vietnamese(questions))) >=0:
                    answer = intent["answers"][0]
        with open('chatbox/{}'.format(static("data/history.json")),encoding='utf-8') as file:
            data = json.load(file)
        print(data[-1]['stt'])
        history_user =  {"stt":data[-1]['stt'] + 1, "status":"user-AI", "text":request.data['question'], "users":"1"}
        history_AI = {"stt":data[-1]['stt'] + 2, "status":"AI", "text":answer, "users":"1"}
        data.append(history_user)
        data.append(history_AI)
        
        with open('chatbox/{}'.format(static("data/history.json")), "w", encoding='utf-8') as file:
            file.write(json.dumps(data))
        return Response(answer, status=status.HTTP_200_OK)