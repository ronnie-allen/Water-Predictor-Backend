from django.urls import path
from .views import WaterPredictAPIView

urlpatterns = [
    path('predict/', WaterPredictAPIView.as_view(), name='water-predict'),
]