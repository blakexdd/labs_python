from django.http import HttpResponse
from django.shortcuts import render
import json

#opening json file to read info from it
with open("json_data.json", 'r') as read_file:
    # load data from json file to data variable
    data = json.load(read_file)

    # assigning name from data to name variable
    name = data['name']

    # assigning head's info from data to head_anme
    # and head_surname variables
    head_name = data['head']['name']
    head_surname = data['head']['surname']

    # assigning location from data to index,
    # city and adress variables
    index = data['location']['index']
    city = data['location']['city']
    adress = data['location']['adress']

    # assigning amount of administrative subsidaries
    ad_amount = len(data['administrative'])

    # assigning amount of scintific subsidaries
    sc_amount = len(data['scintific_and_educational'])

    # assigning amount of mega faclties
    # here we go in loop and searching in
    # sientific and educational subsidaries
    # to count amount of mega faculties
    mf_amount = 0
    for i in data['scintific_and_educational']:
        if i['name'].find("Мегафакультет") != -1:
            mf_amount += 1

    # assigning amount of departments
    # here we go in loop and searching in
    # sientific and educational subsidaries
    # to count amount of departments
    dep_amount = 0
    for i in data['scintific_and_educational']:
        dep_amount += len(i['departments'])

    # forming dictionary of parameters to give
    # it as third argument to render function
    dict = {'name': name, 'head': [head_name, head_surname],
            'adress': {'index': index, 'city': city, 'adress': adress},
            'ad_amount': ad_amount,
            'sc_amount': sc_amount,
            'mf_amount': mf_amount,
            'dep_amount': dep_amount}


# view function for making default page appearance
def index(request):
    return HttpResponse("Hello, world!")

# view function for making hello page appearance
def indexRender(request):
    return render(request, 'index.html', {})

# view function for making ITMO page appearance
def ITMO_University(request):
    return render(request, 'universityInfo.html', dict)