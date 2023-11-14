from django.views.generic import TemplateView
from .utils import make_prediction
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


class HomeView(TemplateView):
    template_name = "core/home.html"


class PredictView(TemplateView):
    template_name = "core/home.html"

    def post(self, request, *args, **kwargs):
        email_text = request.POST.get("email-content")
        prediction = make_prediction(email_text)
        return render(request, self.template_name, {'prediction': prediction,
                                                    'text': email_text})


class PredictAPIView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        email_text = data.get("email-content", "")
        prediction = make_prediction(email_text)
        return Response({"prediction": prediction})
