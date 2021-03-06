# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models



class Estado(models.Model):
    id_estado = models.IntegerField(primary_key=True)
    estado = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estado'


class Friend(models.Model):
    id_friend = models.IntegerField(primary_key=True)
    email = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'friend'


class Friendproyecto(models.Model):
    id_friend = models.ForeignKey(Friend, models.DO_NOTHING, db_column='id_friend', blank=True, null=True)
    id_proyecto = models.ForeignKey('Proyecto', models.DO_NOTHING, db_column='id_proyecto', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'friendproyecto'


class Genero(models.Model):
    id_genero = models.IntegerField(primary_key=True)
    nombre_genero = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'genero'


class Grupopersonas(models.Model):
    id_grupopersonas = models.IntegerField(primary_key=True)
    grupo = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'grupopersonas'


class Maker(models.Model):
    id_maker = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100, blank=True, null=True)
    birth = models.DateField()
    id_ocupacion = models.ForeignKey('Ocupacion', models.DO_NOTHING, db_column='id_ocupacion', blank=True, null=True)
    id_genero = models.ForeignKey(Genero, models.DO_NOTHING, db_column='id_genero', blank=True, null=True)
    id_photo = models.ForeignKey('Profilephoto', models.DO_NOTHING, db_column='id_photo', blank=True, null=True)
    id_estado = models.ForeignKey(Estado, models.DO_NOTHING, db_column='id_estado', blank=True, null=True)
    id_municipio = models.ForeignKey('Municipio', models.DO_NOTHING, db_column='id_municipio', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'maker'


class Makerproyecto(models.Model):
    id_maker = models.ForeignKey(Maker, models.DO_NOTHING, db_column='id_maker', blank=True, null=True)
    id_proyecto = models.ForeignKey('Proyecto', models.DO_NOTHING, db_column='id_proyecto', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'makerproyecto'


class Municipio(models.Model):
    id_municipio = models.IntegerField(primary_key=True)
    municipio = models.CharField(max_length=80, blank=True, null=True)
    id_estado = models.ForeignKey(Estado, models.DO_NOTHING, db_column='id_estado', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'municipio'


class Ocupacion(models.Model):
    id_ocupacion = models.IntegerField(primary_key=True)
    nombre_ocupacion = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'ocupacion'





class Proyecto(models.Model):
    id_proyecto = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=255)
    problema = models.CharField(max_length=700)
    opinion = models.CharField(max_length=700)
    opinion_publico = models.CharField(max_length=700)
    solucion = models.CharField(max_length=700)
    objetivos = models.CharField(max_length=700)
    funcionando = models.BooleanField()
    id_grupopersonas = models.ForeignKey(Grupopersonas, models.DO_NOTHING, db_column='id_grupopersonas', blank=True, null=True)
    id_rangoedad = models.ForeignKey('Rangoedad', models.DO_NOTHING, db_column='id_rangoedad', blank=True, null=True)
    id_genero = models.ForeignKey(Genero, models.DO_NOTHING, db_column='id_genero', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'proyecto'


class Rangoedad(models.Model):
    id_rangoedad = models.IntegerField(primary_key=True)
    rango_edad = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rangoedad'


