from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from .models import *


class HelloAPI(APIView):
    def get(self, request):
        d = {
            'xabar': 'Salom Dunyo',
            'izoh': 'Test uchun API yozdik'
        }
        return Response(d)

    def post(self, request):
        d = request.data
        natija = {
            'xabar': 'POST qabul qilindi',
            'post malumoti': d
        }
        return Response(natija)


class AktyorlarAPI(APIView):
    def get(self, request):
        aktyorlar = Aktyor.objects.all()
        serializer = AktyorSerializer(aktyorlar, many=True)
        return Response(serializer.data)

    def post(self, request):
        aktyor = request.data
        serializer = AktyorSerializer(data=aktyor)
        if serializer.is_valid():
            d = serializer.validated_data
            Aktyor.objects.create(
                ism=d.get('ism'),
                davlat=d.get('davlat'),
                jins=d.get('jins'),
                tugilgan_yil=d.get('tugilgan_yil')
            )
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class AktyorAPI(APIView):
    def get(self, request, pk):
        aktyor = Aktyor.objects.get(id=pk)
        serializer = AktyorSerializer(aktyor)
        return Response(serializer.data)

    def update(self, request, pk):
        aktyor = Aktyor.objects.get(id=pk)
        serializer = AktyorSerializer(aktyor, data=request.data)
        if serializer.is_valid():
            d = serializer.validated_data
            Aktyor.objects.filter(id=pk).update(
                ism=d.get('ism'),
                davlat=d.get('davlat'),
                jins=d.get('jins'),
                tugilgan_yil=d.get('tugilgan_yil')
            )
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class TariflarAPI(APIView):
    def get(self, request):
        tariflar = Tarif.objects.all()
        serializer = TarifSerializer(tariflar, many=True)
        return Response(serializer.data)

    def post(self, request):
        tarif = request.data
        serializer = TarifSerializer(data=tarif)
        if serializer.is_valid():
            data = serializer.validated_data
            Tarif.objects.create(
                nom=data.get('nom'),
                narx=data.get('narx'),
                davomiylik=data.get('davomiylik')
            )
            return Response(serializer.data)
        return Response(serializer.errors)


class TarifOchirAPI(APIView):
    def get(self, request, pk):
        d = Tarif.objects.get(id=pk)
        serializer = TarifSerializer(d)
        d.delete()
        return Response(serializer.data)


class TarifUpdateAPI(APIView):
    def get(self, request, pk):
        tarif = Tarif.objects.get(id=pk)
        serializer = TarifSerializer(tarif)
        return Response(serializer.data)

    def put(self, request, pk):
        tarif = Tarif.objects.get(id=pk)
        serializer = TarifSerializer(tarif, data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            Tarif.objects.filter(id=pk).update(
                nom=data.get('nom'),
                narx=data.get('narx'),
                davomiylik=data.get('davomiylik')
            )
            return Response(serializer.data)
        return Response(serializer.errors)
