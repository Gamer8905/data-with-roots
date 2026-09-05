# Data with Roots

Aplicación web interactiva de **Machine Learning** desarrollada con **Python**, **Flask** y **Bootstrap** para estimar el **tiempo de entrega según la distancia recorrida** mediante un modelo de **Regresión Lineal Simple**.

<p align="center">
  <strong>Universidad de Cundinamarca · Semestre 6 · Machine Learning</strong>
</p>

---

##  Tema del Proyecto

**Estimar el tiempo de entrega según la distancia recorrida.**

Se utilizan **600 registros históricos** de envíos (distancia en km y tiempo real de entrega en minutos) para entrenar un modelo de Regresión Lineal Simple que predice el tiempo de entrega para nuevas distancias.

## Características

- **Conceptos de Machine Learning** explicados de forma visual
- **Tipos de ML**: Supervisado, No Supervisado y por Refuerzo
- **4 Casos de Uso** en diferentes contextos (salud, finanzas, retail, autos)
- **Regresión Lineal** - conceptos fundamentales
- **Gráfico de dispersión** con línea de regresión generado con matplotlib
- **Formulario de predicción** en tiempo real con el modelo scikit-learn

##  Tecnologías

| Tecnología | Versión | Función |
|-----------|---------|---------|
| Python | 3.x | Lenguaje principal |
| Flask | 3.0.0 | Microframework web |
| scikit-learn | 1.3.2 | Modelo de Regresión Lineal |
| numpy | 1.26.2 | Cálculos numéricos |
| pandas | 2.1.4 | Manipulación de datos |
| matplotlib | 3.8.2 | Visualización (gráficos) |
| Bootstrap | 5.3.2 | Diseño responsive |

##  Estructura del Proyecto

```
ML/
|-- app.py                    # Aplicación Flask + Modelo ML
|-- generate_dataset.py       # Generador de 600 registros
|-- requirements.txt          # Dependencias de Python
|-- Procfile                  # Configuración para Render
|-- data/
|   +-- delivery_dataset.csv  # 600 registros del dataset
|-- static/css/
|   +-- style.css             # Estilos (tema oscuro)
+-- templates/
    |-- base.html             # Plantilla base (navbar + footer)
    |-- home.html             # Página principal
    |-- ml_concepts.html      # Conceptos de ML
    |-- ml_types.html         # Tipos de ML
    |-- use_case_1.html       # Caso de uso 1
    |-- use_case_2.html       # Caso de uso 2
    |-- use_case_3.html       # Caso de uso 3
    |-- use_case_4.html       # Caso de uso 4
    |-- lr_concepts.html      # Conceptos Regresión Lineal
    +-- lr_application.html   # Aplicación RL (gráfico + formulario)
```

##  Modelo de Regresión Lineal

- **Variable Independiente (X):** Distancia recorrida (km)
- **Variable Dependiente (Y):** Tiempo de entrega (min)
- **Registros:** 600
- **Ecuación:** `Tiempo = 0.4513 × Distancia + 4.87`
- **R²:** 0.9961 (99.6% de varianza explicada)

##  Ejecución Local

```bash
# 1. Instalar dependencias
pip install -r requirements.txt

# 2. Ejecutar la aplicación
python app.py

# 3. Abrir en el navegador
# http://127.0.0.1:5000
```

##  Despliegue en Render

1. Crear un Web Service conectado al repositorio
2. **Build Command:** `pip install -r requirements.txt`
3. **Start Command:** `gunicorn app:app`
4. Crear el servicio

##  Enlaces

- Repositorio: `https://github.com/machinelearning-source/data-with-roots`
- Aplicación (Render): *(pendiente de desplegar)*

---

**Universidad de Cundinamarca · Facultad de Ingeniería · Semestre 6 · Machine Learning**
