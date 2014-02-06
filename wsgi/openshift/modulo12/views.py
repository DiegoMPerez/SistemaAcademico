# Create your views here.
from _threading_local import local
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
from django.forms.formsets import formset_factory
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from pyanaconda import users
from modulo12.models import *
from modulo12.forms import *
from django.contrib.auth import login, logout, authenticate, user_logged_in, user_logged_out, user_login_failed
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
    fases = MtgTabFases.objects.all().order_by('id_fase')
    ctx = {"estudiante":est, "fases":fases}
    return render_to_response('modulo12/EstudianteDetalle.html',ctx, RequestContext(request))

def definicionView(request, id_e, id_f):
    faseN = int(id_f)
    estudianteN = int(id_e)
    estudiante = MatEstudiantes.objects.get(ci=estudianteN)
    fase = MtgTabFases.objects.get(id_fase=id_f)
    lineamineto = MtgTabFases.objects.get(id_fase=id_f)
    defTrabFormSet = inlineformset_factory(MatEstudiantes, MtgTabDatgenTgrado,extra=1, max_num=1)

    if faseN == 1:
        existe = False
        try:
            definicion = MtgTabDatgenTgrado.objects.get(ci=estudianteN)
            version = MtgTabVersionamiento.objects.get(id_trab_grado=definicion.id_trab_grado)
            existe = True
        except:
            existe = False

        if existe:
            if request.method == "POST":
                formSet = fase1Form(request.POST, instance=definicion)
                if formSet.is_valid():
                    formSet.save()
                    return HttpResponseRedirect('/estudiantes/'+id_e+'/desarrollo/')
            else:
                form = fase1Form(instance=definicion)
                ctx = {'formulario':form, "id_e":id_e, "id_f":fase, "fecha":version.fecha}
                return render_to_response("modulo12/fase1.html", ctx, RequestContext(request))
        else:
            if request.method == "POST":
                formSet = defTrabFormSet(request.POST, instance= estudiante)
                if formSet.is_valid():
                    formSet.save()
                    return HttpResponseRedirect('/estudiantes/'+id_e+'/desarrollo/')
            else:
                formSet = defTrabFormSet(instance= estudiante)
            ctx = {'formulario':formSet,"id_e":id_e,"id_f":fase}
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
        try:
            estudiante = MatEstudiantes.objects.get(ci=id_e)
        except:
            return HttpResponseRedirect('/estudiantes/')
        if request.method == "POST":
            form = defensaForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/')
        else:
            form = defensaForm(initial=[{'correccion':'ssss'}][0])
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


###



_thread_locals = local()


def get_current_request():
    """ returns the request object for this thead """
    return getattr(_thread_locals, "request", None)


def get_current_user():
    """ returns the current user, if exist, otherwise returns None """
    request = get_current_request()
    if request:
        return getattr(request, "User", None)


class ThreadLocalMiddleware(object):
    """ Simple middleware that adds the request object in thread local storage."""
    def process_request(self, request):
        _thread_locals.request = request
##


@receiver(post_save, sender=MtgTabFases)
def print_name(sender, instance, using, **kwargs):
        op = instance
        # for f in op.__class__._meta.fields:
        #    print getattr(op,f.name)
        #
        # print getattr(op,op.__class__._meta.fields[0].name)

@receiver(post_save, sender=MtgTabDatgenTgrado)
def do_Vers_Log(sender, instance, created, **kwargs):
    if created:
        op = instance
        vers_id = getattr(op,op.__class__._meta.fields[0].name)
        TrabGrado = MtgTabDatgenTgrado.objects.get(id_trab_grado=vers_id)
        versInst = MtgTabVersionamiento()
        versInst.id_trab_grado = TrabGrado
        versInst.fecha = hoydia()
        versInst.save()


def do_loginIn(sender, user, request, **kwargs):
    userInstance = AuthUser.objects.get(username=user)
    logUsuario = LogUsuarios()
    logUsuario.id_usuario = userInstance.id
    logUsuario.passw = userInstance.password
    logUsuario.nombre_usuario = user
    logUsuario.es_super_usuario = userInstance.is_superuser
    logUsuario.primer_nombre = userInstance.first_name
    logUsuario.segundo_nombre = userInstance.last_name
    logUsuario.email = userInstance.email
    logUsuario.estado_login = userInstance.is_active
    logUsuario.tipo_login = "log_in"
    logUsuario.dia = hoydia()
    logUsuario.hora = hoyhora()
    logUsuario.save()

    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    print(ip)

user_logged_in.connect(do_loginIn)

def do_login_failed(sender, **kwargs):
    print(sender)


user_login_failed.connect(do_login_failed)


def do_loginOut(sender, user, request, **kwargs):
    userInstance = AuthUser.objects.get(username=user)
    logUsuario = LogUsuarios()
    logUsuario.id_usuario = userInstance.id
    logUsuario.passw = userInstance.password
    logUsuario.nombre_usuario = user
    logUsuario.es_super_usuario = userInstance.is_superuser
    logUsuario.primer_nombre = userInstance.first_name
    logUsuario.segundo_nombre = userInstance.last_name
    logUsuario.email = userInstance.email
    logUsuario.estado_login = userInstance.is_active
    logUsuario.tipo_login = "log_in"
    logUsuario.dia = hoydia()
    logUsuario.hora = hoyhora()
    logUsuario.save()

user_logged_out.connect(do_loginOut)



#######################################  CAPTURA DE LA IP   ###############


#######################$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

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