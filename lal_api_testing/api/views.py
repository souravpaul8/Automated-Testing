from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Person
from rest_framework import status

@api_view(['GET', 'POST'])
def get_names(request):
    if request.method == 'GET':
        names = Person.objects.all().values_list("name", flat=True)
        return Response({"people": list(names)})

    elif request.method == 'POST':
        name = request.data.get("name")
        if not name:
            return Response({"error": "Name is required."}, status=status.HTTP_400_BAD_REQUEST)

        Person.objects.create(name=name)
        return Response({"message": f"Person '{name}' added successfully."}, status=status.HTTP_201_CREATED)

