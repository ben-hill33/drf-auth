from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .permissions import IsOwnerOrReadOnly
from .models import Task
from .serializers import TaskSerializer

class TaskList(ListCreateAPIView):
  queryset = Task.objects.all()
  serializer_class = TaskSerializer
  permission_classes = (IsAuthenticatedOrReadOnly,)

class TaskDetail(RetrieveUpdateDestroyAPIView):
  queryset = Task.objects.all()
  serializer_class = TaskSerializer
  permission_classes = (IsOwnerOrReadOnly,)