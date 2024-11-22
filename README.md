# Uso de Template Tags y Filters en Django

Este proyecto documenta el uso de diferentes template tags y filters de Django para manipular y mostrar datos en las plantillas.

## Template Tags

1. **Tipo de Template Tag: forloop.counter**
   - **Archivo:** `contenido_tareaDosAniosCompletada`
   - **Utilidad:** Mostrar el índice donde se encuentra en el diccionario.
   - **Etiqueta:**
     ```html
     <p>Cantidad de iteraciones de todas las tareas: {{ forloop.counter }}</p>
     ```

2. **Tipo de Template Tag: if else**
   - **Archivo:** `contenido_EtiquetaTareasProyecto`
   - **Utilidad:** Si una tarea es igual a `true`, muestra la tarea.
   - **Etiqueta:**
     ```html
     <p>Cantidad de iteraciones de todas las tareas: {{ forloop.counter }}</p>
     ```

3. **Tipo de Template Tag: for empty**
   - **Archivo:** `tareaProyecto`
   - **Utilidad:** Muestra un texto si no hay elementos que iterar.
   - **Etiqueta:**
     ```html
     <li>No hay proyectos disponibles en este momento.</li>
     ```

4. **Tipo de Template Tag: comment**
   - **Archivo:** `tareaProyecto`
   - **Utilidad:** Hace comentario de varias líneas.
   - **Etiqueta:**
     ```html
     {% comment %}
     Este es un comentario de varias líneas en la plantilla.
     {% endcomment %}
     ```

5. **Tipo de Template Tag: include**
   - **Archivo:** `tareaProyecto`
   - **Utilidad:** Permite agregar una template dentro de otra.
   - **Etiqueta:**
     ```html
     {% include 'otra_template.html' %}
     ```

## Operadores Utilizados

1. **Tipo de Operador: `==`**
   - **Archivo:** `contenido_EtiquetaTareasProyecto`
   - **Condición:** Si `etiqueta.completada == true`.
   - **Ejemplo:**
     ```html
     {% if etiqueta.completada == true %}
       <p>Tarea completada.</p>
     {% endif %}
     ```

2. **Tipo de Operador: `<`**
   - **Archivo:** `contenido_proyecto`
   - **Condición:** Si `proyecto.nombre|length < 50`.
   - **Ejemplo:**
     ```html
     {% if proyecto.nombre|length < 50 %}
       <p>Nombre del proyecto: {{ proyecto.nombre }}</p>
     {% endif %}
     ```

3. **Tipo de Operador: `!=`**
   - **Archivo:** `contenido_tareaDosAniosCompletada`
   - **Condición:** Si `t.proyecto_id != 4`.
   - **Ejemplo:**
     ```html
     {% if t.proyecto_id != 4 %}
       <p>Proyecto no es el número 4.</p>
     {% endif %}
     ```

4. **Tipo de Operador: `and`**
   - **Archivo:** `contenido_tareaProyecto`
   - **Condición:** Si `tarea.estado == 'Completada' and tarea.prioridad <= 22693`.
   - **Ejemplo:**
     ```html
     {% if tarea.estado == 'Completada' and tarea.prioridad <= 22693 %}
       <p>Tarea completada con alta prioridad.</p>
     {% endif %}
     ```

5. **Tipo de Operador: `or`**
   - **Archivo:** `contenido_todosComentarioTarea`
   - **Condición:** Si `comentario.usuario.nombre` o `comentario.fecha_Comentario.year <= 2024`.
   - **Ejemplo:**
     ```html
     {% if comentario.usuario.nombre or comentario.fecha_Comentario.year <= 2024 %}
       <p>Comentario relevante.</p>
     {% endif %}
     ```

## Template Filters

1. **Tipo de Filter: `upper`**
   - **Archivo:** `contenido_proyecto`
   - **Utilidad:** Mostrar el contenido en mayúsculas.
   - **Atributo:**
     ```html
     {{ proyecto.nombre|upper }}
     ```

2. **Tipo de Filter: `floatformat`**
   - **Archivo:** `contenido_proyecto`
   - **Utilidad:** Mostrar la cantidad de decimales para números de tipo float.
   - **Atributo:**
     ```html
     {{ proyecto.duracion_Estimada|floatformat:3 }}
     ```

3. **Tipo de Filter: `length`**
   - **Archivo:** `contenido_proyecto`
   - **Utilidad:** Mostrar la longitud de una cadena.
   - **Atributo:**
     ```html
     {{ proyecto.nombre|length }}
     ```

4. **Tipo de Filter: `date`**
   - **Archivo:** `contenido_proyecto`
   - **Utilidad:** Mostrar el formato de fecha tipo día, mes, año.
   - **Atributo:**
     ```html
     {{ proyecto.fecha_Finalizacion|date:"d-m-Y" }}
     ```

5. **Tipo de Filter: `yesno`**
   - **Archivo:** `contenido_tareaDosAniosCompletada`
   - **Utilidad:** Cambiar de booleano a cadena de "Sí, No".
   - **Atributo:**
     ```html
     {{ t.completada|yesno:"Sí,No" }}
     ```

6. **Tipo de Filter: `truncatechars`**
   - **Archivo:** `contenido_UsuarioTarea`
   - **Utilidad:** Mostrar una cantidad de caracteres determinada.
   - **Atributo:**
     ```html
     {{ asignacion.usuario.nombre|truncatechars:15 }}
     ```

7. **Tipo de Filter: `default`**
   - **Archivo:** `contenido_UsuarioTarea`
   - **Utilidad:** Mostrar un mensaje cuando un campo está vacío.
   - **Atributo:**
     ```html
     {{ asignacion.observaciones|default:"Las observaciones están vacías" }}
     ```

8. **Tipo de Filter: `capfirst`**
   - **Archivo:** `contenido_tareaDosAniosCompletada`
   - **Utilidad:** Mostrar la primera letra en mayúscula.
   - **Atributo:**
     ```html
     {{ t.titulo|capfirst }}
     ```

9. **Tipo de Filter: `add`**
   - **Archivo:** `contenido_proyecto`
   - **Utilidad:** Sumar el valor indicado.
   - **Atributo:**
     ```html
     {{ proyecto.duracion_Estimada|add:"1" }}
     ```

10. **Tipo de Filter: `slice`**
    - **Archivo:** `contenido_proyecto`
    - **Utilidad:** Seleccionar por índices una cadena de texto (no muestra `...`, es diferente de `truncatechars`).
    - **Atributo:**
      ```html
      {{ proyecto.duracion_Estimada|add:"1" }}
      ```

