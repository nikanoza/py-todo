from rest_framework import generics
from .models import Todo
from .serializers import TodoSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

class TodoCreate(APIView):
    def post(self, request):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class TodoList(APIView):
    def get(self, request):
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)

class TodoUpdate(APIView):
    def put(self, request, id):
        todo = self.get_object(id)
        serializer = TodoSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TodoDelete(APIView):
    def get_object(self, id):
        try:
            return Todo.objects.get(id=id)
        except Todo.DoesNotExist:
            raise Http404

    def delete(self, request, id):
        todo = self.get_object(id)
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class TodoDeleteInactive(APIView):
    def delete(self, request):
        deleted_count = Todo.objects.filter(active=True).delete()
        return Response({"message": f"{deleted_count[0]} inactive todos deleted."})