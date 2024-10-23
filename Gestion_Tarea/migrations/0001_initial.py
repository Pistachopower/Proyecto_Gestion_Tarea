import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Etiqueta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=100)),
                ('Descripcion', models.TextField()),
                ('Duracion_Estimada', models.FloatField()),
                ('Fecha_Inicio', models.DateField()),
                ('Fecha_Finalizacion', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.TextField()),
                ('CorreoElectronico', models.CharField(max_length=100, unique=True)),
                ('Contrasena', models.TextField()),
                ('Fecha_Registro', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Tarea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Titulo', models.CharField(max_length=100)),
                ('Descripcion', models.TextField()),
                ('Prioridad', models.IntegerField()),
                ('Completada', models.BooleanField()),
                ('Fecha_Creación', models.DateField()),
                ('hora_Vencimiento', models.TimeField()),
                ('proyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gestion_Tarea.proyecto')),
            ],
        ),
        migrations.CreateModel(
            name='Asignacion_Tarea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tarea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gestion_Tarea.tarea')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gestion_Tarea.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Tarea_Etiqueta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('etiqueta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gestion_Tarea.etiqueta')),
                ('tarea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gestion_Tarea.tarea')),
            ],
        ),
        migrations.AddField(
            model_name='etiqueta',
            name='tarea',
            field=models.ManyToManyField(through='Gestion_Tarea.Tarea_Etiqueta', to='Gestion_Tarea.tarea'),
        ),
        migrations.AddField(
            model_name='tarea',
            name='usuario',
            field=models.ManyToManyField(through='Gestion_Tarea.Asignacion_Tarea', to='Gestion_Tarea.usuario'),
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Contenido', models.TextField()),
                ('Fecha_Comentario', models.DateTimeField(default=django.utils.timezone.now)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gestion_Tarea.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario_Proyecto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gestion_Tarea.proyecto')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gestion_Tarea.usuario')),
            ],
        ),
        migrations.AddField(
            model_name='proyecto',
            name='usuario',
            field=models.ManyToManyField(through='Gestion_Tarea.Usuario_Proyecto', to='Gestion_Tarea.usuario'),
        ),
    ]