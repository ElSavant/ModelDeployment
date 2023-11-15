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
    path('', core.views.HomeView.as_view(), name="home"),
    path('api-auth/', include('rest_framework.urls')),
    path('spam', core.views.SpamHomeView.as_view(), name="spam"),
    path('spam/predict', core.views.SpamPredictView.as_view(), name="spam_predict"),
    path('api/spam/predict', core.views.SpamPredictAPIView.as_view(), name="spam_predict_api"),
    path('fraud', core.views.FraudHomeView.as_view(), name="fraud"),
    path('fraud/predict', core.views.FraudPredictView.as_view(), name="fraud_predict"),
    path('api/fraud/predict', core.views.FraudPredictAPIView.as_view(), name="fraud_predict_api"),
]
