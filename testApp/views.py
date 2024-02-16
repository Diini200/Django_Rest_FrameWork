from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
import io
from rest_framework.parsers import JSONParser
from testApp.models import Employee
from testApp.serializers import EmployeeSerializers
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

@method_decorator(csrf_exempt, name='dispatch')
class EmployeeCRUDCBV(View):
    def get(self, request, *args, **kwargs):
        json_data=request.body
        stream = io.BytesIO(json_data)
        pdata=JSONParser().parse(stream)
        id=pdata.get('id', None)
        
        if id is not None:
            emp=Employee.objects.get(id=id)
            serializer= EmployeeSerializers(emp)
            json_data=JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type='application/json', status=200)
        
        qs= Employee.objects.all()    
        serializer= EmployeeSerializers(qs, many=True)
        json_data=JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type='application/json', status=200)
    
    def post(self, request, *args, **kwargs):
        json_data=request.body
        stream=io.BytesIO(json_data)
        pdata=JSONParser().parse(stream)
        serializer=EmployeeSerializers(data=pdata)
        
        if serializer.is_valid():
            serializer.save()
            
            msg={'msg': 'Resouse is been created succesfully.....'}
            json_data= JSONRenderer().render(msg)
            return HttpResponse(json_data, content_type='application/json')
        
        json_data = JSONRenderer.render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json', status=200)
    
    def put(self, request, *args,**kwargs):
        json_data= request.body
        stream=io.BytesIO(json_data)
        pdata= JSONParser().parse(stream)
        
        id=pdata.get('id')
        
        emp=Employee.objects.get(id=id)        
        serializer= EmployeeSerializers(emp, data=pdata, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            
            msg = {'msg': 'Resource updated Successfully...'}
            json_data=JSONRenderer().render(msg)
            return HttpResponse(json_data,content_type='application/json')
        
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')
    
    def delete(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pdata=JSONParser().parse(stream)
        id=pdata.get('id')
        emp= Employee.objects.get(id=id)
        emp.delete()
        
        msg = {'msg': 'Resource Deleted Successfully...'}
        json_data=JSONRenderer().render(msg)
        return HttpResponse(json_data,content_type='application/json')