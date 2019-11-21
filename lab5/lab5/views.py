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

    # assigning id of educational programm
    edp_id = data['scintific_and_educational'][0]['departments'][0]['educational_programs'][0]['id']

    # assigning name of educational programm
    edp_name = data['scintific_and_educational'][0]['departments'][0]['educational_programs'][0]['name']

    # assigning name of discipline
    dis_name = data['scintific_and_educational'][0]['departments'][0]['educational_programs'][0]['discipline']

    # assigning year of study
    year_of_study = data['scintific_and_educational'][0]['departments'][0]['educational_programs'][0]['year']

    # assigning administrative units data to administrative variable
    administrative = data['administrative']

    # assigning amount of groups
    amount_of_groups = len(year_of_study['groups'])

    # assigning group variable
    group = year_of_study['groups'][0]

    # assigning departaments to variable
    deps = data['scintific_and_educational'][0]['departments']

    # forming dictionary of parameters to give
    # it as third argument to render function
    # for ITMO page
    dict_ITMO = {'name': name, 'head': [head_name, head_surname],
            'adress': {'index': index, 'city': city, 'adress': adress},
            'ad_amount': ad_amount,
            'sc_amount': sc_amount,
            'mf_amount': mf_amount,
            'dep_amount': dep_amount}

    # forming dictionary of parameters to give
    # it as third argument to render function
    # for discipline page
    dict_disc = {'edp_id': edp_id,
                 'edp_name': edp_name,
                 'dis_name': dis_name,
                 'year_of_study': year_of_study,
                 'amount_of_groups': amount_of_groups}

    # forming dictionary of parameters to give
    # it as third argument to render function
    # for group page
    dict_group = {'group': group}

    # forming dictionary of parameters to give
    # it as third argument to render function
    # for departaments page
    dict_deps = {'departaments': deps}

    # forming dictionary of parameters to give
    # it as third argument to render function
    # for university structure page
    dict_uni = {'administrative': administrative}
    dict_uni.update(dict_deps)
    dict_uni.update(dict_ITMO)


# view function for making default page appearance
def index(request):
    return HttpResponse("Hello, world!")

# view function for making hello page appearance
def indexRender(request):
    return render(request, 'index.html', {})

# view function for making ITMO page appearance
def ITMO_University(request):
    return render(request, 'universityInfo.html', dict_ITMO)

# view function for making disc page appearance
def disc(request):
    return render(request, 'disciplineInfo.html', dict_disc)

# view function for making group info page
def group(request):
    return render(request, 'groupsInfo.html', dict_group)

# view function for making departamen info page
def deps(request):
    return render(request, 'departamentsInfo.html', dict_deps)

# view function for making university structure page
def ITMO_structure(request):
    return render(request, 'universityStructure.html', dict_uni)