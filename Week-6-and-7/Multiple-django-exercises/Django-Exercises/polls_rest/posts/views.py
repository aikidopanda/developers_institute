from django.shortcuts import render
from rest_framework.permissions import (IsAdminUser, IsAuthenticated, AllowAny)

# Create your views here.

from rest_framework.views import APIView

# Create your views here.

class PostView(APIView):

    permission_classe = (IsAdminUser)

    def get(self, request, *args, **kwargs):
        queryset = Post.objects.all()
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)
