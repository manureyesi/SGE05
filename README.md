# Tarea para SGE05

## Enunciado.

Una vez creado el módulo de openacademy de la guía oficial de Odoo 11, tendremos que realizar unas pequeñas modificaciones para ampliarlo. La guía oficial se encuentra en [este enlace](https://www.odoo.com/documentation/11.0/howtos/backend.html) y la cocumentacion en español de [odoo](http://vauxoo.github.io/odoo/howtos/backend.html). 

  1. Propiedades del módulo.
  
    1. Cambiar el nombre del módulo por “academia <tu_nombre>”.
    2. Cambiar el autor del módulo por “<tu_nombre> <apellido1> <apellido2>
    
  2. Modelos
  
    1. Crear un modelo para aula que indique el centro, el número de asientos, el nombre, la planta y el número de aula.
    2. Editar el modelo partner e incluir la opción de que pueda indicarse que es alumno, así como su fecha de nacimiento.
    
  3. Relaciones entre modelos
  
    1. Una sesión debe impartirse en un aula. Relaciona la sesión con el aula y el aula con las diferentes sesiones.
    
  4. Vistas de los modelos
  
    1. Crea las vistas de búsqueda, árbol y formulario para las aulas.Edita las vistas de partner para incluir los nuevos datos.
    
  5. Campos calculados
  
    1. Añade el campo edad para partner y calcúlalo a partir de la fecha de nacimiento.
    2. Edita la vista de formulario para visualizar el nuevo campo.
    
  6. Onchange
  
    1. Los alumnos deberán ser mayores de 16 años. Si cambia la fecha de nacimiento, se deberá comprobar si es así. Si cambia el campo que indica si es o no alumno, también se deberá comprobar.
    2. Los instructores deberán ser mayores de 18 años. Si cambia la fecha de nacimiento o el campo que indica que es instructor, se comprobará.
    3. En caso de fallo, se avisará al usuario del problema con un warning.
    
  7. Vistas avanzadas
  
    1. Crea una vista de tipo graph a partir de la edad media de los asistentes a una sesión.
    
  8. __Instalación y pruebas del módulo__

__IMPORTANTE__: para facilitar la corrección, el código modificado o nuevo deberá comentarse. Si es una línea, el comentario será de línea (CAMBIO TAREA SXE05). Si es un bloque, el comentario se pondrá al principio (INICIO CAMBIOS TAREA SXE05) y al final (FIN CAMBIOS TAREA SXE05). Ten en cuenta que los comentarios deberán aparecer tanto en los archivos de Python como de XML.

__NOTAS:__

El comando para crear un modulo es:

```
odoo scaffold openacademy /usr/lib/python3/dist-packages/odoo/addons
```