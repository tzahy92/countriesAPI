from .views import countries_detail
from django.conf.urls import url
from countries import views

urlpatterns = [
    url(r'^api/countries$', views.countries_list),
    url(r'^api/countries/(?P<pk>[0-9]+)$', countries_detail)
]
