from rest_framework import serializers
from watchlist_app.models import WatchList

class MovieSerializer(serializers.ModelSerializer):
    description_length=serializers.SerializerMethodField()
    
    class Meta:
        model = WatchList
        fields = '__all__'
        
    def get_description_length(self,obj):
        return len(obj.description)
        
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