from django.conf.urls import url
from . import views
app_name='mimeapp'
urlpatterns=[
    url(r'^htmlview$',views.htmlview,name='htmlview'),
    url(r'^excelview$',views.excelview,name='excelview'),
    url(r'^xmlview$',views.xmlview,name='xmlview'),
    url(r'^jsonview$',views.jsonview,name='jsonview'),
    url(r'^csvview$',views.csvview,name='csvview'),
    url(r'^pdfview$',views.pdfview,name='pdfview'),
]