from django.contrib import admin
from django.urls import path

from filmApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', HelloAPI.as_view()),
    path('aktyorlar/', AktyorlarAPI.as_view()),
    path('aktyor/<int:pk>/', AktyorAPI.as_view()),
    path('tariflar/', TariflarAPI.as_view()),
    path('delete_tarif/<int:pk>/', TarifOchirAPI.as_view()),
    path('update_tarif/<int:pk>/', TarifUpdateAPI.as_view())
]
