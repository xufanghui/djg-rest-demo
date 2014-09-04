from django.conf.urls import patterns, include, url
from demo.views import CompanyViewSet,SectorViewSet,StaffViewSet
from rest_framework import routers

# router table setting
router=routers.DefaultRouter()
router.register(u'company',CompanyViewSet)
router.register(u'sector',SectorViewSet)
router.register(u'staff',StaffViewSet)

urlpatterns = patterns('',
    url(r'^',include(router.urls)),
)
