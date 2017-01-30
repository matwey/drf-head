from django.db.models.deletion import ProtectedError
from theapp import models, serializers
from rest_framework import status, viewsets
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser

class ModelViewSet(viewsets.ModelViewSet):
	queryset = models.Model.objects.all()
	serializer_class = serializers.ModelSerializer
	lookup_field = 'name'

	def retrieve(self, request, name=None):
		response = super(ModelViewSet, self).retrieve(request, name)
		response['Link'] = "http://foo.com; rel=begin"
		return response
