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

class Docentes(models.Model):
    cedula = models.IntegerField(primary_key=True)
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
        return "DOC. %s   %s"%(self.cedula,self.apellidos)

class MatEstudiantes(models.Model):
    ci = models.CharField(max_length=10,primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    estado = models.BooleanField(null=False , blank=True, default=True)
    class Meta:
        db_table = 'mat_estudiantes'

    def __unicode__(self):
        return "%s  %s  %s"%(self.ci, self.apellido,self.nombre)

class MtgTabCorrecciones(models.Model):
    id_desarrollo = models.ForeignKey('MtgTabDesarrollodefases', primary_key=True, db_column='id_desarrollo')
    fecha = models.DateField()
    correccion = models.CharField(max_length=2000, blank=True)
    correjido_por = models.CharField(max_length=100, blank=True)
    enviar_correccion = models.CharField(max_length=1, blank=True)
    class Meta:
        db_table = 'mtg_tab_correcciones'

class MtgTabDatgenTgrado(models.Model):
    id_trab_grado = models.AutoField(primary_key=True)
    tema = models.CharField(max_length=200, blank=True)
    ci = models.ForeignKey(MatEstudiantes, db_column='ci')
    cedula = models.ForeignKey(Docentes, db_column='cedula')
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
    id_defensa = models.IntegerField(primary_key=True)
    id_jurado = models.ForeignKey('MtgTabJurados', db_column='id_jurado')
    id_version = models.ForeignKey('MtgTabVersionamiento', db_column='id_version')
    fecha_defensa = models.DateField(null=True, blank=True)
    aprobacion = models.CharField(max_length=1, blank=True)
    correccion = models.CharField(max_length=1000, blank=True)
    resolucion = models.CharField(max_length=10000, blank=True)
    class Meta:
        db_table = 'mtg_tab_defensa'

class MtgTabDesarrollodefases(models.Model):
    id_desarrollo = models.AutoField(primary_key=True)
    id_fases_desarrollo = models.ForeignKey('MtgTabFasesdesarrollo', db_column='id_fases_desarrollo')
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
    id_fase = models.ForeignKey(MtgTabFases, db_column='id_fase')
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
    id_version = models.AutoField(primary_key=True)
    id_trab_grado = models.ForeignKey(MtgTabDatgenTgrado, db_column='id_trab_grado', null=True)
    fecha = models.DateField(null=True, blank=True)
    class Meta:
        db_table = 'mtg_tab_versionamiento'

