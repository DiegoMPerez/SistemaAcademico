# Create your views here.
from imaplib import _Authenticator
import datetime
import user
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.core.context_processors import csrf, request
from django.core.urlresolvers import reverse
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.forms.models import inlineformset_factory
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

from modulo12.models import *
from modulo12.forms import *
from django.contrib.auth import login, logout, authenticate, user_logged_in
from django.contrib.auth.models import User


##########################################  LOGIN  #######################################################
def loginView(request):
    mensaje=""
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
                    return HttpResponseRedirect('/')
            else:
                mensaje = "USUARIO O PASSWORD INCORRECTOS "
        form = LoginForm()
        #print(user.f.name)
        ctx = {'form':form, 'mensaje':mensaje}
        return render_to_response('modulo12/login.html',ctx,RequestContext(request))

def logoutView(request):
    logout(request)
    return HttpResponseRedirect('/')

def acercaDe_View(request):
    usuario = 'diego'
    try:
        admin = User.objects.get(username__exact='diego')
    except:
        usuario = 'no'
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
    #desarrolloEstudiante =
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
    estudianteN = int(id_e)
    fase = MtgTabFases.objects.get(id_fase=id_f)
    lineamineto = MtgTabFases.objects.get(id_fase=id_f)
    if faseN == 1:
        existe = False
        try:
            definicion = MtgTabDatgenTgrado.objects.get(ci=id_e)
            existe = True
        except:
            existe = False

        if existe:
            if request.method == "POST":
                form = fase1Form(request.POST, instance=definicion)
                if form.is_valid():
                    form.save()

                    return HttpResponseRedirect('/estudiantes/'+id_e+'/desarrollo/')
            else:
                form = fase1Form(instance=definicion)
                ctx = {'formulario':form,"id_e":id_e,"id_f":fase}
                return render_to_response("modulo12/fase1.html", ctx, RequestContext(request))
        else:
            if request.method == "POST":
                form = fase1Form(request.POST)
                versio = versionamientoForm(request.POST)
                if form.is_valid() and versio.is_valid():
                    form.save()
                    versio.save()
                    return HttpResponseRedirect('/estudiantes/'+id_e+'/desarrollo/')
            else:
                form = fase1Form()
                ctx = {'formulario':form,"id_e":id_e,"id_f":fase}
                return render_to_response("modulo12/fase1.html", ctx, RequestContext(request))

    #FASES  > 1

    elif faseN > 1 and faseN < 13:
        if request.method == "POST":
            form = desarrolloForm(request.POST)
            if form.is_valid():
                form.save()
            return HttpResponseRedirect('/estudiantes/'+id_e+'/desarrollo/')
        else:
            form = desarrolloForm()
        ctx = {'formulario':form,"id_e":id_e,"id_f":fase,"lineamiento":lineamineto}
        return render_to_response("modulo12/EstudianteDesarrolloFases.html", ctx,RequestContext(request))
    else:
        return HttpResponseRedirect('/estudiantes/'+id_e+'/desarrollo/')



#######################################     DEFENSA         ##################################################

def defensaView(request, id_e):
    if request.user.is_authenticated():
        estudiante = MatEstudiantes.objects.get(ci=id_e)
        if request.method == "POST":
            form = defensaForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/')
        else:
            form = defensaForm()
        ctx = {"formulario":form, "id_e":estudiante}
        return render_to_response("modulo12/defensa.html", ctx, RequestContext(request))
    else:
        return HttpResponse("No puede votar en esta encuesta.")

###########################################  SENALES   #####################################################

@login_required
def fasesView(request):
    if request.method == "POST":
        formulario = fasesForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/')
    else:
        formulario = fasesForm()
    ctx = {"formulario":formulario}
    return render_to_response("modulo12/fases.html", ctx, RequestContext(request))

def faseGuardada(sender, **kwargs):

    print("%s  %s %s"%(hoydia(),hoyhora()))

@receiver(post_save, sender=MtgTabFases)
def print_name(sender, instance, **kwargs):
        op = instance

        for f in op.__class__._meta.fields:
            print getattr(op,f.name)


def do_login(sender, user, request, **kwargs):
    print(user.get_username())

user_logged_in.connect(do_login)


def hoydia():
    ahora=datetime.datetime.now()
    hoy=ahora.date()
    return hoy

def hoyhora():
    ahora=datetime.datetime.now()
    hora=ahora.time()
    a_hora=str(hora)
    a_hora=a_hora[:8]
    return a_hora


##################################  registro de usuarios

def main(request):
    return render_to_response('modulo12/main.html', {}, context_instance=RequestContext(request))

def signup(request):
    if request.method == 'POST':  # If the form has been submitted...
        form = SignUpForm(request.POST)  # A form bound to the POST data
        if form.is_valid():  # All validation rules pass

            # Process the data in form.cleaned_data
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            email = form.cleaned_data["email"]
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]

            # At this point, user is a User object that has already been saved
            # to the database. You can continue to change its attributes
            # if you want to change other fields.
            user = User.objects.create_user(username, email, password)
            user.first_name = first_name
            user.last_name = last_name

            # Save new user attributes
            user.save()

            return HttpResponseRedirect('/')  # Redirect after POST
    else:
        form = SignUpForm()

    data = {
        'form': form,
    }
    return render_to_response('modulo12/registro.html', data, context_instance=RequestContext(request))