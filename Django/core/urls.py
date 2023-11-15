"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import core.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('spam', core.views.HomeView.as_view(), name="spam"),
    path('fraud', core.views.FraudHomeView.as_view(), name="fraud"),
    path('spam/predict', core.views.PredictView.as_view(), name="spam_predict"),
    path('fraud/predict', core.views.FraudPredictView.as_view(), name="fraud_predict"),
    path('api/fraud/predict', core.views.PredictAPIView.as_view(), name="fraud_predict_api"),
    path('api/spam/predict', core.views.PredictAPIView.as_view(), name="spam_predict_api"),
    path('api-auth/', include('rest_framework.urls'))
]
