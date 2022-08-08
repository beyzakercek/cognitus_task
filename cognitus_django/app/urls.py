from django.urls import path
from app.views import Create, List, Delete, Update, Train, Predict

urlpatterns = [
    path('create', Create.as_view(), name='create'),
    path('list', List.as_view(), name='list'),
    path('update/<int:pk>', Update.as_view(), name='update'),
    path('delete/<int:pk>', Delete.as_view(), name='delete'),
    path('train', Train.as_view(), name='train'),
    path('predict', Predict.as_view(), name='predict')

]