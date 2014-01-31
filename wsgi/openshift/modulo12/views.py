# Create your views here.
from imaplib import _Authenticator
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from modulo12.models import *
from modulo12.forms import *
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User



##########################################  LOGIN  #######################################################
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
    admin = User.objects.get(username__exact='admin')
    if admin is not None:
        return render_to_response('modulo12/acercaDe.html',RequestContext(request))
    else:
        return HttpResponseRedirect('/login')

##########################  DOCENTE  #####################################################################

def docenteListaEstudiantesView(request):
    listaEstudiantes = MatEstudiantes.objects.all();
    ctx = {'estudiantes':listaEstudiantes}
    return render_to_response('modulo12/DocenteListaEstudiantes.html',ctx, RequestContext(request))

def docenteFasesView(request,id_e):
    est = MatEstudiantes.objects.get(ci=id_e)
    fases = MtgTabFases.objects.all()
    ctx = {"estudiante":est, "fases":fases}
    return render_to_response('modulo12/DocenteEstudianteDetalle.html',ctx, RequestContext(request))

def docenteCorreccionView(request,id_e,id_f):
    estudiante = MatEstudiantes.objects.get(ci=id_e)
    fase = MtgTabFases.objects.get(id_fase=id_f)
    if request.method == "POST":
        form = correccionDocenteForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = correccionDocenteForm()
    ctx = {"formulario":form,"id_e":estudiante,"id_f":fase}
    return render_to_response("modulo12/DocenteCorreccion.html", ctx, RequestContext(request))

#######################################   ESTUDIANTES ##################################################

def estudiantesView(request):
    listaEstudiantes = MatEstudiantes.objects.all();
    ctx = {'estudiantes':listaEstudiantes}
    return render_to_response('modulo12/ListaEstudiantes.html',ctx, RequestContext(request))

def estudianteView(request, id_e):
    est = MatEstudiantes.objects.get(ci=id_e)
    fases = MtgTabFases.objects.all()
    ctx = {"estudiante":est, "fases":fases}
    return render_to_response('modulo12/EstudianteDetalle.html',ctx, RequestContext(request))

def definicionView(request, id_e, id_f):
    faseN = int(id_f)
    fase = MtgTabFases.objects.get(id_fase=id_f)
    if faseN == 1:
        if request.method == "POST":
            form = fase1Form(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/estudiantes/'+id_e+'/desarrollo/')
        else:
            form = fase1Form()
            ctx = {'formulario':form,"id_e":id_e,"id_f":fase}
            return render_to_response("modulo12/fase1.html", ctx, RequestContext(request))
    elif faseN > 1 and faseN < 13:
        if request.method == "POST":
            form = desarrolloForm(request.POST)
            if form.is_valid():
                form.save()
            return HttpResponseRedirect('/estudiantes/'+id_e+'/desarrollo/')
        else:
            form = desarrolloForm()
        ctx = {'formulario':form,"id_e":id_e,"id_f":fase}
        return render_to_response("modulo12/EstudianteDesarrolloFases.html", ctx,RequestContext(request))
    else:
        return HttpResponseRedirect('/estudiantes/'+id_e+'/desarrollo/')



#######################################     DEFENSA         ##################################################

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


