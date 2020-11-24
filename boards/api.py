from .models import Board
from .serializers import BoardSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics



@api_view(['GET']) #all boards list
def board_list_api(request):
    boards = Board.objects.all()
    data = BoardSerializer(boards, many=True).data
    return Response({'data':data})


@api_view(['GET']) # one board
def board_detail_api(request, id):
    board = Board.objects.get(id=id)
    data = BoardSerializer(board).data
    return Response({'data':data})

class BoardListApi(generics.ListCreateAPIView):# class view with create
    queryset = Board.objects.all()
    serializer_class = BoardSerializer



class BoardDetail(generics.RetrieveUpdateDestroyAPIView):# class view with create and del and edit
    serializer_class = BoardSerializer
    queryset = Board.objects.all()
    lookup_field = 'id'

