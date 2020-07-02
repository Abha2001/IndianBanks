from .models import Banks,Branches
from rest_framework import serializers

class BanksSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= Banks
        fields= ['url', 'name', 'id']

class BranchesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= Branches
        fields= ['url','ifsc', 'bank','branch', 'address','city','district','state']