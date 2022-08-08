import pandas as pd
import requests

from app.models import Data
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, UpdateAPIView, DestroyAPIView
from app.serializers import DataSerializer
from rest_framework.response import Response


class Create(APIView):
    def put(self, request):
        file = self.request.data["file"]
        data = pd.read_excel(file)
    
        for index, row in data.iterrows():
            Data.objects.create(text=row['text'], label=row['label'])
        return Response({"message": "Data created."})
  
class List(ListAPIView):
    serializer_class = DataSerializer
    queryset = Data.objects.all()

class Update(UpdateAPIView):
    serializer_class = DataSerializer
    queryset = Data.objects.all()

class Delete(DestroyAPIView):
    serializer_class = DataSerializer
    queryset = Data.objects.all()

class Train(APIView):
    #serializer_class = DataSerializer
    #queryset = Data.objects.all()

    def post(self):
        res = requests.post('http://127.0.0.1:3535/train')
        return Response({"message":"success"})

class Predict(APIView):
    #serializer_class = DataSerializer
    #queryset = Data.objects.all()

    def post(self, request):
        res = requests.post('http://127.0.0.1:3535/predict?text=%s'%request.POST.get("text"))
        return Response(res)