from rest_framework import serializers


class PredictSerialiser(serializers.Serializer):
    email_text = serializers.CharField()
    