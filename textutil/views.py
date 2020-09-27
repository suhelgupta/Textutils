from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,"index.html")

def Analyze(request):
    if request.POST.get('text') == '':
        return HttpResponse("Please write text in textbox <a href='/'>Click here to try again</a>")

    recivetext = request.POST.get('text', 'default')

    removepunc = request.POST.get('removepunc', 'off')
    capall = request.POST.get('fullcaps', 'off')
    capfirst = request.POST.get('capfirst', 'off')
    smallall = request.POST.get('lower', 'off')
    removenline = request.POST.get('rmnewline', 'off')
    extraspaverm = request.POST.get('extspacerm', 'off')
    spaceremove = request.POST.get('allspacerm', 'off')
    countchar = request.POST.get('cntchar', 'off')

    flag = True
    mylist = [removepunc,capall,capfirst, smallall, removenline, extraspaverm, spaceremove, countchar]
    for i in mylist:
        if i == "on":
            flag = False
        


    if(flag):
        return HttpResponse("Please select any services <a href='/'>Click here to try again</a>")

    if removepunc == "on":
        purpos = "Remove Panctuation"
        Analysed = removepuncf(recivetext)
        recivetext = Analysed


    if capfirst == "on":
        purpos = "Capital First word"
        Analysed = capfirstf(recivetext)
        recivetext = Analysed
        
    if capall == "on":
        purpos = "Capital all"
        Analysed = capallf(recivetext)
        recivetext = Analysed

    if smallall == "on":
        purpos = "Small Case all"
        Analysed = smallallf(recivetext)
        recivetext = Analysed

    if removenline == "on":
        purpos = "Remove New Line"
        Analysed = removenlinef(recivetext)
        recivetext = Analysed

    if extraspaverm == "on":
        purpos = "space remover"
        Analysed = extraspavermf(recivetext)
        recivetext = Analysed

    if spaceremove == "on":
        purpos = "Extra space remover"
        Analysed = spaceremovef(recivetext)
        recivetext = Analysed

    if countchar == "on":
        purpos = "Count Character"
        Analysed = countcharf(recivetext)
        recivetext = recivetext + "\n\n" + Analysed
    
    return Analysedtext(request,purpos,recivetext)



def Analysedtext(request,purpos,Analysed):
    params = {'purpose': purpos, 'Analyzed_text': Analysed}
    return render(request, "Analyze.html", params)

def removepuncf(text):
    analys = ""
    panctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~''' # List of Panchuations
    for i in text:
        if i in panctuations:
            continue
        analys += i
    return analys

def capallf(text):
    return text.upper()

def capfirstf(text):
    return text.capitalize()

def smallallf(text):
    return text.lower()

def removenlinef(text):
    anal = ""
    for i in text:
        if i != "\n" and i != "\r":
            anal = anal + i
    return anal

def spaceremovef(text):
    anal = ""
    for i in text:
        if i == " ":
            continue
        anal = anal + i
    return anal

def extraspavermf(text):
    anal = ""
    for i,j in enumerate(text):
        if text[i] == " " and text[i+1] == " ":
            continue
        anal = anal + j
    return anal

def countcharf(text):
    for i,j in enumerate(text):
        pass
    return f"Number Of Character is :- {i+1}"