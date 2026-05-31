# Test Driven Development (TDD)

Se aplicaron pruebas unitarias y de integración durante el ciclo de desarrollo para asegurar la estabilidad del backend.

## 1. Pruebas de Integración (API)
- **Test de Salud (Health Check):** Verifica que el servidor FastAPI responda correctamente en la ruta raíz.
- **Test de Endpoint `/buscar`:** Valida que al enviar un parámetro de consulta, el backend responda con un JSON que contenga los campos `receta`, `info` y `status`.

## 2. Pruebas de Lógica
- **Verificación de Filtro:** Se testeó la función `generar_receta_ia` para asegurar que el separador de documentos funcione correctamente y no retorne el archivo completo.
- **Manejo de Errores:** Se validó que ante la ausencia del archivo `.txt`, el sistema retorne un mensaje de error controlado en lugar de colapsar.