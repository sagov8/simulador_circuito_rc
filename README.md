# ⚡ Simulador Interactivo de un Circuito RC en Serie

Este proyecto es una aplicación web interactiva desarrollada con **Python** y **Streamlit** que simula y visualiza el proceso de **carga de un capacitor** en un circuito RC (Resistencia-Capacitor) en serie bajo una fuente de voltaje de corriente continua (DC).

La herramienta permite a los usuarios modificar la Resistencia ($R$) y la Capacitancia ($C$) del circuito para observar inmediatamente cómo estos cambios afectan la **Constante de Tiempo ($\tau$)** y la **respuesta temporal** de la carga $q(t)$ y el voltaje $V_C(t)$.

---

## 💡 Conceptos Fundamentales

El análisis del circuito se basa en la aplicación de la Ley de Voltajes de Kirchhoff (LVK), resultando en una Ecuación Diferencial Ordinaria (EDO) de primer orden.

### 1. Ecuación del Circuito (LVK)

Aplicando la Ley de Voltajes de Kirchhoff, se obtiene la EDO que modela la carga $q(t)$ del capacitor, donde $E_0$ es el voltaje de la fuente:

$$R \frac{dq}{dt} + \frac{1}{C}q = E_0$$

### 2. Solución Analítica

La solución de la EDO (asumiendo que el capacitor está inicialmente descargado, $q(0)=0$) define la carga en función del tiempo:

$$q(t) = E_0 C \left(1 - e^{-t/(RC)}\right)$$

### 3. Constante de Tiempo ($\tau$)

El parámetro $\tau$, que rige la velocidad de carga, se calcula como:

$$\tau = RC$$

---

## ⚙️ Tecnologías Utilizadas

* **Python:** Lenguaje de programación principal.
* **Streamlit:** Framework para la creación de la interfaz de usuario interactiva (UI).
* **NumPy:** Utilizado para cálculos numéricos y generación de datos de tiempo.
* **Plotly:** Librería para la visualización gráfica interactiva de la carga y el voltaje.

---

## 🚀 Instalación y Ejecución

Para ejecutar el simulador localmente, sigue los siguientes pasos:

### 1. Requisitos

Asegúrate de tener Python instalado (versión 3.8+ recomendada).

### 2. Clonar el Repositorio

```bash
git clone <URL_DE_TU_REPOSITORIO>
cd <nombre-del-proyecto>
```

3. Instalar Dependencias
Instala las librerías necesarias usando pip:
```bash
pip install streamlit numpy plotly
```

4. Ejecutar la Aplicación
Dentro del directorio del proyecto donde se encuentra el archivo app.py ejecutar:
```bash
streamlit run ./app.py
```
