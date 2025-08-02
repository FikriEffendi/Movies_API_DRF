from rest_framework import serializers
from watchlist_app.models import WatchList

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=200)
    active = serializers.BooleanField()

    def create(self, validated_data):
        return WatchList.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name=validated_data.get('name',instance.name)
        instance.description=validated_data.get('description',instance.description)
        instance.active=validated_data.get('active',instance.active)
        instance.save()
        return instance
    
    def validate_name(self,value):
        if len(value)<2:
            raise serializers.ValidationError("Name must be at least 2 characters long")
        return value
    
    def validate_description(self,value):
        if len(value)<10:
            raise serializers.ValidationError("Description must be at least 10 characters long")
        return value
    
    def validate(self,data):
        if data['name']==data['description']:
            raise serializers.ValidationError("Name and description must be different")
        return data