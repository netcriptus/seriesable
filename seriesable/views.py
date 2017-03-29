from django.views.generic import ListView
from django.http import HttpResponse

class Health(ListView):
    def get(self, request):
        return HttpResponse("ok")
