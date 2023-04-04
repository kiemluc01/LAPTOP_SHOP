from django.shortcuts import render
import json
from . import HandleString as hs
from rest_framework.views import APIView
from rest_framework.response import Response
from django.templatetags.static import static
from rest_framework import status, viewsets
from chatbox.models import HistoryChat
from chatbox.serializers import HistoryChatSerializer, ProductHistory, StaffHistorySerializer, DetailHistorychatSerializer
from shopapp.models import Product
from shopapp.serializers import DetailProductSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication

# Create your views here.s

class ChatAIViewset(viewsets.ModelViewSet):
    queryset = HistoryChat.objects.all()
    serializer_class = HistoryChatSerializer
    
    def get_serializer_class(self):
        if self.action == 'list':
            return DetailHistorychatSerializer
        return HistoryChatSerializer
    
    # def create(self, request, *args, **kwargs):
    #     with open('chatbox/{}'.format(static("data/AI.json")),encoding='utf-8') as file:
    #         data = json.load(file)
    #     answer = "Tôi không hiểu câu hỏi của bạn"
    #     for intent in data["intents"]:
    #         for questions in intent['questions']:
    #             if hs.special_characters(hs.no_accent_vietnamese(request.data['question'])).find(hs.special_characters(hs.no_accent_vietnamese(questions))) >=0:
    #                 answer = intent["answers"][0]
    #     serializer_user = HistoryChatSerializer(user=request.user, content= request.data['question'])
    #     if serializer_user.is_valid():
    #         serializer_user.save()
        
        
    
class ChatAI(APIView):
    authentication_classes = [JWTAuthentication]
    
    def get(self, request):
        with open('chatbox/{}'.format(static("data/history.json")),encoding='utf-8') as file:
            data = json.load(file)
        return Response(data)
    
    def post(self, request):
        with open('chatbox/{}'.format(static("data/AI.json")),encoding='utf-8') as file:
            data = json.load(file)
        answer = "Tôi không hiểu câu hỏi của bạn"
        has_image = 0
        for intent in data["intents"]:
            user_ques = hs.no_accent_vietnamese(request.data['question'])
            if hs.check(intent['questions'],user_ques):
                answer = intent["answers"][0]
                if intent['questions'] ==  ["sản phẩm đang hot", "sản phẩm nổi bật nhất"] or intent['questions'] ==["sản phẩm mới nhất", "sản phẩm mới"]:
                    products = Product.objects.all().order_by('created_at')
                    answer = '<div className="has_image"><span>Những sản phẩm mới nhất của cửa hàng:'
                    for product in products:
                        answer+='</span><br/> <a href="/login"> <img src="http://127.0.0.1:8000/media/{}" alt=""/><span><strong>{}</strong></span><span>giá bán: {}</span></a>'.format(product.rootImage,product.name, product.price)
                    answer+='</div>'
                    has_image = 1
                with open('chatbox/{}'.format(static("data/history.json")),encoding='utf-8') as file:
                    data = json.load(file)
                stt =1
                if data != []:
                    stt = data[-1]['stt'] + 1
                history_user =  {"stt":stt, "status":"user-AI", "text":request.data['question'], "users":"1", "has_image":False}
                history_AI = {"stt":stt+1, "status":"AI", "text":answer, "users":"1", "has_image":has_image}
                data.append(history_user)
                data.append(history_AI)
                
                with open('chatbox/{}'.format(static("data/history.json")), "w", encoding='utf-8') as file:
                    file.write(json.dumps(data))
                return Response({"answer": answer, "has_image":has_image}, status=status.HTTP_200_OK)
        return Response({"answer": answer, "has_image":has_image}, status=status.HTTP_200_OK)
            