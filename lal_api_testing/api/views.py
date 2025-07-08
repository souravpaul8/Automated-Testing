from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Person

@api_view(['GET'])
def get_names(request):
    names = Person.objects.all().values_list("name", flat=True)
    return Response({"people": list(names)})

