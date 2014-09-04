"""
        views resource define
        @author xu_fanghui
        @date 2014-09-03
        @version demo 0.1
"""

from rest_framework import viewsets
from demo.models import Company,Sector,Staff
from demo.serializers import CompanySerializer,SectorSerializer,StaffSerializer

class CompanyViewSet(viewsets.ModelViewSet):
     queryset=Company.objects.all()
     serializer_class=CompanySerializer

class SectorViewSet(viewsets.ModelViewSet):
     queryset=Sector.objects.all()
     serializer_class=SectorSerializer


class StaffViewSet(viewsets.ModelViewSet):
     queryset=Staff.objects.all()
     serializer_class=StaffSerializer


