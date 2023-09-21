# I Have created This file -- Debayan
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request, 'index.html')
def analyze(request):
    # Get The text
    djtext = request.GET.get('text' , 'default')
    # Checkbox values

    removepunc =request.GET.get('removepunc' , 'off')
    fullcaps =request.GET.get('fullcaps' , 'off')
    smallcaps =request.GET.get('smallcaps' , 'off')
    newlineremv =request.GET.get('newlineremv' , 'off')
    extraspaceremv =request.GET.get('extraspaceremv' , 'off')
    charcounter =request.GET.get('charcounter' , 'off')

    #check whether removepunc is on
    if removepunc=="on":
        punctuations = '''!()-[];:'"\,<>./?{}@#$%^&*~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose' : "Remove Punctuations" , "analyzed_text": analyzed}
        djtext = analyzed

    # Check whether fullcaps is on or off
    if fullcaps =="on":
        analyzed =""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': "Upper case Generator", "analyzed_text": analyzed}
        return render(request , "analyze.html" , params)
    if smallcaps =="on":
        analyzed =""
        for char in djtext:
            analyzed = analyzed + char.lower()
        params = {'purpose': "Lower case Generator", "analyzed_text": analyzed}
        djtext = analyzed
    if extraspaceremv =="on":
        analyzed = ""
        for index , char in enumerate(djtext):
            if not(djtext[index]==" " and djtext[index+1]==" "):
                analyzed = analyzed + char


        params = {'purpose': "Upper case Generator", "analyzed_text": analyzed}
        djtext = analyzed
        # return render(request, "analyze.html", params)
    # check the charcounter is on or off
    if charcounter =="on":
        analyzed = ""
        count =0
        for char in djtext:
            count = count + 1
            analyzed = count
            params = {'purpose': "Character Counter", "analyzed_text":analyzed}
        djtext = analyzed
    if (newlineremv == "on"):
            analyzed = ""
            for char in djtext:
                if char != "\n" and char != "\r":
                    analyzed = analyzed + char


            params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        # return render(request, "analyze.html", params)

    if (removepunc != "on" and newlineremv != "on" and extraspaceremv != "on" and fullcaps != "on" and smallcaps != "on" and charcounter!="on"):
        return HttpResponse("please select any operation and try again")

    return render(request, 'analyze.html', params)








