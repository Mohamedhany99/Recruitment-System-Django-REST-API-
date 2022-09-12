from rest_framework.exceptions import ValidationError
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.pagination import LimitOffsetPagination

from hr_management.serializer import EmpSerializer
from hr_management.models import Employee

class EmpPagination(LimitOffsetPagination):
    default_limit = 10
    max_limit = 100

class EmpList(ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmpSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('id',)
    search_fields = ('name', 'job_title')
    pagination_class = EmpPagination

class EmpCreate(CreateAPIView):
    serializer_class = EmpSerializer

    def create(self, request, *args, **kwargs):
        # try:
            # passvalidate =  request.data.get('price')
        #     if price is not None and float(price) <= 0.0:
        #         raise ValidationError({ 'price': 'Must be above $0.00' })
        # except ValueError:
        #     raise ValidationError({ 'price': 'A valid number is required' })
        return super().create(request, *args, **kwargs)
