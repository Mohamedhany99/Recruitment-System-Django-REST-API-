from rest_framework import serializers

from hr_management.models import Employee

class EmpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"

    def to_representation(self, instance):
        data = super().to_representation(instance)
        # data['is_on_sale'] = instance.is_on_sale()
        # data['current_price'] = instance.current_price()
        return data
