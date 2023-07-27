from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializer import Lab32Serializer
from .models import Lab32
from .permissions import IsOwnerOrReadOnly

class Lab32List(generics.ListCreateAPIView):
    # this does need the comma because it is a tuple, not just data in parens
    # permission_classes = (IsAuthenticated,)
    queryset = Lab32.objects.all()
    serializer_class = Lab32Serializer

class Lab32Detail(generics.RetrieveUpdateDestroyAPIView):
    # this does need the comma because it is a tuple, not just data in parens
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    queryset = Lab32.objects.all()
    serializer_class = Lab32Serializer

    