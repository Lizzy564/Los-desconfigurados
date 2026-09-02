import streamlit as st
from agenda import Agenda


# CONFIGURACIÓN

st.set_page_config(
    page_title="Gestión de contactos",
    page_icon="📒",
    layout="wide"
)



# INICIALIZAR AGENDA

if "agenda" not in st.session_state:
    st.session_state.agenda = Agenda()

agenda = st.session_state.agenda


# FUNCIONES

def limpiar_campos():
    st.session_state.nombre = ""
    st.session_state.telefono = ""


def agregar_contacto():

    nombre = st.session_state.nombre.strip()
    telefono = st.session_state.telefono.strip()

    if not nombre:
        st.warning("Escribe un nombre.")
        return

    if not telefono:
        st.warning("Escribe un teléfono.")
        return

    try:
        existe = agenda.contiene(nombre)

        agenda.agregar(nombre, telefono)

        if existe:
            st.success(
                f"El teléfono de {nombre} fue actualizado."
            )
        else:
            st.success(
                f"{nombre} fue agregado a la agenda."
            )

    except ValueError as error:
        st.error(str(error))


def buscar_contacto():

    nombre = st.session_state.nombre.strip()

    if not nombre:
        st.warning("Escribe un nombre.")
        return

    try:

        telefono = agenda.telefono_de(nombre)

        st.info(
            f"**Nombre:** {nombre}\n\n"
            f"**Teléfono:** {telefono}"
        )

    except KeyError:

        st.error(
            f"No existe un contacto llamado {nombre}."
        )


def eliminar_contacto():

    nombre = st.session_state.nombre.strip()

    if not nombre:
        st.warning("Escribe un nombre.")
        return

    try:

        agenda.eliminar(nombre)

        st.success(
            f"{nombre} fue eliminado de la agenda."
        )

        limpiar_campos()

    except KeyError:

        st.error(
            f"No existe un contacto llamado {nombre}."
        )


# ENCABEZADO

col1, col2 = st.columns([3, 1])

with col1:
    st.title("📒 Agenda de Contactos")
    st.caption("Gestiona tus contactos de forma sencilla")

with col2:
    cantidad_contactos = len(agenda)
    st.markdown(f"""
    <div style="
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100%;
        margin-top: 10px;
    ">
        <div style="
            padding: 10px 18px;
            border: 1px solid rgba(128,128,128,0.3);
            border-radius: 10px;
            text-align: center;
            background-color: var(--background-color);
            color: var(--text-color);
        ">
            <div style="
                font-size: 22px;
                font-weight: bold;
            ">
                {cantidad_contactos}
            </div>
            <div style="
                font-size: 13px;
                opacity: 0.7;
            ">
                Contactos
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.divider()


# COLUMNAS

col_formulario, col_contactos = st.columns([1, 2])



# FORMULARIO


with col_formulario:

    st.subheader("Nuevo contacto")

    st.text_input(
        "Nombre:",
        key="nombre"
    )

    st.text_input(
        "Teléfono:",
        key="telefono"
    )


    # BOTÓN AGREGAR / ACTUALIZAR

    st.button(
        "➕ Agregar / actualizar",
        use_container_width=True,
        on_click=agregar_contacto
    )


    
    # BOTÓN BUSCAR

    st.button(
        "🔍 Buscar",
        use_container_width=True,
        on_click=buscar_contacto
    )


    # BOTÓN ELIMINAR

    st.button(
        "🗑 Eliminar",
        use_container_width=True,
        on_click=eliminar_contacto
    )


    # BOTÓN LIMPIAR

    st.button(
        "Limpiar",
        use_container_width=True,
        on_click=limpiar_campos
    )


# LISTA DE CONTACTOS

with col_contactos:

    st.subheader("Contactos")


    # FILTRO

    filtro = st.text_input(
        "🔎 Filtro visual:",
        placeholder="Escribe un nombre para filtrar..."
    ).lower()


    # CREAR LISTA

    contactos = []

    for nombre_contacto in agenda.nombres():

        if (
            filtro == ""
            or nombre_contacto.lower().startswith(filtro)
        ):

            try:

                telefono_contacto = agenda.telefono_de(
                    nombre_contacto
                )

                contactos.append({
                    "Nombre": nombre_contacto,
                    "Teléfono": telefono_contacto
                })

            except KeyError:
                pass


    # MOSTRAR CONTACTOS

    if contactos:

        st.dataframe(
            contactos,
            use_container_width=True,
            hide_index=True
        )

    else:

        st.info(
            "No hay contactos para mostrar."
        )


    # CONTADOR

    st.caption(
        f"Contactos: {len(agenda)}"
    )
