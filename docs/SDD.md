# Software Design Document (SDD) - Recetario IA

## 1. Introducción
Este documento describe el diseño técnico del "Recetario Inteligente", una aplicación web diseñada para la recuperación de recetas basada en ingredientes del usuario utilizando arquitectura moderna.

## 2. Arquitectura del Sistema
Se ha implementado una **Arquitectura Monolítica Desacoplada**:
- **Frontend:** Desarrollado con React + Vite y Tailwind CSS para una interfaz reactiva y moderna.
- **Backend:** Desarrollado con FastAPI (Python), aprovechando su alta velocidad y manejo asíncrono.

## 3. Implementación de Inteligencia Artificial (RAG)
El sistema utiliza una arquitectura **RAG (Retrieval-Augmented Generation)** adaptada:
- **Fuente de Datos:** Documentos de texto plano (.txt) que sirven como base de conocimiento local.
- **Motor de Recuperación:** Debido a la utilización de **Python 3.14**, se implementó un motor de búsqueda semántica modular que garantiza la compatibilidad de librerías, permitiendo extraer fragmentos específicos de recetas basados en los ingredientes ingresados.

## 4. Estructura de Datos
- Las recetas se almacenan con separadores estructurales (`---`) para permitir una recuperación precisa y evitar el desbordamiento de contexto.