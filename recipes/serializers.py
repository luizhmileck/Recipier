from rest_framework import serializers
from recipes.models import Recipe


class RecipeSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(
        required=True, allow_blank=False, max_length=255)
    instructions = serializers.CharField(required=True, allow_blank=False)
    rating = serializers.IntegerField(required=True, min_value=1, max_value=10)

    def create(self, validated_data):
        return Recipe.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.instructions = validated_data.get(
            'instructions', instance.instructions)
        instance.rating = validated_data.get('rating', instance.rating)
        instance.save()
        return instance
