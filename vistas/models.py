from django.db import models

# Create your models here.
"""class Rol(models.Model):
    Rol = models.CharField(max_length=200)
    Descripcion = models.CharField(max_length=200)
    def __str__(self):
        return "%s rol" % self.name

 class Users(models.Model):
    rol = models.OneToOneField(
        Rol,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    Nombre = models.CharField(max_length=200,default=False)
    ApellidoPaterno = models.CharField(max_length=200,default=False)
    ApellidoPaterno = models.CharField(max_length=200,default=False)
    Curp = models.CharField(max_length=200,default=False)
    def __str__(self): 
        return "%s Users" % self.name
"""


class Rol(models.Model):
  Rol = models.CharField(max_length=50, default=False)
  Descripcion = models.CharField(max_length=100, default=False)


class Equipo(models.Model):
  nombre_equipo = models.CharField(max_length=50, default=False)
  media = models.CharField(max_length=100, default=False)

  def __str__(self):
    return "%s the equipo" % self.nombre_equipo


class User(models.Model):
  user_id = models.AutoField(primary_key=True)
  user_rol_id = models.OneToOneField(
    Rol,
    on_delete=models.CASCADE
  )
  equipo_id = models.OneToOneField(
    Equipo,
    on_delete=models.CASCADE
  )
  nombre = models.CharField(max_length=100, default=False, blank=False, null=False)
  apellidoPaterno = models.CharField(max_length=100, default=False, blank=False, null=False)
  apellidoMaterno = models.CharField(max_length=100, default=False, blank=True, null=True)
  cumpleanos = models.DateField()
  curp = models.CharField(max_length=100, default=False)


class Torneo(models.Model):
  torneo_id = models.AutoField(primary_key=True)
  descripcion = models.CharField(max_length=100)
  Equipo = models.ManyToManyField(Equipo)


class Campo(models.Model):
  campo_id = models.AutoField(primary_key=True)
  nombre_campo = models.CharField(max_length=100)
  url = models.CharField(max_length=500)


class Partidos(models.Model):
  id_partido = models.AutoField(primary_key=True)
  fecha = models.DateField(null=True)
  campos = models.ForeignKey(Campo, on_delete=models.CASCADE, related_name="id_campos")
  visitante = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name="id_visitante")
  local = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name="id_local")
  arbitro = models.ForeignKey(User, on_delete=models.CASCADE, related_name="id_arbitro")
  torneo = models.ForeignKey(Torneo, on_delete=models.CASCADE, related_name="id_toreno")
  status = models.ForeignKey(Torneo, on_delete=models.CASCADE, related_name="id_status_torneo")
  entrenador = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name="id_entrenador")


class Gol(models.Model):
  id_amonestacion = models.AutoField(primary_key=True)
  equipo_ganador = models.ForeignKey(Equipo, on_delete=models.CASCADE)
  id_partido = models.ForeignKey(Partidos, on_delete=models.CASCADE)
  minuto = models.CharField(max_length=20, default=False)
  origen = models.CharField(max_length=20, default=False)


class Amonestacion(models.Model):
  id_jugador = models.ForeignKey(User, on_delete=models.CASCADE, related_name='id_jugador')
  id_partido = models.ForeignKey(Partidos, on_delete=models.CASCADE)
  id_arbitro = models.ForeignKey(User, on_delete=models.CASCADE, related_name='id_arbitro_campo')


class resultado(models.Model):
  id_resultado = models.AutoField(primary_key=True)
  id_equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name="id_equipo_stadisticas")
  inicio_liga = models.DateField()
  partidos_ganados = models.IntegerField(default=0)
  partidos_perdidos = models.IntegerField(default=0)
  partidos_empatados = models.IntegerField(default=0)
  goles_favor = models.IntegerField(default=0)
  goles_en_contra = models.IntegerField(default=0)
  puntos = models.IntegerField(default=0)
  id_torneo = models.ForeignKey(Torneo, on_delete=models.CASCADE, related_name="id_torneo")
