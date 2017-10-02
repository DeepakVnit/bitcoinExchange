# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import requests as httprequest
import json
import socket   #for sockets
import sys

#Django imports
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import permissions
#my imports
from bitcoinapp.constants import generateAvgUrl
from bitcoinapp.constants import marketinfo

# from bitcoinapp.constants import
# Create your views here.

@api_view(['GET','OPTIONS'])
def getRate(request):
    resultjson = {}
    tokenr = Token.objects.filter(user_id=2)
    # if validateuser(request,tokenr) and request.method in permissions.SAFE_METHODS:
    if True:
        fsym = request.GET.get('fsym',None)
        tsym = request.GET.get('tsym',None)
        markets = request.GET.get('markets',None)

        url = generateAvgUrl + "?" + "fsym="+fsym+"&tsym="+tsym+"&markets="+markets
        print(url)
        r = httprequest.request('GET', url)
        response = json.loads(r.text)
        resultjson["SYMBOL"] =      response["RAW"]["FROMSYMBOL"]
        resultjson["CURRENCY"] =    response["RAW"]["TOSYMBOL"]
        resultjson["PRICE"] =       response["RAW"]["PRICE"]
        resultjson["LASTMARKET"] =  response["RAW"]["LASTMARKET"]
        resultjson["VOLUME"] =      response["RAW"]["VOLUME24HOUR"]
        resultjson["PCTCHANGE"] =   response["DISPLAY"]["CHANGEPCT24HOUR"]

    return Response(resultjson)


def validateuser(request,tokenr):
    if tokenr and request.META.get("HTTP_TOKEN") and tokenr[0].key == request.META["HTTP_TOKEN"]:
        return True
    else:
        return False


@api_view(['GET','OPTIONS'])
def markets(request):
    tokenr = Token.objects.filter(user_id=2)
    # if validateuser(request,tokenr):
    return Response(marketinfo)
    # else:
    #     return Response({"F":"R"})


@api_view(['GET'])
def marketsdbApi(request):
    print request.user

    return Response({})


@api_view(['GET'])
def socketfunction(request):
    # create an INET, STREAMing socket
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error:
        print 'Failed to create socket'
        sys.exit()

    print 'Socket Created'

    host = 'wss://streamer.cryptocompare.com'
    port = 80

    try:
        remote_ip = socket.gethostbyname(host)

    except socket.gaierror:
        # could not resolve
        print 'Hostname could not be resolved. Exiting'
        sys.exit()

    # Connect to remote server
    s.connect((remote_ip, port))

    print 'Socket Connected to ' + host + ' on ip ' + remote_ip

    # Send some data to remote server
    # message = "GET /data/generateAvg?fsym=XRP&tsym=INR&markets=BTCXIndia"
    message = "GET / HTTP/1.1\r\n\r\n"

    try:
        # Set the whole string
        s.sendall(message)
    except socket.error:
        # Send failed
        print 'Send failed'
        sys.exit()

    print 'Message send successfully'

    # Now receive data
    reply = s.recv(4096)

    print reply
    return Response({})