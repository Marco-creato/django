
from django.urls import path
from .views import findex, fhistoria

urlpatterns = [
   path('', findex),
   path('fhistoria/', fhistoria, name='fhistoria'),
   path('findex/', findex, name='findex'),


]
