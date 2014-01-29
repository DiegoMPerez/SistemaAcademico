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

class Actividades(models.Model):
    codigo_actividades = models.CharField(max_length=5, primary_key=True)
    actividad = models.CharField(max_length=30, blank=True)
    horas = models.DecimalField(null=True, max_digits=65535, decimal_places=65535, blank=True)
    cedula = models.ForeignKey('Docentes', db_column='cedula')
    id_periodo = models.ForeignKey('PeriodosAcademicos', db_column='id_periodo')
    class Meta:
        db_table = 'actividades'

class Ambiente(models.Model):
    id_ambiente = models.IntegerField(primary_key=True)
    nombreambiente = models.CharField(max_length=80, blank=True)
    class Meta:
        db_table = 'ambiente'

class Areas(models.Model):
    id_area = models.IntegerField(primary_key=True)
    nombrearea = models.CharField(max_length=80, blank=True)
    nom_docentes = models.CharField(max_length=100, blank=True)
    nom_carrera = models.CharField(max_length=100, blank=True)
    class Meta:
        db_table = 'areas'

class Asignacion(models.Model):
    codigo_materia_paralelo = models.ForeignKey('MateriasParalelos', null=True, db_column='codigo_materia_paralelo', blank=True)
    numeroespacio = models.ForeignKey('Espacios', null=True, db_column='numeroespacio', blank=True)
    nrodesignacion = models.ForeignKey('DesignacionDia', null=True, db_column='nrodesignacion', blank=True)
    nro = models.IntegerField(primary_key=True)
    class Meta:
        db_table = 'asignacion'

class AsistenciaEstudiantes(models.Model):
    ci = models.ForeignKey('MatEstudiantes', db_column='ci')
    codigo_horario = models.ForeignKey('Horarios', null=True, db_column='codigo_horario', blank=True)
    asistencia = models.CharField(max_length=1, blank=True)
    totalasistidos = models.DecimalField(null=True, max_digits=65535, decimal_places=65535, blank=True)
    fecha = models.DateField(null=True, blank=True)
    class Meta:
        db_table = 'asistencia_estudiantes'

class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=80, unique=True)
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
    username = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=75)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
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

class Bajas(models.Model):
    id_baj = models.IntegerField(primary_key=True)
    objeto_sale = models.ForeignKey('Objeto', db_column='objeto_sale')
    objeto_entra = models.ForeignKey('Objeto', null=True, related_name='Objeto1',db_column='objeto_entra', blank=True)
    detalle = models.CharField(max_length=250)
    class Meta:
        db_table = 'bajas'

class Caracteristica(models.Model):
    id_car = models.IntegerField(primary_key=True)
    cod_obj = models.ForeignKey('Objeto', null=True, db_column='cod_obj', blank=True)
    caractersitca = models.CharField(max_length=250)
    detalle_car = models.CharField(max_length=250)
    class Meta:
        db_table = 'caracteristica'

class Carreras(models.Model):
    cod_carrera = models.IntegerField(primary_key=True)
    nombre_carrera = models.CharField(max_length=40, blank=True)
    class Meta:
        db_table = 'carreras'

class Categoria(models.Model):
    id_categoria = models.IntegerField(primary_key=True)
    id_objetivo = models.ForeignKey('Objetivos', null=True, db_column='id_objetivo', blank=True)
    nombrecategoria = models.CharField(max_length=40, blank=True)
    class Meta:
        db_table = 'categoria'

class Compromisos(models.Model):
    id_compromisos = models.IntegerField(primary_key=True)
    id_materiap = models.ForeignKey('Materiaparalelo', null=True, db_column='id_materiap', blank=True)
    compromiso = models.TextField(blank=True)
    class Meta:
        db_table = 'compromisos'

class ConexionModulogestionbiblioteca(models.Model):
    id_bibliografia = models.CharField(max_length=40, primary_key=True)
    codigo_barras_libro = models.ForeignKey('Libros', null=True, db_column='codigo_barras_libro', blank=True)
    id_materiap = models.ForeignKey('Materiaparalelo', null=True, db_column='id_materiap', blank=True)
    class Meta:
        db_table = 'conexion_modulogestionbiblioteca'

class ControlDocumentacion(models.Model):
    cod_control = models.IntegerField(primary_key=True)
    cod_formato_procedimientos = models.ForeignKey('FormatoProcedimientos', null=True, db_column='cod_formato_procedimientos', blank=True)
    class Meta:
        db_table = 'control_documentacion'

class CopiaLibro(models.Model):
    codigo_barras = models.DecimalField(primary_key=True, decimal_places=65535, max_digits=65535)
    copia_numero = models.DecimalField(null=True, max_digits=65535, decimal_places=65535, blank=True)
    titulo = models.CharField(max_length=100, blank=True)
    disponibilidad = models.CharField(max_length=13, blank=True)
    class Meta:
        db_table = 'copia_libro'

class Dedicaciones(models.Model):
    cod_dedicacion = models.CharField(max_length=5, primary_key=True)
    dedicacion = models.CharField(max_length=30, blank=True)
    class Meta:
        db_table = 'dedicaciones'

class DemoCliente(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=200)
    apellidos = models.CharField(max_length=200)
    status = models.BooleanField()
    class Meta:
        db_table = 'demo_cliente'

class DesignacionDia(models.Model):
    nrodesignacion = models.IntegerField(primary_key=True)
    codigo_dia = models.ForeignKey('Dia', null=True, db_column='codigo_dia', blank=True)
    horainicio = models.CharField(max_length=5, blank=True)
    horafin = models.CharField(max_length=5, blank=True)
    class Meta:
        db_table = 'designacion_dia'

class Designaciones(models.Model):
    cod_designacion = models.CharField(max_length=5, primary_key=True)
    designacion = models.CharField(max_length=30, blank=True)
    class Meta:
        db_table = 'designaciones'

class Detalle(models.Model):
    id_det = models.IntegerField(primary_key=True)
    cod_obj = models.ForeignKey('Objeto', db_column='cod_obj')
    id_car = models.ForeignKey(Caracteristica, db_column='id_car')
    class Meta:
        db_table = 'detalle'

class Devoluciones(models.Model):
    codigo_devoluciones = models.DecimalField(primary_key=True, decimal_places=65535, max_digits=65535)
    codigo_prestamo = models.ForeignKey('Prestamos', null=True, db_column='codigo_prestamo', blank=True)
    fecha_devolucion = models.DateField(null=True, blank=True)
    class Meta:
        db_table = 'devoluciones'

class Dia(models.Model):
    codigo_dia = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=10, blank=True)
    class Meta:
        db_table = 'dia'

class Distribucion(models.Model):
    id_dist = models.IntegerField(primary_key=True)
    id_esp = models.ForeignKey('Espacio', db_column='id_esp')
    cod_obj = models.ForeignKey('Objeto', db_column='cod_obj')
    class Meta:
        db_table = 'distribucion'

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
    session_key = models.CharField(max_length=40, primary_key=True)
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
    cedula = models.DecimalField(primary_key=True, decimal_places=0, max_digits=10)
    nombres = models.CharField(max_length=50, blank=True)
    apellidos = models.CharField(max_length=50, blank=True)
    titulo_tn = models.CharField(max_length=50, blank=True)
    titulos_cn = models.CharField(max_length=100, blank=True)
    telefono = models.CharField(max_length=20, blank=True)
    direccion = models.CharField(max_length=50, blank=True)
    email = models.CharField(max_length=20, blank=True)
    foto = models.CharField(max_length=10, blank=True)
    hojavida = models.CharField(max_length=10, blank=True)
    cod_dedicacion = models.ForeignKey(Dedicaciones, null=True, db_column='cod_dedicacion', blank=True)
    cod_designacion = models.ForeignKey(Designaciones, null=True, db_column='cod_designacion', blank=True)
    class Meta:
        db_table = 'docentes'

class Ejesformaciones(models.Model):
    ideje = models.IntegerField(primary_key=True)
    nombreeje = models.CharField(max_length=40, blank=True)
    class Meta:
        db_table = 'ejesformaciones'

class Espacio(models.Model):
    id_esp = models.IntegerField(primary_key=True)
    nom_esp = models.CharField(max_length=100)
    num_esp = models.DecimalField(max_digits=65535, decimal_places=65535)
    tipo_esp = models.CharField(max_length=15)
    desc_esp = models.CharField(max_length=250)
    ubic_esp = models.CharField(max_length=250)
    cap_esp = models.DecimalField(max_digits=65535, decimal_places=65535)
    class Meta:
        db_table = 'espacio'

class Espacios(models.Model):
    cod_espacio = models.ForeignKey('Tipoespacio', null=True, db_column='cod_espacio', blank=True)
    numeroespacio = models.IntegerField(primary_key=True)
    dimesiones = models.IntegerField(null=True, blank=True)
    capacidad = models.IntegerField(null=True, blank=True)
    mesas_sillas = models.IntegerField(null=True, blank=True)
    proyector = models.CharField(max_length=2, blank=True)
    tablero = models.CharField(max_length=2, blank=True)
    ubicacion = models.CharField(max_length=30, blank=True)
    class Meta:
        db_table = 'espacios'

class Estrategias(models.Model):
    id_estrategia = models.IntegerField(primary_key=True)
    nombreestrategia = models.CharField(max_length=80, blank=True)
    class Meta:
        db_table = 'estrategias'

class EstudiantesMaterias(models.Model):
    ci = models.ForeignKey('MatEstudiantes', null=True, db_column='ci', blank=True)
    codmateria = models.ForeignKey('Materias', null=True, db_column='codmateria', blank=True)
    class Meta:
        db_table = 'estudiantes_materias'

class Evaluaciones(models.Model):
    id_evaluaciones = models.IntegerField(primary_key=True)
    id_materiap = models.ForeignKey('Materiaparalelo', null=True, db_column='id_materiap', blank=True)
    id_prueba = models.ForeignKey('Tipoprueba', null=True, db_column='id_prueba', blank=True)
    parcial1 = models.IntegerField(null=True, blank=True)
    parcial2 = models.IntegerField(null=True, blank=True)
    parcial3 = models.IntegerField(null=True, blank=True)
    parcial4 = models.IntegerField(null=True, blank=True)
    parcial5 = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'evaluaciones'

class ExperienciaLaboral(models.Model):
    idlaboral = models.IntegerField(primary_key=True)
    ci = models.ForeignKey('MatEstudiantes', null=True, db_column='ci', blank=True)
    cuidad = models.CharField(max_length=100, blank=True)
    cargo = models.CharField(max_length=100, blank=True)
    fechainicio = models.DateField(null=True, blank=True)
    fechasalida = models.DateField(null=True, blank=True)
    institucion = models.CharField(max_length=100, blank=True)
    tiempo = models.CharField(max_length=1, blank=True)
    pagwebempresa = models.CharField(max_length=100, blank=True)
    descripcioncargo = models.CharField(max_length=50, blank=True)
    class Meta:
        db_table = 'experiencia_laboral'

class Externos(models.Model):
    cedula = models.CharField(max_length=10, primary_key=True)
    foto = models.CharField(max_length=10, blank=True)
    nombres = models.CharField(max_length=30, blank=True)
    apellidos = models.CharField(max_length=30, blank=True)
    direccion = models.CharField(max_length=30, blank=True)
    e_mail = models.CharField(max_length=30, blank=True)
    telefono = models.CharField(max_length=10, blank=True)
    class Meta:
        db_table = 'externos'

class FormacionAcademico(models.Model):
    idformacademica = models.IntegerField(primary_key=True)
    ci = models.ForeignKey('MatEstudiantes', null=True, db_column='ci', blank=True)
    instituto = models.CharField(max_length=100, blank=True)
    titulo = models.CharField(max_length=100, blank=True)
    nivelformacion = models.CharField(max_length=100, blank=True)
    pais = models.CharField(max_length=100, blank=True)
    especialidad = models.CharField(max_length=150, blank=True)
    duraciontitulo = models.CharField(max_length=10, blank=True)
    codregistrosenecyt = models.CharField(max_length=20, blank=True)
    class Meta:
        db_table = 'formacion_academico'

class FormatoActaReunion(models.Model):
    cod_control = models.ForeignKey(ControlDocumentacion, null=True, db_column='cod_control', blank=True)
    cod_formato_acta_reunion = models.IntegerField(primary_key=True)
    nombre_modulo = models.TextField(blank=True)
    fecha = models.DateField(null=True, blank=True)
    hora_inicio = models.TimeField(null=True, blank=True)
    hora_fin = models.TimeField(null=True, blank=True)
    lugar = models.TextField(blank=True)
    autor_convocatoria = models.TextField(blank=True)
    medio_convocatoria = models.TextField(blank=True)
    objetivo = models.TextField(blank=True)
    responsable = models.TextField(blank=True)
    convocados = models.TextField(blank=True)
    agenda_reunion = models.TextField(blank=True)
    temas_tratados = models.TextField(blank=True)
    firman = models.TextField(blank=True)
    class Meta:
        db_table = 'formato_acta_reunion'

class FormatoBaseDatos(models.Model):
    cod_formato_base_datos = models.IntegerField(primary_key=True)
    archivo = models.TextField(blank=True) # This field type is a guess.
    nombre_archivo = models.TextField(blank=True)
    cod_control = models.ForeignKey(ControlDocumentacion, null=True, db_column='cod_control', blank=True)
    class Meta:
        db_table = 'formato_base_datos'

class FormatoHistoria(models.Model):
    cod_historias_usuarios = models.ForeignKey('HistoriasUsuarios', null=True, db_column='cod_historias_usuarios', blank=True)
    cod_formato_historia = models.IntegerField(primary_key=True)
    numero_historia = models.IntegerField(null=True, blank=True)
    usuario = models.TextField(blank=True)
    nombre_historia = models.IntegerField(null=True, blank=True)
    riesgo = models.TextField(blank=True)
    prioridad = models.TextField(blank=True)
    punto_estimado = models.TextField(blank=True)
    iteracion_asignada = models.TextField(blank=True)
    fecha = models.DateField(null=True, blank=True)
    programador_responsable = models.TextField(blank=True)
    descripcion = models.TextField(blank=True)
    observaciones = models.TextField(blank=True)
    class Meta:
        db_table = 'formato_historia'

class FormatoManualUsuario(models.Model):
    cod_control = models.ForeignKey(ControlDocumentacion, null=True, db_column='cod_control', blank=True)
    cod_formato_manual = models.IntegerField(primary_key=True)
    titulo_modulo = models.TextField(blank=True)
    fecha = models.DateField(null=True, blank=True)
    autor = models.TextField(blank=True)
    indice = models.TextField(blank=True)
    introduccion = models.TextField(blank=True)
    dirigido = models.TextField(blank=True)
    requerimientos_sistema = models.TextField(blank=True)
    conexion_desconexion_sistema = models.TextField(blank=True)
    operacion_sistema = models.TextField(blank=True)
    definiciones = models.TextField(blank=True)
    anexos = models.TextField(blank=True)
    class Meta:
        db_table = 'formato_manual_usuario'

class FormatoOficioDesarollo(models.Model):
    cod_formato_oficio_desarollo = models.IntegerField(primary_key=True)
    titulo = models.TextField(blank=True)
    descripcion = models.TextField(blank=True)
    objetivo = models.TextField(blank=True)
    justificacion = models.TextField(blank=True)
    alcanse = models.TextField(blank=True)
    beneficioarios = models.TextField(blank=True)
    relacion_otros_sistemas = models.TextField(blank=True)
    soporte_tecnologico = models.TextField(blank=True)
    estimacion_recursos = models.TextField(blank=True)
    responsable_proyecto = models.TextField(blank=True)
    analisis_riesgo = models.TextField(blank=True)
    cod_control = models.ForeignKey(ControlDocumentacion, null=True, db_column='cod_control', blank=True)
    class Meta:
        db_table = 'formato_oficio_desarollo'

class FormatoOficioSolicitud(models.Model):
    cod_control = models.ForeignKey(ControlDocumentacion, null=True, db_column='cod_control', blank=True)
    cod_formato_oficio_desarollo = models.IntegerField(primary_key=True)
    justificacion = models.TextField(blank=True)
    nombre_software = models.TextField(blank=True)
    licencia = models.TextField(blank=True)
    solicitante = models.TextField(blank=True)
    class Meta:
        db_table = 'formato_oficio_solicitud'

class FormatoPlanificacion(models.Model):
    cod_modulo = models.ForeignKey('Proyectos', null=True, db_column='cod_modulo', blank=True)
    cod_formato_planificacion = models.IntegerField(primary_key=True)
    titulo = models.TextField(blank=True)
    descripcion = models.TextField(blank=True)
    objetivo = models.TextField(blank=True)
    justificacion = models.TextField(blank=True)
    alcanse = models.TextField(blank=True)
    beneficioarios = models.TextField(blank=True)
    relacion_otros_sistemas = models.TextField(blank=True)
    soporte_tecnologico = models.TextField(blank=True)
    estimacion_recursos = models.TextField(blank=True)
    responsable_proyecto = models.TextField(blank=True)
    analisis_riesgo = models.TextField(blank=True)
    class Meta:
        db_table = 'formato_planificacion'

class FormatoProcedimientos(models.Model):
    cod_modulo = models.ForeignKey('Proyectos', null=True, db_column='cod_modulo', blank=True)
    cod_formato_procedimientos = models.IntegerField(primary_key=True)
    id_formato = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'formato_procedimientos'

class FormatoTarea(models.Model):
    cod_formato_tarea = models.IntegerField(primary_key=True)
    cod_tarea = models.ForeignKey('TareasHistorias', null=True, db_column='cod_tarea', blank=True)
    numero_tarea = models.IntegerField(null=True, blank=True)
    numero_historia = models.IntegerField(null=True, blank=True)
    nombre_tarea = models.TextField(blank=True)
    tipo_tarea = models.TextField(blank=True)
    tiempo_estimado = models.IntegerField(null=True, blank=True)
    fecha_inicio = models.DateField(null=True, blank=True)
    fecha_fin = models.DateField(null=True, blank=True)
    programador = models.TextField(blank=True)
    descripcion = models.TextField(blank=True)
    class Meta:
        db_table = 'formato_tarea'

class HistoriasUsuarios(models.Model):
    cod_control = models.ForeignKey(ControlDocumentacion, null=True, db_column='cod_control', blank=True)
    cod_historias_usuarios = models.IntegerField(primary_key=True)
    numero = models.IntegerField(null=True, blank=True)
    nombre_historia = models.TextField(blank=True)
    fecha_inicio = models.DateField(null=True, blank=True)
    fecha_fin = models.DateField(null=True, blank=True)
    duracion_semanas = models.IntegerField(null=True, blank=True)
    duracion_horas = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'historias_usuarios'

class Historicoestudiante(models.Model):
    idhistorico = models.IntegerField(primary_key=True)
    ci = models.ForeignKey('MatEstudiantes', null=True, db_column='ci', blank=True)
    telefono = models.CharField(max_length=50, blank=True)
    direccion = models.CharField(max_length=100, blank=True)
    email = models.CharField(max_length=100, blank=True)
    ciudaactual = models.CharField(max_length=100, blank=True)
    provinciaactual = models.CharField(max_length=100, blank=True)
    class Meta:
        db_table = 'historicoestudiante'

class Horarios(models.Model):
    codigo_horario = models.CharField(max_length=5, primary_key=True)
    dia = models.CharField(max_length=10, blank=True)
    hora_inicio = models.TimeField(null=True, blank=True)
    hora_fin = models.TimeField(null=True, blank=True)
    cedula = models.ForeignKey(Docentes, null=True, db_column='cedula', blank=True)
    codigo_materia_paralelo = models.ForeignKey('MateriasParalelos', null=True, db_column='codigo_materia_paralelo', blank=True)
    id_periodo = models.ForeignKey('PeriodosAcademicos', db_column='id_periodo')
    numero_horas = models.DecimalField(null=True, max_digits=65535, decimal_places=65535, blank=True)
    id_materiap = models.IntegerField()
    class Meta:
        db_table = 'horarios'

class Lectores(models.Model):
    cedula = models.CharField(max_length=10, primary_key=True)
    tipo_lector = models.CharField(max_length=20)
    nombres = models.CharField(max_length=30, blank=True)
    apellidos = models.CharField(max_length=30, blank=True)
    direccion = models.CharField(max_length=30, blank=True)
    e_mail = models.CharField(max_length=30, blank=True)
    telefono = models.CharField(max_length=10, blank=True)
    foto = models.CharField(max_length=10, blank=True)
    class Meta:
        db_table = 'lectores'

class Libros(models.Model):
    codigomfn = models.CharField(max_length=20)
    codigo_barras_libro = models.DecimalField(primary_key=True, decimal_places=65535, max_digits=65535)
    isbn = models.CharField(max_length=30, blank=True)
    autor = models.CharField(max_length=30, blank=True)
    titulo = models.CharField(max_length=100, blank=True)
    ano = models.DecimalField(null=True, max_digits=65535, decimal_places=65535, blank=True)
    fecha_ingreso = models.DateField(null=True, blank=True)
    editorial = models.CharField(max_length=30, blank=True)
    edicion = models.CharField(max_length=30, blank=True)
    descripcion_fisica = models.CharField(max_length=30, blank=True)
    num_paginas = models.DecimalField(null=True, max_digits=65535, decimal_places=65535, blank=True)
    resumen = models.CharField(max_length=50, blank=True)
    descriptores = models.CharField(max_length=50, blank=True)
    disponibilidad = models.CharField(max_length=30, blank=True)
    foto = models.CharField(max_length=10, blank=True)
    class Meta:
        db_table = 'libros'

class MatEstados(models.Model):
    id_estado = models.IntegerField(primary_key=True)
    descripcion = models.TextField(blank=True)
    class Meta:
        db_table = 'mat_estados'

class MatEstudiantes(models.Model):
    ci = models.TextField(primary_key=True)
    cod_carrera = models.ForeignKey(Carreras, null=True, db_column='cod_carrera', blank=True)
    nombre = models.TextField()
    apellido = models.TextField()
    telefono = models.TextField(blank=True)
    direccion = models.TextField(blank=True)
    estado = models.NullBooleanField(null=True, blank=True)
    email = models.TextField(blank=True)
    foto = models.CharField(max_length=254, blank=True)
    tiposangre = models.TextField(blank=True)
    fechagraduacion = models.DateField(null=True, blank=True)
    colegiograduacion = models.TextField(blank=True)
    fechanacimiento = models.DateField(null=True, blank=True)
    notagraduacion = models.IntegerField(null=True, blank=True)
    especialidadgraduacion = models.TextField(blank=True)
    ciudadania = models.TextField(blank=True)
    ciudadnacimiento = models.TextField(blank=True)
    ciudadactual = models.TextField(blank=True)
    provincianacimiento = models.TextField(blank=True)
    provinciaactual = models.TextField(blank=True)
    class Meta:
        db_table = 'mat_estudiantes'
    def __unicode__(self):
        return self.ci

class MatMatriculas(models.Model):
    id_matricula = models.IntegerField(primary_key=True)
    id_periodo = models.ForeignKey('PeriodosAcademicos', null=True, db_column='id_periodo', blank=True)
    ci = models.ForeignKey(MatEstudiantes, null=True, db_column='ci', blank=True)
    codmateria = models.ForeignKey('Materias', null=True, db_column='codmateria', blank=True)
    id_estado = models.ForeignKey(MatEstados, null=True, db_column='id_estado', blank=True)
    nummatricula = models.IntegerField(null=True, blank=True)
    fecha = models.DateField(null=True, blank=True)
    class Meta:
        db_table = 'mat_matriculas'

class MatParametrosMatriculas(models.Model):
    id_param = models.IntegerField(primary_key=True)
    numeromatricula = models.IntegerField()
    numerocreditos = models.IntegerField()
    class Meta:
        db_table = 'mat_parametros_matriculas'

class Materia(models.Model):
    idmaterias = models.IntegerField(primary_key=True)
    idparaleo = models.ForeignKey('Paralelo', null=True, db_column='idparaleo', blank=True)
    idniveles = models.ForeignKey('Niveles', null=True, db_column='idniveles', blank=True)
    cod_carrera = models.ForeignKey(Carreras, null=True, db_column='cod_carrera', blank=True)
    idperiodo = models.ForeignKey('Periodoacademico', null=True, db_column='idperiodo', blank=True)
    cedula = models.ForeignKey(Docentes, null=True, db_column='cedula', blank=True)
    materia = models.CharField(max_length=45, blank=True)
    creditos = models.CharField(max_length=45, blank=True)
    horasprogramdas = models.CharField(max_length=45, blank=True)
    fechacreacion = models.CharField(max_length=45, blank=True)
    estado = models.CharField(max_length=45, blank=True)
    nummatricula = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'materia'

class Materiaparalelo(models.Model):
    id_materiap = models.IntegerField(primary_key=True)
    codmateria = models.ForeignKey('Materias', null=True, db_column='codmateria', blank=True)
    id_periodo = models.ForeignKey('PeriodosAcademicos', null=True, db_column='id_periodo', blank=True)
    id_pre = models.ForeignKey('Prerequisitos', null=True, db_column='id_pre', blank=True)
    nom_docente = models.CharField(max_length=40, blank=True)
    descripcion = models.TextField(blank=True)
    contribucion = models.TextField(blank=True)
    teoria = models.IntegerField(null=True, blank=True)
    practica = models.IntegerField(null=True, blank=True)
    autonomas = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'materiaparalelo'

class Materias(models.Model):
    codmateria = models.CharField(max_length=11, primary_key=True)
    id_area = models.ForeignKey(Areas, null=True, db_column='id_area', blank=True)
    ideje = models.ForeignKey(Ejesformaciones, null=True, db_column='ideje', blank=True)
    nombremateria = models.CharField(max_length=40, blank=True)
    nivel = models.IntegerField(null=True, blank=True)
    creditos = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'materias'

class MateriasParalelos(models.Model):
    codigo_materia_paralelo = models.CharField(max_length=5, primary_key=True)
    codmateria = models.ForeignKey(Materias, db_column='codmateria')
    paralelo = models.CharField(max_length=1)
    numero_estudiantes = models.DecimalField(null=True, max_digits=65535, decimal_places=65535, blank=True)
    cod_carrera = models.ForeignKey(Carreras, db_column='cod_carrera')
    class Meta:
        db_table = 'materias_paralelos'

# ****************************************************************************************************
##########################################################################################################

class MtgTabCorrecciones(models.Model):
    id_desarrollo = models.ForeignKey('MtgTabDesarrollodefases', db_column='id_desarrollo')
    fecha = models.DateField()
    correccion = models.CharField(max_length=2000, blank=True)
    correjido_por = models.CharField(max_length=100, blank=True)
    enviar_correccion = models.CharField(max_length=1, blank=True)
    class Meta:
        db_table = 'mtg_tab_correcciones'

class MtgTabDatgenTgrado(models.Model):
    id_trab_grado = models.AutoField(primary_key=True)
    tema = models.CharField(max_length=100, blank=True)
    ci = models.ForeignKey(MatEstudiantes, null=True, db_column='ci', blank=True)
    cedula = models.ForeignKey(Docentes, null=True, db_column='cedula', blank=True)
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
    id_jurado = models.ForeignKey('MtgTabJurados', null=True, db_column='id_jurado', blank=True)
    id_version = models.ForeignKey('MtgTabVersionamiento', null=False, db_column='id_version', blank=False)
    fecha_defensa = models.DateTimeField(null=True, blank=True)
    aprobacion = models.CharField(max_length=1, blank=True)
    correccion = models.TextField(max_length=1000, blank=True)
    resolucion = models.TextField(max_length=10000, blank=True)
    class Meta:
        db_table = 'mtg_tab_defensa'

class MtgTabDesarrollodefases(models.Model):
    id_desarrollo = models.IntegerField(primary_key=True)
    id_fases_desarrollo = models.ForeignKey('MtgTabFasesdesarrollo', null=True, db_column='id_fases_desarrollo', blank=True)
    desarrollo = models.CharField(max_length=2000, blank=True)
    fecha_desarrollo = models.DateField(null=True, blank=True)
    enviar_a_corregir = models.CharField(max_length=1, blank=True)
    class Meta:
        db_table = 'mtg_tab_desarrollodefases'

class MtgTabFases(models.Model):
    id_fase = models.IntegerField(primary_key=True)
    descripcion_fase = models.CharField(max_length=100, blank=True)
    lineamientos = models.CharField(max_length=500, blank=True)
    class Meta:
        db_table = 'mtg_tab_fases'

class MtgTabFasesdesarrollo(models.Model):
    id_fases_desarrollo = models.IntegerField(primary_key=True)
    id_version = models.ForeignKey('MtgTabVersionamiento', unique=True, db_column='id_version')
    id_fase = models.ForeignKey(MtgTabFases, null=True, db_column='id_fase', blank=True)
    estado = models.CharField(max_length=1, blank=True)
    class Meta:
        db_table = 'mtg_tab_fasesdesarrollo'

class MtgTabJurados(models.Model):
    id_jurado = models.IntegerField(primary_key=True)
    jurado1 = models.CharField(max_length=100, blank=True)
    jurado2 = models.CharField(max_length=100, blank=True)
    jurado3 = models.CharField(max_length=100, blank=True)
    secretario_abogado = models.CharField(max_length=100, blank=True)
    class Meta:
        db_table = 'mtg_tab_jurados'

class MtgTabVersionamiento(models.Model):
    id_version = models.IntegerField(primary_key=True)
    id_trab_grado = models.ForeignKey(MtgTabDatgenTgrado, null=True, db_column='id_trab_grado', blank=True)
    fecha = models.DateField(null=True, blank=True)
    class Meta:
        db_table = 'mtg_tab_versionamiento'



#*********************************************************************************************************
##########################################################################################################
class Multas(models.Model):
    cedula = models.ForeignKey(Lectores, null=True, db_column='cedula', blank=True)
    codigo_barras_libro = models.ForeignKey(Libros, null=True, db_column='codigo_barras_libro', blank=True)
    codigo_barras_tesis = models.ForeignKey('Tesis', null=True, db_column='codigo_barras_tesis', blank=True)
    fecha_multa = models.DateField(null=True, blank=True)
    valormulta = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'multas'

class Nivel(models.Model):
    id_nivel = models.IntegerField(primary_key=True)
    id_categoria = models.ForeignKey(Categoria, null=True, db_column='id_categoria', blank=True)
    nombrenivel = models.CharField(max_length=40, blank=True)
    class Meta:
        db_table = 'nivel'

class Niveles(models.Model):
    idniveles = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=45, blank=True)
    class Meta:
        db_table = 'niveles'

class Notas(models.Model):
    idnotas = models.IntegerField(primary_key=True)
    idmaterias = models.ForeignKey(Materia, null=True, db_column='idmaterias', blank=True)
    notauno = models.DecimalField(null=True, max_digits=65535, decimal_places=65535, blank=True)
    notados = models.DecimalField(null=True, max_digits=65535, decimal_places=65535, blank=True)
    notatres = models.DecimalField(null=True, max_digits=65535, decimal_places=65535, blank=True)
    suma = models.DecimalField(null=True, max_digits=65535, decimal_places=65535, blank=True)
    promedio = models.DecimalField(null=True, max_digits=65535, decimal_places=65535, blank=True)
    aprueba = models.CharField(max_length=1, blank=True)
    class Meta:
        db_table = 'notas'

class Objetivos(models.Model):
    id_objetivo = models.IntegerField(primary_key=True)
    id_materiap = models.ForeignKey(Materiaparalelo, null=True, db_column='id_materiap', blank=True)
    descripcion = models.TextField(blank=True)
    class Meta:
        db_table = 'objetivos'

class Objeto(models.Model):
    cod_obj = models.CharField(max_length=50, primary_key=True)
    nom_obj = models.CharField(max_length=150)
    imagen_obj = models.TextField() # This field type is a guess.
    det_obj = models.CharField(max_length=250)
    marca_obj = models.CharField(max_length=150)
    modelo_obj = models.CharField(max_length=250)
    categoria_obj = models.CharField(max_length=150)
    precio_obj = models.TextField() # This field type is a guess.
    estado_obj = models.CharField(max_length=25)
    operativo_obj = models.BooleanField()
    fech_adquis_obj = models.DateField()
    custodio_obj = models.CharField(max_length=15)
    class Meta:
        db_table = 'objeto'

class Paralelo(models.Model):
    idparaleo = models.IntegerField(primary_key=True)
    paralelo = models.CharField(max_length=1, blank=True)
    class Meta:
        db_table = 'paralelo'

class Periodoacademico(models.Model):
    idperiodo = models.IntegerField(primary_key=True)
    periodoacademico = models.CharField(max_length=45, blank=True)
    fechainicio = models.DateField(null=True, blank=True)
    fechafinal = models.DateField(null=True, blank=True)
    primerbimes = models.DateField(null=True, blank=True)
    segundobimes = models.DateField(null=True, blank=True)
    supletorio = models.DateField(null=True, blank=True)
    periodoactual = models.DateField(null=True, blank=True)
    class Meta:
        db_table = 'periodoacademico'

class PeriodosAcademicos(models.Model):
    id_periodo = models.IntegerField(primary_key=True)
    ciclo = models.CharField(max_length=80, blank=True)
    nombre = models.TextField(blank=True)
    fechainic = models.DateField(null=True, blank=True)
    fechafin = models.DateField(null=True, blank=True)
    fechainian = models.DateField(null=True, blank=True)
    fechafinan = models.DateField(null=True, blank=True)
    fechainiex = models.DateField(null=True, blank=True)
    fechafinex = models.DateField(null=True, blank=True)
    fechainima = models.DateField(null=True, blank=True)
    fechafinma = models.DateField(null=True, blank=True)
    class Meta:
        db_table = 'periodos_academicos'

class Planificaion(models.Model):
    cod_planificaion = models.IntegerField(primary_key=True)
    cod_formato_planificacion = models.ForeignKey(FormatoPlanificacion, null=True, db_column='cod_formato_planificacion', blank=True)
    cod_formato_planificaion = models.IntegerField(null=True, blank=True)
    numero = models.IntegerField(null=True, blank=True)
    nombre = models.TextField(blank=True)
    fecha_inicio = models.DateField(null=True, blank=True)
    fecha_fin = models.DateField(null=True, blank=True)
    duracion = models.TextField(blank=True)
    class Meta:
        db_table = 'planificaion'

class Preguntas(models.Model):
    idpregunta = models.IntegerField(primary_key=True)
    pregunta = models.CharField(max_length=100, blank=True)
    opcion1 = models.CharField(max_length=100, blank=True)
    opcion2 = models.CharField(max_length=100, blank=True)
    opcion3 = models.CharField(max_length=100, blank=True)
    class Meta:
        db_table = 'preguntas'

class Prerequisitos(models.Model):
    id_pre = models.IntegerField(primary_key=True)
    tipo = models.CharField(max_length=40, blank=True)
    codmateria = models.ForeignKey(Materias, null=True, db_column='codmateria', blank=True)
    class Meta:
        db_table = 'prerequisitos'

class Prestamos(models.Model):
    codigo_prestamo = models.DecimalField(primary_key=True, decimal_places=65535, max_digits=65535)
    cedula = models.ForeignKey(Lectores, null=True, db_column='cedula', blank=True)
    codigo_barras_libro = models.ForeignKey(Libros, null=True, db_column='codigo_barras_libro', blank=True)
    codigo_barras_tesis = models.ForeignKey('Tesis', null=True, db_column='codigo_barras_tesis', blank=True)
    fecha_prestamo = models.DateField(null=True, blank=True)
    fecha_debe_devolver = models.DateField(null=True, blank=True)
    class Meta:
        db_table = 'prestamos'

class ProActividades(models.Model):
    id_actividad = models.IntegerField(primary_key=True)
    id_proceso = models.ForeignKey('ProProcesos', null=True, db_column='id_proceso', blank=True)
    actividad = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)
    responsable = models.CharField(max_length=150)
    class Meta:
        db_table = 'pro_actividades'

class ProAnexos(models.Model):
    id_anexo = models.IntegerField(primary_key=True)
    archivo_a = models.TextField(blank=True) # This field type is a guess.
    extension_a = models.CharField(max_length=5, blank=True)
    class Meta:
        db_table = 'pro_anexos'

class ProAnexosReferencias(models.Model):
    id_anex_ref = models.SmallIntegerField(primary_key=True)
    id_anexo = models.ForeignKey(ProAnexos, null=True, db_column='id_anexo', blank=True)
    id_referencia = models.ForeignKey('ProReferencias', null=True, db_column='id_referencia', blank=True)
    id_proceso = models.ForeignKey('ProProcesos', null=True, db_column='id_proceso', blank=True)
    class Meta:
        db_table = 'pro_anexos__referencias'

class ProControlVersiones(models.Model):
    id_control_ver = models.CharField(max_length=10, primary_key=True)
    id_proceso = models.ForeignKey('ProProcesos', null=True, db_column='id_proceso', blank=True)
    fecha = models.DateField()
    version = models.DecimalField(max_digits=3, decimal_places=0)
    realizado_por = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=50)
    class Meta:
        db_table = 'pro_control_versiones'

class ProDefiniciones(models.Model):
    id_definicion = models.IntegerField(primary_key=True)
    id_proceso = models.ForeignKey('ProProcesos', null=True, db_column='id_proceso', blank=True)
    palabra = models.CharField(max_length=25)
    definicion = models.CharField(max_length=300)
    class Meta:
        db_table = 'pro_definiciones'

class ProDiagrama(models.Model):
    id_diagrama = models.SmallIntegerField(primary_key=True)
    id_proceso = models.ForeignKey('ProProcesos', null=True, db_column='id_proceso', blank=True)
    archivo_diag = models.TextField() # This field type is a guess.
    extension_diag = models.CharField(max_length=5)
    class Meta:
        db_table = 'pro_diagrama'

class ProFormatos(models.Model):
    id_formato = models.IntegerField(primary_key=True)
    id_proceso = models.ForeignKey('ProProcesos', null=True, db_column='id_proceso', blank=True)
    archivo_f = models.TextField() # This field type is a guess.
    extensionf = models.CharField(max_length=5)
    class Meta:
        db_table = 'pro_formatos'

class ProProcesos(models.Model):
    id_proceso = models.IntegerField(primary_key=True)
    titulo = models.CharField(max_length=30)
    objetivo = models.CharField(max_length=400)
    campo_aplicacion = models.CharField(max_length=100)
    clientes = models.CharField(max_length=100)
    alcance = models.CharField(max_length=500)
    class Meta:
        db_table = 'pro_procesos'

class ProReferencias(models.Model):
    id_referencia = models.IntegerField(primary_key=True)
    referencia = models.CharField(max_length=250)
    class Meta:
        db_table = 'pro_referencias'

class Proyectos(models.Model):
    nombre_modulo = models.TextField(blank=True)
    cod_modulo = models.IntegerField(primary_key=True)
    fecha_inicio = models.DateField(null=True, blank=True)
    id_usuario1 = models.ForeignKey('UsuUsuarios', null=True,related_name='id_usuario1', db_column='id_usuario1', blank=True)
    id_usuario2 = models.ForeignKey('UsuUsuarios', null=True, db_column='id_usuario2', blank=True)
    class Meta:
        db_table = 'proyectos'

class PrvInstitucione(models.Model):
    ruc = models.CharField(max_length=13, primary_key=True)
    empresa = models.CharField(max_length=50, blank=True)
    direccion = models.CharField(max_length=60, blank=True)
    telefono = models.CharField(max_length=13, blank=True)
    tipo = models.CharField(max_length=12, blank=True)
    numero_estudiantes = models.IntegerField(null=True, blank=True)
    correo = models.CharField(max_length=60, blank=True)
    imagen = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'prv_institucione'

class PrvNota(models.Model):
    ci = models.ForeignKey('PrvVinculacione', primary_key=True, db_column='ci')
    nota1 = models.FloatField(null=True, blank=True)
    nota2 = models.FloatField(null=True, blank=True)
    promedio = models.FloatField(null=True, blank=True)
    aprueba = models.CharField(max_length=2, blank=True)
    class Meta:
        db_table = 'prv_nota'

class PrvPracticante(models.Model):
    ci = models.ForeignKey(MatEstudiantes, primary_key=True, db_column='ci')
    cedula = models.ForeignKey(Docentes, null=True, db_column='cedula', blank=True)
    codigo_carrera = models.CharField(max_length=6, blank=True)
    fecha_inicio = models.DateField(null=True, blank=True)
    fecha_finalizacion = models.DateField(null=True, blank=True)
    codigo_periodo_academico = models.CharField(max_length=30, blank=True)
    ruc = models.ForeignKey(PrvInstitucione, null=True, db_column='ruc', blank=True)
    id_administrativo = models.ForeignKey('UsuAdministrativos', null=True, db_column='id_administrativo', blank=True)
    avance = models.IntegerField(null=True, blank=True)
    estado = models.CharField(max_length=10, blank=True)
    numero_cred_aprobados = models.IntegerField(null=True, blank=True)
    certificado_empresa = models.TextField(blank=True) # This field type is a guess.
    certificado_hcu = models.TextField(blank=True) # This field type is a guess.
    planificacion = models.TextField(blank=True) # This field type is a guess.
    informe_final = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'prv_practicante'

class PrvVinculacione(models.Model):
    ci = models.ForeignKey(MatEstudiantes, primary_key=True, db_column='ci')
    ruc = models.ForeignKey(PrvInstitucione, null=True, db_column='ruc', blank=True)
    id_administrativo = models.ForeignKey('UsuAdministrativos', null=True, db_column='id_administrativo', blank=True)
    codigo_carrera = models.CharField(max_length=10, blank=True)
    fechaini = models.DateField(null=True, blank=True)
    fechafin = models.DateField(null=True, blank=True)
    estado = models.CharField(max_length=10, blank=True)
    codigo_periodo_academico = models.CharField(max_length=10, blank=True)
    numero_cred_aprobados = models.IntegerField(null=True, blank=True)
    certificado_empresa = models.TextField(blank=True) # This field type is a guess.
    planificacion = models.TextField(blank=True) # This field type is a guess.
    informe_final = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'prv_vinculacione'

class Recursos(models.Model):
    id_recursos = models.IntegerField(primary_key=True)
    nombrerecursos = models.CharField(max_length=80, blank=True)
    class Meta:
        db_table = 'recursos'

class Relaciones(models.Model):
    id_relacion = models.IntegerField(primary_key=True)
    id_resultados = models.ForeignKey('Resultadosaprendizaje', null=True, db_column='id_resultados', blank=True)
    id_carrera = models.ForeignKey('Resultadoscarrera', null=True, db_column='id_carrera', blank=True)
    class Meta:
        db_table = 'relaciones'

class RespuestaEstudiantes(models.Model):
    idresp = models.IntegerField(primary_key=True)
    ci = models.ForeignKey(MatEstudiantes, null=True, db_column='ci', blank=True)
    idpregunta = models.ForeignKey(Preguntas, null=True, db_column='idpregunta', blank=True)
    respuesta = models.CharField(max_length=150, blank=True)
    class Meta:
        db_table = 'respuesta_estudiantes'

class Resultadosaprendizaje(models.Model):
    id_resultados = models.IntegerField(primary_key=True)
    excelente = models.TextField(blank=True)
    mbuena = models.TextField(blank=True)
    buena = models.TextField(blank=True)
    regular = models.TextField(blank=True)
    deficiente = models.TextField(blank=True)
    id_materiap = models.ForeignKey(Materiaparalelo, null=True, db_column='id_materiap', blank=True)
    class Meta:
        db_table = 'resultadosaprendizaje'

class Resultadoscarrera(models.Model):
    id_carrera = models.IntegerField(primary_key=True)
    descripcion = models.TextField(blank=True)
    class Meta:
        db_table = 'resultadoscarrera'

class Subtopicos(models.Model):
    id_subtopico = models.IntegerField(primary_key=True)
    id_topico = models.ForeignKey('Topicos', null=True, db_column='id_topico', blank=True)
    id_resultados = models.ForeignKey(Resultadosaprendizaje, null=True, db_column='id_resultados', blank=True)
    id_estrategia = models.ForeignKey(Estrategias, null=True, db_column='id_estrategia', blank=True)
    id_ambiente = models.ForeignKey(Ambiente, null=True, db_column='id_ambiente', blank=True)
    id_recursos = models.ForeignKey(Recursos, null=True, db_column='id_recursos', blank=True)
    id_tics = models.ForeignKey('Tics', null=True, db_column='id_tics', blank=True)
    nrohoras = models.IntegerField(null=True, blank=True)
    horasteoricas = models.IntegerField(null=True, blank=True)
    horaspracticas = models.IntegerField(null=True, blank=True)
    horasautonomas = models.IntegerField(null=True, blank=True)
    porcentaje = models.FloatField(null=True, blank=True)
    class Meta:
        db_table = 'subtopicos'

class TabBeAnuncios(models.Model):
    id_anuncio = models.IntegerField(primary_key=True)
    id_empresa = models.ForeignKey('TabBeEmpresas', db_column='id_empresa')
    ci = models.ForeignKey(MatEstudiantes, db_column='ci')
    id_tecnologia = models.ForeignKey('TabBeTecnologias', db_column='id_tecnologia')
    descripcion = models.CharField(max_length=200)
    fecha_inicio = models.DateField()
    fecha_limite = models.DateField()
    experiencia_previa = models.CharField(max_length=1)
    descripcion_puesto = models.CharField(max_length=100)
    hora = models.TimeField()
    class Meta:
        db_table = 'tab_be_anuncios'

class TabBeEmpresas(models.Model):
    id_empresa = models.IntegerField(primary_key=True)
    razon_social = models.CharField(max_length=50)
    ruc_ci = models.CharField(max_length=13)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=9)
    campo_ocupacional = models.CharField(max_length=50)
    e_mail = models.CharField(max_length=100)
    sitioweb = models.CharField(max_length=20)
    class Meta:
        db_table = 'tab_be_empresas'

class TabBeTecnologias(models.Model):
    id_tecnologia = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=50)
    empresa = models.CharField(max_length=50)
    class Meta:
        db_table = 'tab_be_tecnologias'

class TareasHistorias(models.Model):
    cod_formato_historia = models.ForeignKey(FormatoHistoria, null=True, db_column='cod_formato_historia', blank=True)
    cod_tarea = models.IntegerField(primary_key=True)
    numero_historia = models.IntegerField(null=True, blank=True)
    nombre_historia = models.TextField(blank=True)
    numero_tarea = models.IntegerField(null=True, blank=True)
    nombre_tarea = models.TextField(blank=True)
    tiempo_estimado = models.IntegerField(null=True, blank=True)
    total_horas = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'tareas_historias'

class Tesis(models.Model):
    codigomfn = models.CharField(max_length=20)
    codigo_barras_tesis = models.DecimalField(primary_key=True, decimal_places=65535, max_digits=65535)
    titulo = models.CharField(max_length=100, blank=True)
    autor = models.CharField(max_length=30, blank=True)
    ano = models.DecimalField(null=True, max_digits=65535, decimal_places=65535, blank=True)
    carrera = models.CharField(max_length=30, blank=True)
    director = models.CharField(max_length=30, blank=True)
    descripcion_fisica = models.CharField(max_length=30, blank=True)
    num_paginas = models.DecimalField(null=True, max_digits=65535, decimal_places=65535, blank=True)
    resumen = models.CharField(max_length=30, blank=True)
    descriptores = models.CharField(max_length=30, blank=True)
    disponibilidad = models.CharField(max_length=30, blank=True)
    class Meta:
        db_table = 'tesis'

class Tics(models.Model):
    id_tics = models.IntegerField(primary_key=True)
    nombretics = models.CharField(max_length=80, blank=True)
    class Meta:
        db_table = 'tics'

class Tipoespacio(models.Model):
    cod_espacio = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=20, blank=True)
    class Meta:
        db_table = 'tipoespacio'

class Tipoprueba(models.Model):
    id_prueba = models.IntegerField(primary_key=True)
    prueba = models.CharField(max_length=80, blank=True)
    class Meta:
        db_table = 'tipoprueba'

class Topicos(models.Model):
    id_topico = models.IntegerField(primary_key=True)
    id_materiap = models.ForeignKey(Materiaparalelo, null=True, db_column='id_materiap', blank=True)
    numero = models.IntegerField(null=True, blank=True)
    nombretopico = models.CharField(max_length=100, blank=True)
    class Meta:
        db_table = 'topicos'

class TutActa(models.Model):
    id_acta = models.IntegerField(primary_key=True)
    id_tesis = models.ForeignKey('TutTesis', null=True, db_column='id_tesis', blank=True)
    fecha = models.DateField(null=True, blank=True)
    nota = models.DecimalField(null=True, max_digits=4, decimal_places=2, blank=True)
    class Meta:
        db_table = 'tut_acta'

class TutActividades(models.Model):
    id_actividad = models.IntegerField(primary_key=True)
    id_cronograma = models.ForeignKey('TutCronogramas', null=True, db_column='id_cronograma', blank=True)
    descripcion_actividad = models.CharField(max_length=300, blank=True)
    observaciones = models.CharField(max_length=300, blank=True)
    estado = models.NullBooleanField(null=True, blank=True)
    class Meta:
        db_table = 'tut_actividades'

class TutCronogramas(models.Model):
    id_cronograma = models.IntegerField(primary_key=True)
    cronograma = models.CharField(max_length=300, blank=True)
    class Meta:
        db_table = 'tut_cronogramas'

class TutDefensas(models.Model):
    id_defensa = models.IntegerField(primary_key=True)
    id_tesis = models.ForeignKey('TutTesis', null=True, db_column='id_tesis', blank=True)
    tipo_defensa = models.CharField(max_length=50, blank=True)
    fecha_def = models.DateField(null=True, blank=True)
    observaciones = models.CharField(max_length=300, blank=True)
    nota = models.DecimalField(null=True, max_digits=4, decimal_places=2, blank=True)
    aprobado = models.NullBooleanField(null=True, blank=True)
    class Meta:
        db_table = 'tut_defensas'

class TutJuradosDefensas(models.Model):
    id_jurado = models.IntegerField(primary_key=True)
    cedula = models.ForeignKey(Docentes, null=True, db_column='cedula', blank=True)
    id_defensa = models.ForeignKey(TutDefensas, null=True, db_column='id_defensa', blank=True)
    nota = models.DecimalField(null=True, max_digits=4, decimal_places=2, blank=True)
    class Meta:
        db_table = 'tut_jurados_defensas'

class TutRegArchAvanceTesis(models.Model):
    id_avance = models.IntegerField(primary_key=True)
    id_tesis = models.ForeignKey('TutTesis', null=True, db_column='id_tesis', blank=True)
    id_actividad = models.ForeignKey(TutActividades, null=True, db_column='id_actividad', blank=True)
    id_revision = models.ForeignKey('TutRevAvanceTesis', null=True, db_column='id_revision', blank=True)
    descripcion = models.CharField(max_length=300, blank=True)
    nomb_archivo = models.CharField(max_length=300, blank=True)
    fecha_subida = models.DateField(null=True, blank=True)
    class Meta:
        db_table = 'tut_reg_arch_avance_tesis'

class TutRegistroCorreciones(models.Model):
    id_reg_correccion = models.IntegerField(primary_key=True)
    id_revision = models.ForeignKey('TutRevAvanceTesis', null=True, db_column='id_revision', blank=True)
    correcion = models.CharField(max_length=300, blank=True)
    check = models.NullBooleanField(null=True, db_column='CHECK', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'tut_registro_correciones'

class TutRevAvanceTesis(models.Model):
    id_revision = models.IntegerField(primary_key=True)
    id_tesis = models.ForeignKey('TutTesis', null=True, db_column='id_tesis', blank=True)
    estado = models.NullBooleanField(null=True, blank=True)
    descripcion = models.CharField(max_length=300, blank=True)
    class Meta:
        db_table = 'tut_rev_avance_tesis'

class TutTesis(models.Model):
    id_tesis = models.IntegerField(primary_key=True)
    id_tut_tesis = models.ForeignKey('TutTutoriasTesis', null=True, db_column='id_tut_tesis', blank=True)
    id_acta = models.ForeignKey(TutActa, null=True, db_column='id_acta', blank=True)
    tema_tesis = models.CharField(max_length=300, blank=True)
    pathtesis = models.CharField(max_length=300, blank=True)
    class Meta:
        db_table = 'tut_tesis'

class TutTutorias(models.Model):
    id_tutoria = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=300, blank=True)
    class Meta:
        db_table = 'tut_tutorias'

class TutTutoriasTesis(models.Model):
    id_tut_tesis = models.IntegerField(primary_key=True)
    id_tutoria = models.ForeignKey(TutTutorias, null=True, db_column='id_tutoria', blank=True)
    id_cronograma = models.ForeignKey(TutCronogramas, null=True, db_column='id_cronograma', blank=True)
    cedula = models.ForeignKey(Docentes, null=True, db_column='cedula', blank=True)
    fecha_inicio = models.DateField(null=True, blank=True)
    fecha_fin = models.DateField(null=True, blank=True)
    ci = models.ForeignKey(MatEstudiantes, null=True, db_column='ci', blank=True)
    class Meta:
        db_table = 'tut_tutorias_tesis'

class UsuAdministrativos(models.Model):
    id_administrativo = models.IntegerField(primary_key=True)
    id_rol = models.ForeignKey('UsuRoles', db_column='id_rol')
    cedula = models.CharField(max_length=10)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.CharField(max_length=15)
    difreccion = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    foto = models.TextField(blank=True) # This field type is a guess.
    tipo_sangre = models.CharField(max_length=4)
    fecha_nacimiento = models.DateField()
    ciudadania = models.CharField(max_length=50)
    ciudad_nacimiento = models.CharField(max_length=50)
    provincia_nacimiento = models.CharField(max_length=50)
    class Meta:
        db_table = 'usu_administrativos'

class UsuEventos(models.Model):
    id_evento = models.IntegerField(primary_key=True)
    nombre_evento = models.CharField(max_length=50)
    class Meta:
        db_table = 'usu_eventos'

class UsuPistasAuditoria(models.Model):
    id_pista = models.IntegerField(primary_key=True)
    id_usuario = models.ForeignKey('UsuUsuarios', db_column='id_usuario')
    id_evento = models.ForeignKey(UsuEventos, db_column='id_evento')
    ci = models.ForeignKey(MatEstudiantes, null=True, db_column='ci', blank=True)
    fecha_hora = models.DateTimeField()
    nota1 = models.IntegerField(null=True, blank=True)
    nota2 = models.IntegerField(null=True, blank=True)
    nota3 = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'usu_pistas_auditoria'

class UsuRoles(models.Model):
    id_rol = models.IntegerField(primary_key=True)
    nombre_rol = models.CharField(max_length=50)
    class Meta:
        db_table = 'usu_roles'

class UsuUsuarios(models.Model):
    id_usuario = models.IntegerField(primary_key=True)
    id_rol = models.ForeignKey(UsuRoles, db_column='id_rol')
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    cedula = models.CharField(max_length=10)
    direccion = models.CharField(max_length=50)
    telefono = models.CharField(max_length=15)
    email = models.CharField(max_length=50)
    foto = models.TextField(blank=True) # This field type is a guess.
    usuario = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    class Meta:
        db_table = 'usu_usuarios'

class Verbo(models.Model):
    id_verbo = models.IntegerField(primary_key=True)
    id_nivel = models.ForeignKey(Nivel, null=True, db_column='id_nivel', blank=True)
    nombreverbo = models.CharField(max_length=60, blank=True)
    class Meta:
        db_table = 'verbo'

