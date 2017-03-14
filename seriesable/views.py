from django.views.generic import ListView

class Health(ListView):
    def get(self, request):
        return HttpResponse("ok")
