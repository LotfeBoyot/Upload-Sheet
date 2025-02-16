from rest_framework import generics
from .models import *
from .serializers import *
from django.http import JsonResponse
from django.views import View
from django.core.management import call_command

class UnitListView(generics.ListCreateAPIView):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer


class ActorListView(generics.ListCreateAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class UnitTypeListView(generics.ListCreateAPIView):
    queryset = UnitType.objects.all()
    serializer_class = UnitTypeSerializer


class UnitStatusListView(generics.ListCreateAPIView):
    queryset = UnitStatus.objects.all()
    serializer_class = UnitStatusSerializer


class BuildingListView(generics.ListCreateAPIView):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer



class RunCommandView(View):
    def get(self, request, *args, **kwargs):
        try:
            call_command('populate_dummy_tables')  # Replace with your actual command name
            return JsonResponse({'status': 'success', 'message': 'Command executed successfully.'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)