from django.db import models
from django.db import connection

# Create your models here.

class Curso(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, null=False, blank=False)
    descripcion = models.TextField(null=True, blank=True)
    imagen = models.URLField(blank=False, null=False, default="https://st3.depositphotos.com/16203680/19307/v/950/depositphotos_193076602-stock-illustration-question-mark-hand-drawn-symbol.jpg")
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        managed = True
        db_table = 'cursos'


class Estudiante(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, null=False, blank=False)
    apellido = models.CharField(max_length=50, null=False, blank=False)
    cursos = models.ManyToManyField(Curso, related_name="estudiantes", blank=True)
    
    def __str__(self):
        return  f"{self.nombre} {self.apellido}"
    
    class Meta:
        managed = True
        db_table = 'estudiantes'
        
    @staticmethod
    def obtener_cursos(id):
        with connection.cursor() as cursor:
            cursor.execute(
                """
                    SELECT c.id, c.nombre, c.descripcion, c.imagen
                    FROM cursos c
                    INNER JOIN estudiantes_cursos ec ON ec.curso_id = c.id
                    WHERE ec.estudiante_id = %s
                """,
                [id],
            )
            cursos = cursor.fetchall()
            
            cursos = [Curso(id=curso[0], nombre=curso[1], descripcion=curso[2], imagen=curso[3]) for curso in cursos]
            
            return cursos
        