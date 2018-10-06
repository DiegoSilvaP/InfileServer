  
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import render
# from .forms import UploadFileForm

from filer.models.filemodels import File, Folder
from django.views.decorators.csrf import csrf_exempt

import base64
from django.core.files.base import ContentFile
from random import uniform
import time

# from file_app.models import File



# Imaginary function to handle an uploaded file.
# from somewhere import handle_uploaded_file

@csrf_exempt
def upload_file(request):
    # print("FECHA ",time.strftime("%b %d %Y %H:%M:%S"))
    nombreArchivo=int(uniform(1, 999999.0))

    alldata=request.POST

    
    img = alldata.get("file","0")
    # print("imagen",img)
    carpeta = alldata.get("carpeta", "0")
    oficina = alldata.get("oficina", "0")

    imagen = ContentFile(base64.b64decode(img), name='temp.png') # You can save this as file instance.
    ar = File()
    ar.name=nombreArchivo
    ar.file = imagen
    ar.folder_id=carpeta
    # ar.description = folder
    # ar.sha1 = ""
    ar.save()

    

    

    # # print("DIRECTORIO: ",directorio)

    # print(alldata)
    
    
    return HttpResponse(1)

def obtenerOficinas(request):
    oficinas = Folder.objects.filter(parent__isnull=True)
    arrayofi = []
    for ofi in oficinas:
        ofiDict = dict()
        ofiDict["id"] = ofi.pk
        ofiDict["nombre"] = ofi.name
        arrayofi.append(ofiDict)

    return JsonResponse(arrayofi, safe=False)

@csrf_exempt
def obtenerCarpetas(request):
    carpetas = Folder.objects.filter(parent__pk=request.POST.get("oficina"))
    arrayCarpetas = []
    for dire in carpetas:
        directoriosDict = dict()
        directoriosDict["id"] = dire.pk
        directoriosDict["nombre"] = dire.name
        arrayCarpetas.append(directoriosDict)

    return JsonResponse(arrayCarpetas, safe=False)