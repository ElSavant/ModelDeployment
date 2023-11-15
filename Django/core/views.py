from django.views.generic import TemplateView
from .utils import make_prediction, model_predict
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


class HomeView(TemplateView):
    template_name = "core/home.html"


class FraudHomeView(TemplateView):
    template_name = "core/index.html"


class FraudPredictView(TemplateView):
    template_name = "core/results.html"

    def get(self, request, *args, **kwargs):
        results = {
            "Amount": "",
            "Merchant": "",
            "Location": "",
            "TimeOfDay": "",
            "TransactionType": "",
            "Predictions": ""
            }
        return render(request, self.template_name, {'results': results})

    def post(self, request, *args, **kwargs):
        input_data = {
            "Amount": request.POST.get("amount"),
            "Merchant": request.POST.get("merchant"),
            "Location": request.POST.get("location"),
            "TimeOfDay": request.POST.get("timeOfDay"),
            "TransactionType": request.POST.get("transactionType")
        }
        results = model_predict(input_data)
        return render(request, self.template_name, {**results})


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
