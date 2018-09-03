from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
data="<html><body><table><tr><th>Eid</th><th>Ename</th><th>Esalary</th></tr>" \
     "<tr><td>1001</td><td>Scott</td><td>10000</td></tr>" \
     "<tr><td>1002</td><td>Alex</td><td>20000</td></tr>" \
     "<tr><td>1003</td><td>John</td><td>20000</td></tr>" \
     "<tr><td>1004</td><td>Amith</td><td>20000</td></tr>" \
     "<tr><td>1005</td><td>Rajesh</td><td>20000</td></tr>" \
     "<tr><td>1006</td><td>Mohan</td><td>20000</td></tr>" \
     "<tr><td>1007</td><td>Santosh</td><td>20000</td></tr>" \
     "</table></body></html>"
def htmlview(request):
     return HttpResponse(data,content_type="text/html")
def excelview(request):
     return HttpResponse(data,content_type="application/vnd.ms-excel")
def xmlview(request):
     return HttpResponse(data,content_type="application/xml")
def jsonview(request):
     return HttpResponse(data,content_type="application/json")
def csvview(request):
     return HttpResponse(data,content_type="text/csv")
def pdfview(request):
     return HttpResponse(data,content_type="application/pdf")
def wordview(request):
     return HttpResponse(data,content_type="application/msword")