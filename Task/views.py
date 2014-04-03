from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from .forms import UploadFileForm
import httplib, urllib
from Task.models import *
import urllib2


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            response = urllib2.urlopen('http://http://api.hackerearth.com/code/compile/')
            compile_result=respose.read()
            entry=file.object.create(file_id=compile_result['id'])
            entry.save()
            #(request.FILES['file'])
            return render(request, 'HackerEarth_task.html',dict(compile_result=compile_result))
            #return HttpResponseRedirect('http://api.hackerearth.com/code/compile')
    else:
        form = UploadFileForm()
    return render_to_response('HackerEarth_task.html', {'form': form})
