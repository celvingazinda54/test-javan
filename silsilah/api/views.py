import imp
from django.shortcuts import render

# Create your views here.
from rest_framework import serializers, status
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import keluargaSerializer
from .models import keluarga
from anytree import Node, RenderTree
from anytree.exporter import DotExporter

@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'all_items':'/',
        'Search by nama':'/?jenis_kelamin=jen_kel',
        'Search by Subcategory':'/?status=status',
        'Add':'/create',
        'Update':'/update/pk',
        'Delete':'/item/pk/delete',
        'Plot':'/plot',
    }

    return Response(api_urls)

@api_view(['POST'])
def add_items(request):
    item = keluargaSerializer(data=request.data)
  
    # validating for already existing data
    if keluarga.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')
  
    if item.is_valid():
        item.save()
        return Response(item.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def view_items(request):
    items = keluarga.objects.all()
    serializers = keluargaSerializer(items, many=True)
  
    # if there is something in items else raise error
    if items:
        return Response(serializers.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def update_items(request, pk):
    item = keluarga.objects.get(pk=pk)
    data = keluargaSerializer(instance=item, data=request.data)
  
    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_items(request, pk):
	item = get_object_or_404(keluarga, pk=pk)
	item.delete()
	return Response(status=status.HTTP_202_ACCEPTED)

@api_view(['GET'])
def plot_tree(request):
    items = keluarga.objects.all()
    ceo = Node("CEO") #root
    vp_1 = Node("VP_1", parent=ceo)
    vp_2 = Node("VP_2", parent=ceo)
    gm_1 = Node("GM_1", parent=vp_1)
    gm_2 = Node("GM_2", parent=vp_2)
    m_1 = Node("M_1", parent=gm_2)
    

    return Response(DotExporter(ceo).to_picture("ceo.png"))