from django.shortcuts import render
from .models import Updates,Sypmtoms,Contact
from django.conf import settings
import requests
from bs4 import BeautifulSoup
# Create your views here.

def getdata(url):
    r = requests.get(url)
    return r.text
up = []

media_url = settings.MEDIA_URL
def index(request):
    htmldata = getdata("https://www.mohfw.gov.in")
    soup = BeautifulSoup(htmldata, 'html.parser')
    for strong in soup.find_all("strong")[5:8]:
        print(strong.text)
        up.append(strong.text)
    updates = Updates.objects.get(pk=1)
    updates.active = up[0]
    updates.recover = up[1]
    updates.death = up[2]
    updates.save()
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
 



