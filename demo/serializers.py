"""
        serializer resource define
        @author xu_fanghui
        @date 2014-09-03
        @version demo 0.1
"""

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from demo.models import Company,Sector,Staff
from rest_framework import serializers

class CompanySerializer(serializers.ModelSerializer):
     class Meta:
         model=Company
         field=('name','simple_name','address','register_date','money','type','description')


class SectorSerializer(serializers.ModelSerializer):
     class Meta:
         model=Sector
         field=('name','simple_name','description','company')

class StaffSerializer(serializers.ModelSerializer):
     class Meta:
         model=Staff
         field=('name','en_name','birthday','sex','address','job_name','telephone','email','card_id','sectors')

