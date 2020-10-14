from rest_framework.views import APIView
#response will be given from response function
from rest_framework.response import Response

class SampleApiView(APIView):
    ''' The get method is responsible for handling the get responses'''
    def get(self,request,format=None):
        #always response should in the form of dictionary
        return Response({'name':"SampleAPIView",'message':"Hello Akhil"})
    def post(self,request,format=None):
        return Response({'message':request.data,"request_method":"POST"})
    def put(self,request,format=None):
        return Response({'message':request.data,"request_method":"PUT"})
    def patch(self,request,format=None):
        return Response({'message':request.data,"request_method":"PATCH"})
    def delete(self,request,format=None):
        return Response({"request_method":"DELETE"})
    