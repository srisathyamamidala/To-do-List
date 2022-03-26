from rest_framework import generics
from todos.models import Todo
from todos.serializers import TodoSerializer


class TodoListView(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


def todoItemView(request):
    print(request.POST.get("id"))

    
