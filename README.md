# 🏨 BookingCraft: Preparación y Análisis de Reservas Hoteleras

## 📌 Descripción del Proyecto

El objetivo principal es **limpiar, preparar y analizar** un conjunto de datos relacionados con solicitudes de reservas, aprobaciones, precios y otros campos clave, con vistas a su integración en un **data warehouse** para posteriores análisis de negocio.

---

## 🧰 Tecnologías Utilizadas

- **Python 3.10+**
- **Visual Studio Code**
- **Power BI**
- Librerías de Python: `pandas`, `numpy`, `sqlalchemy`, `matplotlib`, `seaborn`, `pymysql` y `scipy` 

---

## 🧪 Estructura de la Prueba

### 📊 Parte 1: Análisis Exploratorio de Datos (EDA)

- Inspección general del dataset
- Detección de nulos, duplicados y tipos de datos
- Identificación de inconsistencias y reglas de negocio clave

### 🧼 Parte 2: Limpieza y Preparación

- Eliminar duplicados basados en reserva y cantidad
- Validar formato de correos electrónicos
- Verificar valores obligatorios en columnas `authorized_by`, `reason`, y condicional en `reason_2`
- Convertir todas las cantidades a euros utilizando `currex` o librería alternativa
- Eliminar columna redundante `Amount_comges_in_EUR`
- Normalizar texto (minúsculas, capitalización, etc.)

### 📈 Visualización de Datos

- Creación de gráficos básicos en Power BI o Tableau:
  - Tipos de solicitudes más comunes
  - Distribución de cantidades solicitadas
  - Análisis por cliente, aprobador o motivo

---

## 🧹 Reglas de Limpieza Aplicadas

- ✅ Máximo 2 peticiones por reserva y cantidad
- ✅ Todos los valores en `authorized_by` son obligatorios
- ✅ Correos validados mediante expresión regular
- ✅ Conversión de divisa a euros y eliminación de columna original
- ✅ Campos `reason` obligatorios y `reason_2` altamente recomendados

---

## 📊 Resultados

- Dataset final listo para carga en un Data Warehouse
- Visualizaciones que permiten detectar patrones clave
- Código limpio, comentado y modularizado

---

## 💡 Conclusiones

Este proyecto demuestra habilidades en:
- Ingeniería de datos
- Limpieza y validación con `pandas`
- Visualización efectiva en herramientas de BI
- Estandarización para entorno empresarial

---

## 🚀 Cómo ejecutar el proyecto

1. Clona el repositorio en Python
2. Instala las siguientes librerías:
 - pandas
 - sqlalchemy
 - pymysql
 - numpy
 - matplotlib
 - seaborn
 - scipy
3. Ejecuta el programa

