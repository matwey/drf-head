from rest_framework.reverse import reverse
from theapp import models
from rest_framework import serializers

class ModelSerializer(serializers.HyperlinkedModelSerializer):
	url = serializers.HyperlinkedIdentityField(lookup_field='name', view_name='model-detail')
