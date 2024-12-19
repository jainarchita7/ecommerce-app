from rest_framework.views  import APIView
from rest_framework.response import Response
from rest_framework import status
from api.models import Product, CartItems
from api.serializers import UserSerializer, ProductSerializer, CartItemSerializer

class RegistrationView(APIView):
    def post(self, request):
        serializer = UserSerializer(data = request.data , many= True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_Created)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)  


class ProductView(APIView):
    def post(self, request):
        serializer = ProductSerializer(data = request.data , many= True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_Created)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
    def get(self, request):
        products = Product.objects.all()
        # print(products)
        # for product in products:
        #     print(product)
        serializer = ProductSerializer(products, many= True)
        return Response(serializer.data)
    
    def put(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)   
        except Product.DoesNotExist:
            return Response({"error":"Product Not Found"}, status = status.HTTP_404_NOT_FOUND)

        serializer = ProductSerializer(product, data = request.data,partial= True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk):
        try: 
            product = Product.objects.get(pk = pk)
            product.delete()
            return Response(status = status.HTTP_204_NO_CONTENT)
        except Product.DoesNotExist:
            return Response({"error":"Product Not Found"}, status = status.HTTP_404_NOT_FOUND)


class CartView(APIView):
    def post(self, request):
        serializer = CartItemSerializer(data = request.data , many= True)
        if serializer.is_valid():
            serializer.save(user = request.user)
            return Response(serializer.data, status = status.HTTP_201_Created)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def get(self,request):
        cart_items =  CartItems.objects.filter(user=request.user)
        serializer = CartItemSerializer(cart_items, many= True)
        return Response(serializer.data)