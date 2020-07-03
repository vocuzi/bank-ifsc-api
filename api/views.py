from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView

from api.models import Bank
from api.serializers import BankSerializer


@api_view(['POST'])
def bank_details(request):
	if request.method == "POST":
		if request.data.get("ifsc"):
			"""
			Get bank details with IFSC Code
			"""
			banks = Bank.objects.filter(ifsc=request.data["ifsc"])
			if banks.count():
				serializer = BankSerializer(banks[0])
				return Response(serializer.data)
			else:
				return Response(status=status.HTTP_404_NOT_FOUND)
		if request.data.get("name") and request.data.get("city"):
			"""
			Get list of banks with Bank name and City in input
			"""
			paginator = PageNumberPagination()
			paginator.page_size= 10
			banks = Bank.objects.filter(bank_name=request.data["name"],city=request.data.get("city"))
			payload = paginator.paginate_queryset(banks,request)
			serializer = BankSerializer(payload,many=True)
			return paginator.get_paginated_response(serializer.data)
		else:
			return Response(status=status.HTTP_400_BAD_REQUEST)
	return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)