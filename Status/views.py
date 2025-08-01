from django.shortcuts import render
from .models import Status

def view_status(request):
    #status = Status.objects.filter(id=1).first()
    return render(request, 'status.html')