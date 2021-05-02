import hashlib

from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ViewSet
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from .serializer import UploadSerializer
from rest_framework.views import APIView

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from django.conf import settings
from django.core.files.storage import FileSystemStorage

# ViewSets define the view behavior.

@method_decorator(csrf_exempt, name='dispatch')
class UploadViewSet(ViewSet):
    serializer_class = UploadSerializer

    def list(self, request):
        return Response("GET API")

    def create(self, request):

        file_uploaded = request.FILES.get('file_uploaded')
        if file_uploaded:
            filename = self.handle_uploaded_file(request.POST,request.FILES.get('file_uploaded'))

        readFile = file_uploaded.read()
        md5Hash = hashlib.md5(readFile).hexdigest()
        
        content_type = file_uploaded.content_type
        #change response to be the hash
        
        response = "POST API and you have uploaded a file {} his hash is {}".format(file_uploaded, md5Hash)

        return Response(response)
        


    def handle_uploaded_file(self,post,f):
        with open(settings.MEDIA_ROOT+'/'+f.name, 'wb+') as destination:
            #MDOR_REPOSITORY
            mdorrepository = settings.MEDIA_ROOT
            fs = FileSystemStorage()
            fs.location=mdorrepository
            
            ff = fs.save(f.name,f)
            return ff #.name

