import streamlit as st
import numpy as np
import plotly.graph_objects as go

# Configuración básica de la página
st.set_page_config(
    page_title="Simulador Circuito RC",
    layout="wide"
)

st.title("Simulador Interactivo de un Circuito RC en Serie")

st.markdown(
    """
    Este aplicativo ilustra la **carga de un capacitor** en un circuito RC en serie,
    siguiendo el modelo de Zill (2009) y la solución por el método del **factor integrante**.
    """
)


#  SIDEBAR: PARÁMETROS

st.sidebar.header("Parámetros del circuito")

R = st.sidebar.slider(
    "Resistencia R [Ω]",
    min_value=100,
    max_value=10000,
    value=1000,
    step=100
)

C_micro = st.sidebar.slider(
    "Capacitancia C [μF]",
    min_value=0.1,
    max_value=1000.0,
    value=100.0
)
C = C_micro * 1e-6  # pasamos de microfaradios a faradios

E0 = st.sidebar.slider(
    "Voltaje constante E₀ [V]",
    min_value=1.0,
    max_value=30.0,
    value=5.0
)

mostrar_pasos = st.sidebar.checkbox("Mostrar desarrollo teórico", value=True)

# ==========================
#  CÁLCULOS DEL MODELO
# ==========================

tau = R * C  # constante de tiempo RC
t_max = 5 * tau if tau > 0 else 1.0   # graficamos hasta 5 constantes de tiempo
t = np.linspace(0, t_max, 500)

# Solución para la carga del capacitor
q = E0 * C * (1 - np.exp(-t / (R * C)))

# Voltaje en el capacitor Vc(t) = q(t) / C
Vc = q / C

# ==========================
#  INTERFAZ PRINCIPAL
# ==========================

col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("Resumen del circuito")

    # Si tienes una imagen llamada circuito_rc.png en la misma carpeta, se mostrará
    try:
        st.image("circuito_rc.png", caption="Circuito RC en serie", width='stretch')
    except Exception:
        st.info("📷 Puedes agregar una imagen llamada `circuito_rc.png` en la carpeta del proyecto para mostrar el circuito.")

    st.markdown("**Ecuación diferencial (Kirchhoff):**")
    st.latex(r"R \frac{dq}{dt} + \frac{1}{C}q = E_0")

    st.markdown("**Solución para la carga (condición inicial q(0)=0):**")
    st.latex(r"q(t) = E_0 C \left(1 - e^{-t/(RC)}\right)")

    st.markdown("---")
    st.markdown("**Constante de tiempo:**")
    st.latex(r"\tau = RC")
    st.write(f"τ = {tau:.4e} s")

    st.markdown("**Carga máxima:**")
    st.latex(r"q_{\max} = E_0 C")
    st.write(f"q_max = {E0*C:.4e} C")

    st.markdown("**Voltaje final en el capacitor:**")
    st.write(f"V₍c,∞₎ = {E0:.2f} V")

with col2:
    st.subheader("Curva de carga del capacitor")

    magnitud = st.radio(
        "Magnitud a graficar:",
        ("Carga q(t) [C]", "Voltaje en el capacitor Vc(t) [V]"),
        horizontal=True
    )

    fig = go.Figure()

    if magnitud.startswith("Carga"):
        fig.add_trace(
            go.Scatter(
                x=t,
                y=q,
                mode="lines",
                name="q(t)"
            )
        )
        fig.update_layout(
            xaxis_title="Tiempo t [s]",
            yaxis_title="Carga q(t) [C]",
            title="Evolución de la carga del capacitor"
        )
    else:
        fig.add_trace(
            go.Scatter(
                x=t,
                y=Vc,
                mode="lines",
                name="Vc(t)"
            )
        )
        fig.update_layout(
            xaxis_title="Tiempo t [s]",
            yaxis_title="Voltaje Vc(t) [V]",
            title="Evolución del voltaje en el capacitor"
        )

    st.plotly_chart(fig, width='stretch')

# ==========================
#  DESARROLLO TEÓRICO
# ==========================

if mostrar_pasos:
    st.markdown("---")
    st.header("Desarrollo teórico (método del factor integrante)")

    st.markdown("**Paso 1.** Escribir la ecuación en forma estándar:")
    st.latex(r"\frac{dq}{dt} + \frac{1}{RC}q = \frac{E_0}{R}")

    st.markdown("**Paso 2.** Identificar:")
    st.latex(r"P(t) = \frac{1}{RC}, \quad f(t) = \frac{E_0}{R}")

    st.markdown("y calcular el factor integrante:")
    st.latex(r"\mu(t) = e^{\int P(t)\,dt} = e^{t/(RC)}")

    st.markdown("**Paso 3.** Multiplicar la EDO por el factor integrante:")
    st.latex(r"e^{t/(RC)} \frac{dq}{dt} + \frac{1}{RC} e^{t/(RC)} q = \frac{E_0}{R} e^{t/(RC)}")

    st.markdown("**Paso 4.** Reconocer el lado izquierdo como derivada del producto:")
    st.latex(r"\frac{d}{dt}\left(e^{t/(RC)} q\right) = \frac{E_0}{R} e^{t/(RC)}")

    st.markdown("**Paso 5.** Integrar ambos lados:")
    st.latex(r"e^{t/(RC)} q(t) = \int \frac{E_0}{R} e^{t/(RC)} dt + C_1")

    st.markdown("**Paso 6.** Resolver la integral y despejar q(t):")
    st.latex(r"q(t) = E_0 C + C_1 e^{-t/(RC)}")

    st.markdown("**Paso 7.** Aplicar la condición inicial q(0) = 0:")
    st.latex(r"0 = E_0 C + C_1 \Rightarrow C_1 = -E_0 C")

    st.markdown("**Paso 8.** Sustituir C₁ y obtener la solución específica:")
    st.latex(r"q(t) = E_0 C \left(1 - e^{-t/(RC)}\right)")
