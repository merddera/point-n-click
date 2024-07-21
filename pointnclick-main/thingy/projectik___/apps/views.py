from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from .forms import CommentForm
from .models import CommentFor


def rendermain(request):
    cont = {}
    return render(request, "mainpage.html", cont)


def rendercatalog(request):
    cont = {}
    return render(request, "catalog.html", cont)


def work(coms, request):
    form = CommentForm(request.POST)
    if form.is_valid():
        Date = form.data['inputt']
        coms.comments = coms.comments + Date
        coms.comments = coms.comments + '➥'


def fullfill(massive, com):
    tempvar = ""
    counting = 0
    for i in com.comments:
        tempvar = tempvar + i
        counting = counting + 1
        if i == '➥':
            massive.append(tempvar[:counting - 1])
            tempvar = ""
            counting = 0


@csrf_exempt
def renderdimension1(request):
    cont = {
        'renderer': [], 'id': 0, 'pag': ' ', 'forms': CommentForm()}
    page = 1
    renderer = "pagefordimension1.html"
    if request.method == "GET":
        if page == 1:
            renderer = "pagefordimension1.html"

    if request.method == "POST":
        if page == 1:
            renderer = "pagefordimension1.html"
            comenti = CommentFor.objects.get(related="page1")
            work(comenti, request)

            comenti.save()

            fullfill(cont['renderer'], comenti)
    return render(request, renderer, cont)


@csrf_exempt
def renderdimension2(request):
    cont = {
        'renderer': [], 'id': 0, 'pag': ' ', 'forms': CommentForm()}
    page = 1
    renderer = "pagefordimension2.html"
    if request.method == "POST":
        comenti = CommentFor.objects.get(related="page2")
        work(comenti, request)

        comenti.save()

        fullfill(cont['renderer'], comenti)

    return render(request, renderer, cont)


@csrf_exempt
def renderdimension3(request):
    cont = {
        'renderer': [], 'id': 0, 'pag': ' ', 'forms': CommentForm()}
    renderer = "pagefordimension3.html"
    if request.method == "POST":
        comenti = CommentFor.objects.get(related="page3")
        work(comenti, request)

        comenti.save()

        fullfill(cont['renderer'], comenti)
    return render(request, renderer, cont)


@csrf_exempt
def renderdimension4(request):
    cont = {
        'renderer': [], 'id': 0, 'pag': ' ', 'forms': CommentForm()}
    if request.method == "POST":
        comenti = CommentFor.objects.get(related="page4")
        work(comenti, request)

        comenti.save()

        fullfill(cont['renderer'], comenti)
    return render(request, "pagefordimension4.html", cont)


@csrf_exempt
def renderdimension5(request):
    cont = {
        'renderer': [], 'id': 0, 'pag': ' ', 'forms': CommentForm()}
    if request.method == "POST":
        comenti = CommentFor.objects.get(related="page5")
        work(comenti, request)

        comenti.save()

        fullfill(cont['renderer'], comenti)
    return render(request, "pagefordimension5.html", cont)


@csrf_exempt
def renderdimension6(request):
    cont = {
        'renderer': [], 'id': 0, 'pag': ' ', 'forms': CommentForm()}
    renderer = loader.get_template("pagefordimension1.html")
    if request.method == "POST":
        comenti = CommentFor.objects.get(related="page6")
        work(comenti, request)

        comenti.save()

        fullfill(cont['renderer'], comenti)
    return render(request, "pagefordimension6.html", cont)


@csrf_exempt
def renderdimension7(request):
    cont = {
        'renderer': [], 'id': 0, 'pag': ' ', 'forms': CommentForm()}
    renderer = loader.get_template("pagefordimension1.html")
    if request.method == "POST":
        comenti = CommentFor.objects.get(related="page7")
        work(comenti, request)

        comenti.save()

        fullfill(cont['renderer'], comenti)
    return render(request, "pagefordimension7.html", cont)


@csrf_exempt
def renderdimension8(request):
    cont = {
        'renderer': [], 'id': 0, 'pag': ' ', 'forms': CommentForm()}
    if request.method == "POST":
        comenti = CommentFor.objects.get(related="page8")
        work(comenti, request)

        comenti.save()

        fullfill(cont['renderer'], comenti)
    return render(request, "pagefordimension8.html", cont)


@csrf_exempt
def renderdimension9(request):
    cont = {
        'renderer': [], 'id': 0, 'pag': ' ', 'forms': CommentForm()}
    if request.method == "POST":
        comenti = CommentFor.objects.get(related="page9")
        work(comenti, request)

        comenti.save()

        fullfill(cont['renderer'], comenti)
    return render(request, "pagefordimension9.html", cont)


@csrf_exempt
def renderdimension10(request):
    cont = {
        'renderer': [], 'id': 0, 'pag': ' ', 'forms': CommentForm()}
    if request.method == "POST":
        comenti = CommentFor.objects.get(related="page10")
        work(comenti, request)

        comenti.save()

        fullfill(cont['renderer'], comenti)
    return render(request, "pagefordimension10.html", cont)


@csrf_exempt
def renderdimension11(request):
    cont = {
        'renderer': [], 'id': 0, 'pag': ' ', 'forms': CommentForm()}
    if request.method == "POST":
        comenti = CommentFor.objects.get(related="page11")
        work(comenti, request)

        comenti.save()

        fullfill(cont['renderer'], comenti)
    return render(request, "pagefordimension11.html", cont)


@csrf_exempt
def renderdimension12(request):
    cont = {
        'renderer': [], 'id': 0, 'pag': ' ', 'forms': CommentForm()}
    if request.method == "POST":
        comenti = CommentFor.objects.get(related="page12")
        work(comenti, request)

        comenti.save()

        fullfill(cont['renderer'], comenti)
    return render(request, "pagefordimension12.html", cont)


@csrf_exempt
def renderdimension13(request):
    cont = {
        'renderer': [], 'id': 0, 'pag': ' ', 'forms': CommentForm()}
    if request.method == "POST":
        comenti = CommentFor.objects.get(related="page13")
        work(comenti, request)

        comenti.save()

        fullfill(cont['renderer'], comenti)
    return render(request, "pagefordimension13.html", cont)


@csrf_exempt
def renderdimension14(request):
    cont = {
        'renderer': [], 'id': 0, 'pag': ' ', 'forms': CommentForm()}
    if request.method == "POST":
        comenti = CommentFor.objects.get(related="page14")
        work(comenti, request)

        comenti.save()

        fullfill(cont['renderer'], comenti)
    return render(request, "pagefordimension14.html", cont)


@csrf_exempt
def renderdimension15(request):
    cont = {
        'renderer': [], 'id': 0, 'pag': ' ', 'forms': CommentForm()}
    if request.method == "POST":
        comenti = CommentFor.objects.get(related="page15")
        work(comenti, request)

        comenti.save()

        fullfill(cont['renderer'], comenti)
    return render(request, "pagefordimension15.html", cont)


@csrf_exempt
def renderdimension16a(request):
    cont = {
        'renderer': [], 'id': 0, 'pag': ' ', 'forms': CommentForm()}
    if request.method == "POST":
        comenti = CommentFor.objects.get(related="page16a")
        work(comenti, request)

        comenti.save()

        fullfill(cont['renderer'], comenti)
    return render(request, "pagefordimension16a.html", cont)


@csrf_exempt
def renderdimension16b(request):
    cont = {
        'renderer': [], 'id': 0, 'pag': ' ', 'forms': CommentForm()}
    if request.method == "POST":
        comenti = CommentFor.objects.get(related="page16b")
        work(comenti, request)

        comenti.save()

        fullfill(cont['renderer'], comenti)
    return render(request, "pagefordimension16b.html", cont)


@csrf_exempt
def renderdimension17a(request):
    cont = {
        'renderer': [], 'id': 0, 'pag': ' ', 'forms': CommentForm()}
    if request.method == "POST":
        comenti = CommentFor.objects.get(related="page17a")
        work(comenti, request)

        comenti.save()

        fullfill(cont['renderer'], comenti)
    return render(request, "pagefordimension17a.html", cont)


@csrf_exempt
def renderdimension20(request):
    cont = {
        'renderer': [], 'id': 0, 'pag': ' ', 'forms': CommentForm()}
    if request.method == "POST":
        comenti = CommentFor.objects.get(related="page20")
        work(comenti, request)

        comenti.save()

        fullfill(cont['renderer'], comenti)
    page = 1
    return render(request, "pagefordimension20.html", cont)



"""SECOND COMICS"""

@csrf_exempt
def secondcomics1(request):
    cont = {}
    page = 1
    return render(request, "secondcomics1.html", cont)

@csrf_exempt
def secondcomics2(request):
    cont = {}
    page = 1
    return render(request, "secondcomics2.html", cont)

@csrf_exempt
def secondcomics3(request):
    cont = {}
    page = 1
    return render(request, "secondcomics3.html", cont)

@csrf_exempt
def secondcomics4(request):
    cont = {}
    page = 1
    return render(request, "secondcomics4.html", cont)

@csrf_exempt
def secondcomics5(request):
    cont = {}
    page = 1
    return render(request, "secondcomics5.html", cont)

@csrf_exempt
def secondcomics6(request):
    cont = {}
    page = 1
    return render(request, "secondcomics6.html", cont)

@csrf_exempt
def secondcomics7(request):
    cont = {}
    page = 1
    return render(request, "secondcomics7.html", cont)

@csrf_exempt
def secondcomics8(request):
    cont = {}
    page = 1
    return render(request, "secondcomics8.html", cont)

@csrf_exempt
def secondcomics9(request):
    cont = {}
    page = 1
    return render(request, "secondcomics9.html", cont)

@csrf_exempt
def secondcomics10(request):
    cont = {}
    page = 1
    return render(request, "secondcomics10.html", cont)

@csrf_exempt
def secondcomics11(request):
    cont = {}
    page = 1
    return render(request, "secondcomics11.html", cont)

@csrf_exempt
def secondcomics12(request):
    cont = {}
    page = 1
    return render(request, "secondcomics12.html", cont)

@csrf_exempt
def secondcomics13(request):
    cont = {}
    page = 1
    return render(request, "secondcomics13.html", cont)

@csrf_exempt
def secondcomics14(request):
    cont = {}
    page = 1
    return render(request, "secondcomics14.html", cont)

@csrf_exempt
def secondcomics15(request):
    cont = {}
    page = 1
    return render(request, "secondcomics15.html", cont)

@csrf_exempt
def secondcomics16(request):
    cont = {}
    page = 1
    return render(request, "secondcomics16.html", cont)

@csrf_exempt
def secondcomics17(request):
    cont = {}
    page = 1
    return render(request, "secondcomics17.html", cont)

@csrf_exempt
def secondcomics18(request):
    cont = {}
    page = 1
    return render(request, "secondcomics18.html", cont)

@csrf_exempt
def secondcomics19(request):
    cont = {}
    page = 1
    return render(request, "secondcomics19.html", cont)

@csrf_exempt
def secondcomics20(request):
    cont = {}
    page = 1
    return render(request, "secondcomics20.html", cont)

@csrf_exempt
def secondcomicsEnd(request):
    cont = {}
    page = 1
    return render(request, "secondcomicsEnd.html", cont)