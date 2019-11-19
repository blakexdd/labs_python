from django.http import HttpResponse
from django.shortcuts import render
import json

with open("json_data.json", 'r') as read_file:
    data = json.load(read_file)
    name = data['name']
    head_name = data['head']['name']
    head_surname = data['head']['surname']
    index = data['location']['index']
    city = data['location']['city']
    adress = data['location']['adress']
    ad_amount = len(data['administrative'])
    sc_amount = len(data['scintific_and_educational'])
    mf_amount = 0
    for i in data['scintific_and_educational']:
        if i['name'].find("Мегафакультет") != -1:
            mf_amount += 1
    dep_amount = 0
    for i in data['scintific_and_educational']:
        dep_amount += len(i['departments'])

    dict = {'name': name, 'head': [head_name, head_surname],
            'adress': {'index': index, 'city': city, 'adress': adress},
            'ad_amount': ad_amount,
            'sc_amount': sc_amount,
            'mf_amount': mf_amount,
            'dep_amount': dep_amount}


def index(request):
    return HttpResponse("Hello, world!")


#def indexRender(request):
#    return render(request, 'index.html', {})

def indexRender(request):
    return render(request, 'universityInfo.html', dict)