from rest_framework import serializers


class AktyorSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    ism = serializers.CharField()
    davlat = serializers.CharField()
    jins = serializers.CharField()
    tugilgan_yil = serializers.DateField()


class TarifSerializer(serializers.Serializer):
    nom = serializers.CharField()
    narx = serializers.IntegerField()
    davomiylik = serializers.DurationField()

