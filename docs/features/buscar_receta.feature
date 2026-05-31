Feature: Buscar Receta Inteligente
  Como un estudiante que no sabe cocinar
  Quiero ingresar mis ingredientes
  Para obtener una receta basada en mi base de datos local

  Scenario: El usuario busca una receta existente
    Given que el usuario tiene "huevos" en el refrigerador
    When el usuario ingresa "huevos" en el buscador
    And presiona el botón "Generar Receta"
    Then el sistema debe mostrar la receta de "Omelet clásico"