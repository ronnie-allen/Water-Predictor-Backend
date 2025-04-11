from rest_framework import serializers

class WaterInputSerializer(serializers.Serializer):
    ph = serializers.FloatField()
    Hardness = serializers.FloatField()
    Solids = serializers.FloatField()
    Chloramines = serializers.FloatField()
    Sulfate = serializers.FloatField()
    Conductivity = serializers.FloatField()
    Organic_carbon = serializers.FloatField()
    Trihalomethanes = serializers.FloatField()
    Turbidity = serializers.FloatField()
