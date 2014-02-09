# -*- coding: utf-8 -*-
# Create your views here.
from _threading_local import local
from imaplib import _Authenticator
import datetime
import user
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.core.context_processors import csrf, request
from django.core.urlresolvers import reverse
from django.db.models.signals import post_save, pre_save, post_delete, pre_delete
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
from cStringIO import StringIO


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
    try:
        est = MatEstudiantes.objects.get(ci=id_e)
        fases = MtgTabFases.objects.all()
        ctx = {"estudiante":est, "fases":fases}
        return render_to_response('modulo12/DocenteEstudianteDetalle.html',ctx, RequestContext(request))
    except:
        error = "ERROR: NO EXISTE EL ESTUDIANTE"
        url = "/docente/estudiantes/"
        ctx = {'error':error,"url":url}
        return render_to_response('modulo12/Error.html',ctx,RequestContext(request))

def docenteCorreccionView(request,id_e,id_f):
    estudiante = MatEstudiantes.objects.get(ci=id_e)
    fase = MtgTabFases.objects.get(id_fase=id_f)
    correccionSetForm = inlineformset_factory(MtgTabFasesdesarrollo,MtgTabCorrecciones,extra=1,max_num=1)
    try:
        defTG = MtgTabDatgenTgrado.objects.get(id_estudiante=estudiante.id_estudiante)
        version = MtgTabVersionamiento.objects.get(id_trab_grado=defTG.id_trab_grado)
        faseD = MtgTabFasesdesarrollo.objects.get(id_version=version.id_version, id_fase=fase.id_fase)
        if request.method == "POST":
            form = correccionSetForm(request.POST,instance=faseD,initial=[{'fecha':hoydia()}])
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/docente/estudiantes/%s/correccion/'%(id_e))
        else:
            form = correccionSetForm(instance=faseD,initial=[{'fecha':hoydia()}])
        ctx = {"formulario":form,"id_e":estudiante,"id_f":fase}
        return render_to_response("modulo12/DocenteCorreccion.html", ctx, RequestContext(request))
    except:
        error = "ERROR: NADA PARA CORREGIR"
        url = "/docente/estudiantes/%s/correccion/"%(id_e)
        ctx = {'error':error,"url":url}
        return render_to_response('modulo12/Error.html',ctx,RequestContext(request))





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
    fases = MtgTabFases.objects.all().order_by('id_fase')
    faseN = int(id_f)
    estudianteN = int(id_e)
    estudiante = MatEstudiantes.objects.get(ci=estudianteN)
    formularioEst = estudianteForm()
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
                formSet = fase1Form(request.POST)
                if formSet.is_valid():
                    formSet.save()
                    return HttpResponseRedirect('/estudiantes/'+id_e+'/desarrollo/')
            else:
                form = fase1Form()
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
                formularioEst = estudianteForm()
            ctx = {'formulario':formSet,'fases':fases,'formEstudiante':formularioEst,"estudiante":estudiante,"id_f":fase}
            return render_to_response("modulo12/fase1.html", ctx, RequestContext(request))

    #FASES  > 1

    elif faseN > 1 and faseN < 13:
        desarrolloSetForm = inlineformset_factory(MtgTabFasesdesarrollo,MtgTabDesarrollodefases,extra=1, max_num=1)
        try:
            definicion = MtgTabDatgenTgrado.objects.get(id_estudiante=estudiante.id_estudiante)
        except:
            error = "ERROR: NO EXISTE EL ESTUDIANTE"
            url = "/estudiantes/%s/desarrollo/"%(estudiante.ci)
            ctx = {'error':error,"url":url}
            return render_to_response('modulo12/Error.html',ctx,RequestContext(request))
        version = MtgTabVersionamiento.objects.get(id_trab_grado=definicion.id_trab_grado)
        fase = MtgTabFases.objects.get(id_fase=faseN)
        fasesDesarrollo = MtgTabFasesdesarrollo.objects.get(id_fase=fase.id_fase,id_version=version.id_version)
        if request.method == "POST":
            setForm = desarrolloSetForm(request.POST,instance=fasesDesarrollo, initial=[{'fecha_desarrollo':hoydia()}])
            if setForm.is_valid():
                setForm.save()
                return HttpResponseRedirect('/estudiantes/'+id_e+'/desarrollo/')
        else:
            setForm = desarrolloSetForm(instance= fasesDesarrollo, initial=[{'fecha_desarrollo':hoydia()}])
        ctx = {'formulario':setForm,"id_e":id_e,"id_f":fase,"lineamiento":lineamineto}
        return render_to_response("modulo12/EstudianteDesarrolloFases.html", ctx,RequestContext(request))
    else:
        return HttpResponseRedirect('/estudiantes/'+id_e+'/desarrollo/')



#######################################     DEFENSA         ##################################################

def defensaView(request, id_e):
    defensaSetForm = inlineformset_factory(MtgTabVersionamiento,MtgTabDefensa,extra=1, max_num=1)
    try:
        estudiante = MatEstudiantes.objects.get(ci=id_e)
        defTG = MtgTabDatgenTgrado.objects.get(id_estudiante=estudiante.id_estudiante)
        version = MtgTabVersionamiento.objects.get(id_trab_grado=defTG.id_trab_grado)
        print(version.id_version)
    except:
        error = "ERROR: NO EXISTE EL ESTUDIANTE"
        url = "/estudiantes/"
        ctx = {'error':error,"url":url}
        return render_to_response('modulo12/Error.html',ctx,RequestContext(request))
    if request.method == "POST":
        form = defensaSetForm(request.POST, instance=version,initial=[{'fecha_defensa':hoydia()}])
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = defensaSetForm(instance=version,initial=[{'fecha_defensa':hoydia()}])
    ctx = {"formulario":form, "id_e":estudiante}
    return render_to_response("modulo12/defensa.html", ctx, RequestContext(request))



def juradosView(request):
    if request.method == "POST":
        formulario = juradoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/estudiantes/')
    else:
        formulario = juradoForm()
    ctx = {'formulario':formulario}
    return render_to_response('modulo12/jurados.html',ctx, RequestContext(request))


#######################   FASES       #########################################################
@login_required
def fasesAddView(request):
    if request.method == "POST":
        formulario = fasesForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/fases/lista/')
    else:
        formulario = fasesForm()
    ctx = {"formulario":formulario}
    return render_to_response("modulo12/Fases_Add.html", ctx, RequestContext(request))

def fasesEditView(request, id_f):
    faseInstance = MtgTabFases.objects.get(id_fase=id_f)
    if request.method == "POST":
        formulario = fasesForm(request.POST,instance = faseInstance)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/fases/lista')
    else:
        formulario = fasesForm(instance = faseInstance)
    ctx = {"formulario":formulario, 'id_f':id_f}
    return render_to_response("modulo12/Fases_Add.html", ctx, RequestContext(request))

def fasesElimView(request,id_f):
    faseInstance = MtgTabFases.objects.get(id_fase=id_f)
    faseInstance.delete()
    return HttpResponseRedirect('/fases/lista')

def fasesView(request):
    fases = MtgTabFases.objects.all().order_by('id_fase')
    ctx = {'fases':fases}
    return render_to_response('modulo12/Fases_List.html',ctx,RequestContext(request))


#######################   AUDITORIA   #####################################################

def auditoriaUsuariosView(request):
    if str(request.user) == 'auditor':
        formulario = LogUsuarios.objects.all().order_by('id_log_usuario')
        ctx = {'formulario':formulario}
        return render_to_response('modulo12/AuditoriaUsuarios.html',ctx, RequestContext(request))
    else:
        error = "ERROR: NECESITA SER USUARIO AUDITOR"
        url = "/accounts/login/"
        return ERROR(request,error,url)


def ERROR (request,error,url):
    ctx = {'error':error,"url":url}
    return render_to_response('modulo12/Error.html',ctx,RequestContext(request))

def auditoriaModelosView(request):
    if str(request.user) == 'auditor':
        formulario = LogModels.objects.all().order_by('id_log_models')
        ctx = {'formulario':formulario}
        return render_to_response('modulo12/AuditoriaModelos.html',ctx, RequestContext(request))
    else:
        error = "ERROR: NECESITA SER USUARIO AUDITOR"
        url = "/accounts/login/"
        return ERROR(request,error,url)

###########################################  SENALES   #####################################################

def getUserActivo():
    usuarioActivo = AuthUser.objects.get(login="True")
    return usuarioActivo

# LOG  FASES

@receiver(pre_save, sender=MtgTabFases,)
def do_FasesPreSave_Log(sender, instance,update_fields, **kwargs):
    op = instance
    id = getattr(op,op.__class__._meta.fields[0].name)
    i1 = ""
    v1 = ""
    n1 = ""
    i2 = ""
    v2 = ""
    n2 = ""
    try:
        fields = op.__class__._meta.fields
        objetoAnterior = MtgTabFases.objects.get(id_fase=id)
        if objetoAnterior.descripcion_fase != getattr(op,fields[1].name):
            i1 = "descripcion_fase:"
            v1 =  objetoAnterior.descripcion_fase
            n1 =  getattr(op,fields[1].name)
        elif objetoAnterior.lineamientos != getattr(op,op.__class__._meta.fields[2].name):
            i2 = "lineamientos:"
            v2 = objetoAnterior.lineamientos
            n2 = getattr(op,fields[2].name)
        logModel = LogModels()
        logModel.id_usuario = getUserActivo()
        logModel.id_model = str(id)
        logModel.nombre_modelo = "MtgTabFases"
        logModel.accion = "modificado"
        logModel.descripcion = ""
        logModel.valor_nuevo = "[%s ( %s )][%s ( %s )]"%(i1,n1,i2,n2)
        logModel.valor_antiguo = "[%s ( %s )][%s ( %s )]"%(i1,v1,i2,v2)
        logModel.dia = hoydia()
        logModel.hora = hoyhora()
        logModel.save()
    except:
        print("?")


@receiver(post_save, sender=MtgTabFases)
def do_Fases_Log(sender, instance, created,update_fields,raw, **kwargs):
    op = instance
    idFase = getattr(op,op.__class__._meta.fields[0].name)
    logModel = LogModels()
    logModel.id_model = str(idFase)
    logModel.nombre_modelo = "MtgTabFases"
    logModel.descripcion = op
    logModel.dia = hoydia()
    logModel.hora = hoyhora()
    if created:
        logModel.accion = "creado"
        logModel.save()



@receiver(pre_delete, sender=MtgTabFases)
def do_FasesDelete_Log(sender, instance, **kwargs):
    op = instance
    log_reg = {}
    for f in op.__class__._meta.fields:
        valor_nuevo=getattr(op,f.name)
        log_reg[f.name]=valor_nuevo
    id = getattr(op,op.__class__._meta.fields[0].name)
    logModel = LogModels()
    logModel.id_usuario = getUserActivo()
    logModel.id_model = id
    logModel.nombre_modelo = "MtgTabFases"
    logModel.accion = "borrado"
    logModel.descripcion = op
    logModel.valor_nuevo = ""
    logModel.valor_antiguo = log_reg
    logModel.dia = hoydia()
    logModel.hora = hoyhora()
    logModel.save()


@receiver(post_save, sender=MtgTabDatgenTgrado)
def do_DatGeSave_Log(sender, instance, created, **kwargs):
    if created:
        op = instance
        id = getattr(op,op.__class__._meta.fields[0].name)

        TrabGrado = MtgTabDatgenTgrado.objects.get(id_trab_grado=id)
        versInst = MtgTabVersionamiento()
        versInst.id_trab_grado = TrabGrado
        versInst.fecha = hoydia()
        versInst.save()

        logModel = LogModels()
        logModel.id_model = str(id)
        logModel.id_usuario = getUserActivo()
        logModel.nombre_modelo = "MtgTabDatgenTgrado"
        logModel.descripcion = op
        logModel.dia = hoydia()
        logModel.hora = hoyhora()
        logModel.accion = "creado"
        logModel.save()


@receiver(pre_save, sender=MtgTabDatgenTgrado)
def do_DatGeEdit_Log(sender, instance, **kwargs):
    op = instance
    id = getattr(op,op.__class__._meta.fields[0].name)
    i1 = ""
    v1 = ""
    n1 = ""
    i3 = ""
    v3 = ""
    n3 = ""
    i4 = ""
    v4 = ""
    n4 = ""
    i5 = ""
    v5 = ""
    n5 = ""
    i6 = ""
    v6 = ""
    n6 = ""
    i7 = ""
    v7 = ""
    n7 = ""
    i8 = ""
    v8 = ""
    n8 = ""
    i9 = ""
    v9 = ""
    n9 = ""
    i10 = ""
    v10 = ""
    n10 = ""
    i11 = ""
    v11 = ""
    n11 = ""
    i12 = ""
    v12 = ""
    n12 = ""
    i13 = ""
    v13 = ""
    n13 = ""
    try:
        fields = op.__class__._meta.fields
        objetoAnterior = MtgTabDatgenTgrado.objects.get(id_trab_grado=id)
        if objetoAnterior.tema != getattr(op,fields[1].name):
            i1 = "tema:"
            v1 =  objetoAnterior.tema
            n1 =  getattr(op,fields[1].name)
        elif objetoAnterior.id_docente != getattr(op,op.__class__._meta.fields[3].name):
            i3 = "id_docente:"
            v3 = objetoAnterior.id_docente
            n3 = getattr(op,fields[3].name)
        elif objetoAnterior.area_investigacion != getattr(op,op.__class__._meta.fields[4].name):
            i4 = "area_investigacion:"
            v4 = objetoAnterior.area_investigacion
            n4 = getattr(op,fields[4].name)
        elif objetoAnterior.entidad_auspicia != getattr(op,op.__class__._meta.fields[5].name):
            i5 = "entidad_auspicia:"
            v5 = objetoAnterior.entidad_auspicia
            n5 = getattr(op,fields[5].name)
        elif objetoAnterior.direccion_autor != getattr(op,op.__class__._meta.fields[6].name):
            i6 = "direccion_autor:"
            v6 = objetoAnterior.direccion_autor
            n6 = getattr(op,fields[6].name)
        elif objetoAnterior.telefono_autor != getattr(op,op.__class__._meta.fields[7].name):
            i7 = "telefono_autor:"
            v7 = objetoAnterior.telefono_autor
            n7 = getattr(op,fields[7].name)
        elif objetoAnterior.correo_electronico != getattr(op,op.__class__._meta.fields[8].name):
            i8 = "correo_electronico:"
            v8 = objetoAnterior.correo_electronico
            n8 = getattr(op,fields[8].name)
        elif objetoAnterior.presupuesto != getattr(op,op.__class__._meta.fields[9].name):
            i9 = "presupuesto:"
            v9 = objetoAnterior.presupuesto
            n9 = getattr(op,fields[9].name)
        elif objetoAnterior.direccion_trabajo != getattr(op,op.__class__._meta.fields[10].name):
            i10 = "direccion_trabajo:"
            v10 = objetoAnterior.direccion_trabajo
            n10 = getattr(op,fields[10].name)
        elif objetoAnterior.telefono_trabajo != getattr(op,op.__class__._meta.fields[11].name):
            i11 = "telefono_trabajo:"
            v11 = objetoAnterior.telefono_trabajo
            n11 = getattr(op,fields[11].name)
        elif objetoAnterior.investigacion != getattr(op,op.__class__._meta.fields[12].name):
            i12 = "investigacion:"
            v12 = objetoAnterior.investigacion
            n12 = getattr(op,fields[12].name)
        elif objetoAnterior.director != getattr(op,op.__class__._meta.fields[13].name):
            i13 = "director:"
            v13 = objetoAnterior.director
            n13 = getattr(op,fields[13].name)
        logModel = LogModels()
        logModel.id_usuario = getUserActivo()
        logModel.id_model = str(id)
        logModel.nombre_modelo = "MtgTabDatgenTgrado"
        logModel.accion = "modificado"
        logModel.descripcion = ""
        logModel.valor_nuevo = "[%s ( %s )][%s ( %s )][%s ( %s )][%s ( %s )][%s ( %s )][%s ( %s )][%s ( %s )][%s ( %s )][%s ( %s )][%s ( %s )][%s ( %s )][%s ( %s )]"%(i1,n1,i3,n3,i4,n4,i5,n5,i6,n6,i7,n7,i8,n8,i9,n9,i10,n10,i11,n11,i12,n12,i13,n13)
        logModel.valor_antiguo = "[%s ( %s )][%s ( %s )][%s ( %s )][%s ( %s )][%s ( %s )][%s ( %s )][%s ( %s )][%s ( %s )][%s ( %s )][%s ( %s )][%s ( %s )][%s ( %s )]"%(i1,v1,i3,v3,i4,v4,i5,v5,i6,v6,i7,v7,i8,v8,i9,v9,i10,v10,i11,v11,i12,v12,i13,v13)
        logModel.dia = hoydia()
        logModel.hora = hoyhora()
        logModel.save()
    except:
        print("?")


@receiver(post_delete, sender=MtgTabDatgenTgrado)
def do_Fase1Delete_Log(sender, instance, **kwargs):
    op = instance
    log_reg = {}
    for f in op.__class__._meta.fields:
        valor_nuevo=getattr(op,f.name)
        log_reg[f.name] = str(valor_nuevo)

    vers_id = getattr(op,op.__class__._meta.fields[0].name)
    logModel = LogModels()
    logModel.id_model = vers_id
    logModel.id_usuario = getUserActivo()
    logModel.nombre_modelo = "MtgTabDatgenTgrado"
    logModel.accion = "modelo eliminado"
    logModel.descripcion = op
    logModel.valor_antiguo = log_reg
    logModel.valor_nuevo = ""
    logModel.dia = hoydia()
    logModel.hora = hoyhora()
    logModel.save()


@receiver(post_save, sender=MtgTabVersionamiento)
def do_Versionam_Log(sender, instance, created, **kwargs):
    if created:
        op = instance
        vers_id = getattr(op,op.__class__._meta.fields[0].name)
        versInstancia = MtgTabVersionamiento.objects.get(id_version=vers_id)
        fases = MtgTabFases.objects.all()
        for f in fases:
            faseDesarrollo = MtgTabFasesdesarrollo()
            faseDesarrollo.id_version = versInstancia
            faseDesarrollo.id_fase = f
            faseDesarrollo.save()

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
    logUsuario.estado_login = True
    logUsuario.tipo_login = "log_in"
    logUsuario.dia = hoydia()
    logUsuario.hora = hoyhora()
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    logUsuario.ip = ip
    logUsuario.save()
    request.session['0'] = 'bar'
    usuario = AuthUser.objects.get(id=userInstance.id)
    usuario.login = True
    usuario.save()

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
    logUsuario.tipo_login = "log_out"
    logUsuario.dia = hoydia()
    logUsuario.hora = hoyhora()
    logUsuario.save()
    usuario = AuthUser.objects.get(id=userInstance.id)
    usuario.login = False
    usuario.save()

user_logged_out.connect(do_loginOut)

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

def prueba(request):
    return  render_to_response('modulo12/pruebaq.html')