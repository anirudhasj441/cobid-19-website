from django.shortcuts import render
from .models import Updates,Sypmtoms,Contact
from django.conf import settings
# Create your views here.

media_url = settings.MEDIA_URL
def index(request):
  
  updates = Updates.objects.get(pk=1)
  symptoms = Sypmtoms.objects.all()
  if request.method == "POST":
    na = request.POST['name']
    ct = request.POST['contact']
    em = request.POST['email']
    msg = request.POST['message']
    Contact.objects.create(name=na,email=em,contact=ct,message=msg)
  params = {
    'updates':updates,
    'media_url':media_url,
    'symptoms':symptoms,
  }
  return render(request,'app/index.html',params)
  