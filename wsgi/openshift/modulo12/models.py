# -*- coding: utf-8 -*-
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=80)
    class Meta:
        db_table = 'auth_group'

class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')
    class Meta:
        db_table = 'auth_group_permissions'

class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100)
    class Meta:
        db_table = 'auth_permission'

class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField()
    is_superuser = models.BooleanField()
    username = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=75)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    login = models.CharField(max_length=5)
    class Meta:
        db_table = 'auth_user'

class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)
    class Meta:
        db_table = 'auth_user_groups'

class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)
    class Meta:
        db_table = 'auth_user_user_permissions'

class DemoCliente(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=200)
    apellidos = models.CharField(max_length=200)
    status = models.BooleanField()
    class Meta:
        db_table = 'demo_cliente'

class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)
    action_time = models.DateTimeField()
    user = models.ForeignKey(AuthUser)
    content_type = models.ForeignKey('DjangoContentType', null=True, blank=True)
    object_id = models.TextField(blank=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    class Meta:
        db_table = 'django_admin_log'

class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    class Meta:
        db_table = 'django_content_type'

class DjangoSession(models.Model):
    session_key = models.CharField(max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()
    class Meta:
        db_table = 'django_session'

class DjangoSite(models.Model):
    id = models.IntegerField(primary_key=True)
    domain = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    class Meta:
        db_table = 'django_site'

class Docentes(models.Model):
    id_docente = models.AutoField(primary_key=True)
    cedula = models.CharField(max_length=10)
    nombres = models.CharField(max_length=50, blank=True)
    apellidos = models.CharField(max_length=50, blank=True)
    titulo_tn = models.CharField(max_length=50, blank=True)
    titulos_cn = models.CharField(max_length=100, blank=True)
    telefono = models.CharField(max_length=20, blank=True)
    direccion = models.CharField(max_length=50, blank=True)
    email = models.CharField(max_length=20, blank=True)
    foto = models.CharField(max_length=10, blank=True)
    hojavida = models.CharField(max_length=10, blank=True)
    cod_dedicacion = models.CharField(max_length=5, blank=True)
    cod_designacion = models.CharField(max_length=5, blank=True)
    class Meta:
        db_table = 'docentes'

    def __unicode__(self):
        return "%s  -  %s %s"%(self.cedula, self.apellidos, self.nombres)

class LogModels(models.Model):
    id_log_models = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey(AuthUser, db_column='id_usuario')
    id_model = models.CharField(max_length=10)
    nombre_modelo = models.CharField(max_length=50)
    accion = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=50)
    valor_nuevo = models.CharField(max_length=500)
    valor_antiguo = models.CharField(max_length=500)
    dia = models.DateField()
    hora = models.CharField(max_length=10)
    class Meta:
        db_table = 'log_models'

class LogUsuarios(models.Model):
    id_log_usuario = models.AutoField(primary_key=True)
    id_usuario = models.CharField(max_length=10)
    passw = models.CharField(max_length=128)
    nombre_usuario = models.CharField(max_length=50)
    es_super_usuario = models.BooleanField()
    primer_nombre = models.CharField(max_length=50)
    segundo_nombre = models.CharField(max_length=50)
    email = models.CharField(max_length=30)
    estado_login = models.CharField(max_length=10)
    tipo_login = models.CharField(max_length=20)
    activo = models.BooleanField()
    dia = models.DateField()
    hora = models.CharField(max_length=10)
    ip = models.CharField(max_length=20)
    class Meta:
        db_table = 'log_usuarios'

class MatEstudiantes(models.Model):
    id_estudiante = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    ci = models.CharField(max_length=10)
    telefono = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    estado = models.BooleanField(null=False, blank=True)
    class Meta:
        db_table = 'mat_estudiantes'
    def __unicode__(self):
        return self.ci

class MtgTabCorrecciones(models.Model):
    id_correccion = models.AutoField(primary_key=True)
    id_fases_desarrollo = models.ForeignKey('MtgTabFasesdesarrollo', db_column='id_fases_desarrollo')
    fecha = models.DateField()
    correccion = models.TextField(max_length=2000, blank=True)
    correjido_por = models.CharField(max_length=100, blank=True)
    enviar_correccion = models.BooleanField(default=True)
    class Meta:
        db_table = 'mtg_tab_correcciones'

class MtgTabDatgenTgrado(models.Model):
    id_trab_grado = models.AutoField(primary_key=True)
    tema = models.CharField(max_length=100, blank=True)
    id_estudiante = models.ForeignKey(MatEstudiantes, db_column='id_estudiante')
    id_docente = models.ForeignKey(Docentes, db_column='id_docente')
    area_investigacion = models.CharField(max_length=200, blank=True)
    entidad_auspicia = models.CharField(max_length=100, blank=True)
    direccion_autor = models.CharField(max_length=100, blank=True)
    telefono_autor = models.CharField(max_length=10, blank=True)
    correo_electronico = models.CharField(max_length=100, blank=True)
    presupuesto = models.IntegerField(null=True, blank=True)
    direccion_trabajo = models.CharField(max_length=100, blank=True)
    telefono_trabajo = models.CharField(max_length=10, blank=True)
    investigacion = models.CharField(max_length=10, blank=True)
    director = models.CharField(max_length=100, blank=True)
    class Meta:
        db_table = 'mtg_tab_datgen_tgrado'

class MtgTabDefensa(models.Model):
    id_defensa = models.AutoField(primary_key=True)
    id_jurado = models.ForeignKey('MtgTabJurados', db_column='id_jurado')
    id_version = models.ForeignKey('MtgTabVersionamiento', db_column='id_version')
    fecha_defensa = models.DateField(null=True, blank=True)
    aprobacion = models.BooleanField(max_length=5, blank=True,default=False)
    correccion = models.TextField(max_length=1000, blank=True)
    resolucion = models.TextField(max_length=10000, blank=True)
    class Meta:
        db_table = 'mtg_tab_defensa'

class MtgTabDesarrollodefases(models.Model):
    id_desarrollo = models.AutoField(primary_key=True)
    id_fases_desarrollo = models.ForeignKey('MtgTabFasesdesarrollo', db_column='id_fases_desarrollo')
    desarrollo = models.TextField(max_length=2000, blank=True)
    fecha_desarrollo = models.DateField(null=True, blank=True)
    enviar_a_corregir = models.BooleanField(default=True)
    class Meta:
        db_table = 'mtg_tab_desarrollodefases'

class MtgTabFases(models.Model):
    id_fase = models.AutoField(primary_key=True)
    descripcion_fase = models.CharField(max_length=100, blank=True)
    lineamientos = models.TextField(max_length=500, blank=True)
    class Meta:
        db_table = 'mtg_tab_fases'

class MtgTabFasesdesarrollo(models.Model):
    id_fases_desarrollo = models.AutoField(primary_key=True)
    id_version = models.ForeignKey('MtgTabVersionamiento', db_column='id_version')
    id_fase = models.ForeignKey(MtgTabFases, db_column='id_fase')
    estado = models.CharField(max_length=1, blank=True)
    class Meta:
        db_table = 'mtg_tab_fasesdesarrollo'

class MtgTabJurados(models.Model):
    id_jurado = models.AutoField(primary_key=True)
    jurado1 = models.CharField(max_length=100, blank=True)
    jurado2 = models.CharField(max_length=100, blank=True)
    jurado3 = models.CharField(max_length=100, blank=True)
    secretario_abogado = models.CharField(max_length=100, blank=True)
    class Meta:
        db_table = 'mtg_tab_jurados'
    def __unicode__(self):
        return "%s - %s, %s, %s"%(self.id_jurado,self.jurado1, self.jurado2, self.jurado3)

class MtgTabVersionamiento(models.Model):
    id_version = models.AutoField(primary_key=True)
    id_trab_grado = models.ForeignKey(MtgTabDatgenTgrado, db_column='id_trab_grado')
    fecha = models.DateField(null=True, blank=True)
    class Meta:
        db_table = 'mtg_tab_versionamiento'

class Padres(models.Model):
    id_padre = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40)
    class Meta:
        db_table = 'padres'

class Hijos(models.Model):
    id_hijo = models.AutoField(primary_key=True)
    id_padre = models.ForeignKey('Padres', db_column='id_padre')
    nombre = models.CharField(max_length=20)
    class Meta:
        db_table = 'hijos'