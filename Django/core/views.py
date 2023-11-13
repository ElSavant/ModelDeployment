from django.views.generic import TemplateView
from .utils import make_prediction
from django.shortcuts import render


class HomeView(TemplateView):
    template_name = "core/home.html"


class PredictView(TemplateView):
    template_name = "core/home.html"

    def post(self, request, *args, **kwargs):
        email_text = request.form.get("email-content")
        prediction = make_prediction(email_text)
        return render(request, self.template_name, {'prediction': prediction,
                                                    'text': email_text})
