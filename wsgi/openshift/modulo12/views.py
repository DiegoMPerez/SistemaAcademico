# Create your views here.
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from modulo12.models import *
from modulo12.forms import *
from django.contrib.auth import login, logout, authenticate

def loginView(request):
    mensaje = ""
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')
    else:
        if request.method == "POST":
            form = LoginForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                usuario = authenticate(username=username, password=password)
                if usuario is not None and usuario.is_active:
                    login(request,usuario)
                    return HttpResponseRedirect('/acerca')
                else:
                    mensaje = " USUARIO Y PASSWORD INCORRECTO "
        form = LoginForm()
        ctx = {'form':form, 'mensaje':mensaje}
        return render_to_response('modulo12/login.html',ctx,RequestContext(request))

def logoutView(request):
    logout(request)
    return HttpResponseRedirect('/')

def acercaDe_View(request):
    if request.user.is_authenticated():
        return render_to_response('modulo12/acercaDe.html',RequestContext(request))
    else:
        return HttpResponseRedirect('/login')

def estudiantesView(request):
    listaEstudiantes = MatEstudiantes.objects.all();
    ctx = {'estudiantes':listaEstudiantes}
    return render_to_response('modulo12/Docente_listaEs.html',ctx, RequestContext(request))

def definicionView(request):
    if request.method == "POST":
        form = fase1Form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
		form = fase1Form()
    ctx = {}
    ctx.update(csrf(request))
    ctx['formulario'] = form
    return render_to_response("modulo12/fase1.html", ctx)

def defensaView(request):
    if request.method == "POST":
        form = defensaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
		form = defensaForm()
    ctx = {}
    ctx.update(csrf(request))
    ctx['formulario'] = form
    return render_to_response("modulo12/defensa.html", ctx)


def correccionDocenteView(request):
    if request.method == "POST":
        form = correccionDocenteForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
		form = correccionDocenteForm()
    ctx = {}
    ctx.update(csrf(request))
    ctx['formulario'] = form
    return render_to_response("modulo12/defensa.html", ctx)

def desarrolloView(request):
    if request.method == "POST":
        form = desarrolloForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
		form = desarrolloForm()
    ctx = {}
    ctx.update(csrf(request))
    ctx['formulario'] = form
    return render_to_response("modulo12/desarrolloFases.html", ctx)


def estudianteView(request, id_e):
    est = MatEstudiantes.objects.get(ci=id_e)
    ctx = {"estudiante":est}
    return render_to_response('modulo12/detalleEstudiante.html',ctx, RequestContext(request))

def fasesView(request):
    fs = MtgTabFases.objects.all()
    ctx = {"fases":fs}
    return render_to_response('modulo12/detalleEstudiante.html',ctx, RequestContext(request))
