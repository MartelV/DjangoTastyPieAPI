from django.urls import path, include
from tastypie.api import Api
from api.resources import NoteResource

v1_api = Api(api_name='v1')
v1_api.register(NoteResource())

urlpatterns = [
    path('', include(v1_api.urls)),
]
