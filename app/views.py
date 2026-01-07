from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Car
from .serializers import CarSerializer
from rest_framework import status
from datetime import datetime
from .serializers import CarSerializer


class CarListApiView(APIView):

    def get(self, request):
        cars = Car.objects.all()
        serializer = CarSerializer(cars, many=True) 
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = CarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    'data': 'Car successfully created',
                    'create': True,
                    'created_at': str(datetime.now())
                },
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CarDetailApiView(APIView):

    def get(self, request, pk):
        try:
            car = Car.objects.get(pk=pk)
        except Car.DoesNotExist:
            return Response(
                {"error": "Car not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = CarSerializer(car)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        try:
            car = Car.objects.get(pk=pk)
        except Car.DoesNotExist:
            return Response(
                {"error": "Car not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = CarSerializer(car, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            car = Car.objects.get(pk=pk)
        except Car.DoesNotExist:
            return Response(
                {"error": "Car not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        car.delete()
        return Response(
            {"message": "Car deleted"},
            status=status.HTTP_204_NO_CONTENT
        )
