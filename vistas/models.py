from django.db import models

# Create your models here.

class Rol(models.Model):
    Rol = models.CharField(max_length=50,default=False)
    Descripcion = models.CharField(max_length=100,default=False)

    def __str__(self):
        return "%s the place" % self.name

class Equipo(models.Model):
    nombre_equipo = models.CharField(max_length=50,default=False)
    media = models.CharField(max_length=100,default=False)

    def __str__(self):
        return "%s the equipo" % self.name
        
class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_rol_id = models.OneToOneField(
        Rol,
        on_delete=models.CASCADE
    )
    equipo_id = models.OneToOneField(
        Equipo,
        on_delete=models.CASCADE
    )
    Nombre = models.CharField(max_length=100,default=False)
    ApellidoPaterno = models.CharField(max_length=100,default=False)
    ApellidoPaterno = models.CharField(max_length=100,default=False)
    Birthday = models.DateField()
    Curp = models.CharField(max_length=100,default=False)
    

    def __str__(self):
        return "%s the Users" % self.place.name

class Torneo(models.Model):
    THEME_CHOICES = ((1,"Liguilla"),(2,"Torneo"))
    torneo_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    tipo_de_torneo = models.IntegerField(choices=THEME_CHOICES, unique=True)

    def __str__(self):
        torneo = (self.descripcion,self.tipo )
        return torneo

class Campos(models.Model):
    campo_id = models.AutoField(primary_key=True)
    nombre_campo = models.CharField(max_length=100)
    url = models.CharField(max_length=500)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)
        
class Campos(models.Model):
    campo_id = models.AutoField(primary_key=True)
    nombre_campo = models.CharField(max_length=100)
    url = models.CharField(max_length=500)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

class Partidos(models.Model):
    id_partido = models.AutoField(primary_key=True)
    fecha =  models.DateField(null=True) 
    campos = models.ForeignKey(Campos, on_delete=models.CASCADE,related_name="id_campos")
    visitante = models.ForeignKey(Equipo, on_delete=models.CASCADE,related_name="id_visitante")
    local = models.ForeignKey(Equipo, on_delete=models.CASCADE,related_name="id_local")
    arbitro = models.ForeignKey(Users, on_delete=models.CASCADE,related_name="id_arbitro")
    torneo = models.ForeignKey(Torneo, on_delete=models.CASCADE,related_name="id_toreno")
    status = models.ForeignKey(Torneo, on_delete=models.CASCADE,related_name="id_status_torneo")
    entrenador = models.ForeignKey(Equipo, on_delete=models.CASCADE,related_name="id_entrenador")
    def __str__(self):
        return self.headline

class Gol(models.Model):
    id_amonestacion = models.AutoField(primary_key=True)
    equipo_ganador = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    id_partido = models.ForeignKey(Partidos, on_delete=models.CASCADE) 
    minuto = models.CharField(max_length= 20 ,default=False)
    origen = models.CharField(max_length= 20 ,default=False)

class Amonestacion(models.Model):
    id_jugador = models.ForeignKey(Users, on_delete=models.CASCADE,related_name='id_jugador')
    id_partido = models.ForeignKey(Partidos, on_delete=models.CASCADE) 
    id_arbitro = models.ForeignKey(Users, on_delete=models.CASCADE,related_name='id_arbitro_campo')

class liguilla(models.Model):
    id_liguilla = models.AutoField(primary_key=True)
    id_equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE,related_name="id_equipo_stadisticas")
    inicio_liga = models.DateField()
    partidos_ganados = models.IntegerField()
    partidos_perdidos = models.IntegerField()
    partidos_enpatados = models.IntegerField()
    goles_favor = models.IntegerField()
    goles_enccontra = models.IntegerField()
    puntos = models.IntegerField()
    type_torneo = models.IntegerField()
    id_torneo = models.ForeignKey(Torneo, on_delete=models.CASCADE,related_name="id_torneo")
    def __str__(self):
        return self