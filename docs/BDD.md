# Behavior Driven Development (BDD)

**Característica:** Generación de Recetas Inteligentes
**Como** un usuario que tiene ingredientes limitados
**Quiero** ingresar mis ingredientes en la plataforma
**Para** recibir una receta específica que pueda cocinar de inmediato.

## Escenario: Búsqueda exitosa de receta
- **Given (Dado)** que el usuario se encuentra en la pantalla principal del Recetario IA.
- **And (Y)** el archivo de base de datos local contiene la receta de "Fresas con Crema".
- **When (Cuando)** el usuario escribe "fresas" en el buscador y presiona "Generar Receta".
- **Then (Entonces)** el sistema debe filtrar los documentos locales y mostrar únicamente la receta de "Fresas con Crema".

## Escenario: Ingrediente no encontrado
- **Given (Dado)** que el usuario ingresa un ingrediente inexistente (ej. "piedras").
- **When (Cuando)** presiona el botón de generación.
- **Then (Entonces)** el sistema debe devolver un mensaje amigable indicando que no hay coincidencias y sugiriendo ingredientes base.