from django.shortcuts import render
from requests import get
from json import loads


def index(request):
    return render(request, 'scanner/index.html')


def engines(request):
    response = get("http://iss.moex.com/iss/engines.json")
    text = loads(response.text)
    return render(request, 'scanner/engines.html', {'text': text})


def markets(request):
    engine = request.GET['engine']
    request_markets = "http://iss.moex.com/iss/engines/" + engine + "/markets.json"
    response = get(request_markets)
    text = loads(response.text)
    d = {'request_markets': request_markets,
         'text': text,
         'engine': engine}
    return render(request, 'scanner/markets.html', d)


def securities(request):

    try:
        engine = request.GET['engine']
        market = request.GET['market']
        request_securities = "?engine="+engine+"&market="+market
    except KeyError:
        engine = "все"
        market = "все"
        request_securities = ""
    request_securities = "http://iss.moex.com/iss/securities.json" + request_securities
    response = get(request_securities)
    text = loads(response.text)
    d = {'request_securities': request_securities,
         'text': text,
         'engine': engine,
         'market': market}
    return render(request, 'scanner/securities.html', d)
