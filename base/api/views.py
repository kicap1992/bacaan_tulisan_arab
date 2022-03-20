import os
from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import tb_bacaan
from .serializers import tb_bacaanSerializer
from .check_similarity import check_similarity
from .interfaceCLI import cek_simlilarity2

from .librosa_run import fungsi_librosa

@api_view(['GET', 'POST'])
def getRoutes(request):
  
  if request.method == 'GET':
    
    routes = [
      'GET /api',
      'POST /api/bacaan',
      
      
    ]
    return Response(routes)
  if request.method == 'POST':
    url_bacaan = request.POST['url_bacaan']
    nama = request.FILES['sound'].name
    nama = nama.replace('Z', '').replace('.wav', '').replace('.', '').replace('-', ' ').replace(':', ' ').replace('T', ' ')
    path = 'static/uploaded/'
    # print(bool(request.FILES.get('hehe', False))) # check if file is empty , true is not empty . false is empty
    handle_uploaded_file(request.FILES['sound'],url_bacaan,nama)
    # check_similarity(path+nama+'.wav', 'static/audio/'+url_bacaan)
    # similarity = check_similarity(path+nama+'.wav', 'static/audio/'+url_bacaan)
    librosa_run = fungsi_librosa(path+nama+'.wav', 'static/audio/'+url_bacaan)
    # remove athe last 5 char on url_bacaan
    url_bacaan =  url_bacaan[:-5]
    # print(url_bacaan)
    # similarity2 = cek_simlilarity2(path+nama+'.wav', 'static/audio/'+url_bacaan)
    dataall = {'data' : 'sini data'}
    #add librosa_run dictinary to dataall
    dataall.update(librosa_run)   
    return Response(dataall)


def handle_uploaded_file(f,url_bacaan,nama):
    path = 'static/uploaded/' # this is the path to the folder where you want to save the file
    isExist = os.path.exists(path) # check if the folder exist
    if not isExist: # if not exist then create the folder
      os.mkdir(path) # create the folder
    with open(path+nama+'.wav', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
            
    

@api_view(['GET'])
def getBacaans(request):
  bacaans = tb_bacaan.objects.all()
  serializer = tb_bacaanSerializer(bacaans, many=True)
  return Response(serializer.data)

@api_view(['GET'])
def getBacaan(request,pk):
  bacaan = tb_bacaan.objects.get(id=pk)
  serializer = tb_bacaanSerializer(bacaan)
  return Response(serializer.data)