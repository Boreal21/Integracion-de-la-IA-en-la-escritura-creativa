# En primer lugar, debes ejecutar el siguiente comando en la terminal de tu computadora:
# python -m venv .venv
# Este comando crea un entorno virtual en la carpeta .venv de tu proyecto.

# En segundo lugar, debes instalar las librerías necesarias en tu entorno virtual con el siguiente comando:
# El siguiente código sirve para instalar Streamlit en tu computadora desde el terminal y hacer un primer programa en Streamlit.
# pip install Streamlit

# Adicional, este código sirve para acceder una página web en tu navegador que te brinda información sobre Streamlit.
# streamlit hello

# En tercer lugar, este comando sirve para ejecutar un script de Python en Streamlit.
# OJO: Debes antes tener instalado Streamlit en tu computadora y 
##     tener un script de Python (your_script.py) que quieras ejecutar en Streamlit.
# python -m streamlit run your_script.py

# Este código sirve para hacer un primer programa en Streamlit.
import streamlit as st

# La función st.markdown permite agregar texto en formato Markdown a la aplicación de Streamlit
st.markdown("<h1 style='text-align: center;'>Ecos de sueños perdidos más allá de los algoritmos</h1>", unsafe_allow_html=True)

# Creamos una barra lateral
sidebar = st.sidebar

# Añadir un select box al sidebar para la selección de la pestaña de la página principal
pagina_principal = sidebar.selectbox("Selecciona una pestaña:", ("Ficha técnica de personajes y escenarios", "Relato", "Escenarios", "Verso", "Diálogo"))

# Lógica para mostrar contenido basado en la selección de la pestaña
if pagina_principal == "Ficha técnica de personajes y escenarios":
    # La función st.markdown permite centrar y agrandar la letra del título de la web en Streamlit.
    st.markdown("<h2 style='text-align: center;'>Ficha técnica de personajes y escenarios</h2>", unsafe_allow_html=True)

    # Escribimos un subtítulo
    st.markdown("<h3 style='text-align: center;'>Andrómeda “La atada”</h3>", unsafe_allow_html=True)


    # Creamos una tabla con la información de los personajes
    tabla_personaje1 = """
    <div style='text-align: center;'>

    |----|Perfil descriptivo| 
    |-------|--------------|
    | **Edad** | 22 años |
    | **Identidad de género** | Mujer |
    | **Ocupación** | Estudiante de Literatura. En su tiempo libre se dedica a su proyecto personal como blogger de crítica literaria, reflexiones cotidianas y crítica miscelánea. |  
    | **Descripción física** | Con un metro sesenta y cinco y una postura segura, su complexión atlética y sus enormes ojos verde esmeralda tienden a reflejar pasión y entusiasmo cuando se encuentra inmersa en una discusión. Su ovalado rostro aloja alrededor de sus rosados delgados labios unas delicadas pecas dispersas que se vuelven más notables cerca de su cumpleaños en febrero a la luz del verano. Su largo cabello castaño oscuro suele estar suelto o atado en un moño desordenado y sus delicadas manos tienden a estar manchadas con tinta en sus delgados y largos dedos. | 
    | **Personalidad** | Atada a sus propios pensamientos y posiciones, Andrómeda es insaciablemente curiosa y busca siempre tener la razón, por lo que suele estar investigando sobre temas nuevos y buscando argumentos para mantenerse informada o descubrir algún detalle que desconoce. Su gusto por quejarse y expresar sus opiniones es incomparable, sea sobre algo trivial o más profundo; llena de ingenio, sus quejas tienden a estar cargadas de observaciones perspicaces junto con una media sonrisa irónica que, mezclada con su lenguaje impertinente la meten en problemas con personas que no entienden su forma de expresarse. Una mente perfeccionista y autocrítica como la de ella tiende a estar en constante lucha con el miedo a no ser lo suficientemente buena; sin embargo, pese a ello, su determinación y pasión por lo que ama, así como su rechazo a las personas que renuncian, la mantienen en marcha. | 
    | **Pasatiempos** | Siempre con un libro en la mano, tiene un amor irremediable por las novelas canónicas, sean clásicas o contemporáneas, incluyendo obras de autores como Jane Austen y Gabriel García Márquez. Le fascina el arte y la historia, por lo que nunca duda en dar caminatas por la ciudad para pasar horas visitando museos, galerías y bibliotecas. |
    | **Relaciones personales** | Celeste, estudiante de Filosofía, es su mejor amiga y disfrutan de acompañarse a los debates sobre ética, a pesar de que Celeste es una constante retadora. Su profesor favorito, el Dr. Rivas, la ha guiado como mentor, desafiándola a pensar críticamente y a ser más profesional y persistente con sus opiniones. De su mamá heredó su amor con la lectura, y de su papá, un importante científico, el amor por el conocimiento y la curiosidad intelectual.|
    | **Aspiraciones** | El sueño de Andrómeda es convertirse en una escritora reconocida, cuya voz influya en el imaginario colectivo y que no sea simple entretenimiento. |

    </div>
    """
    # Mostramos la tabla
    st.markdown(tabla_personaje1, unsafe_allow_html=True)

    # Escribimos un subtítulo
    st.markdown("<h3 style='text-align: center;'>Facultad de Humanidades</h3>", unsafe_allow_html=True)
    
    tabla_escenario1 = """
    <div style='text-align: center;'>

    |----|Perfil descriptivo| 
    |-------|--------------|
    | **Descripción general** | En el corazón del campus universitario, la Facultad de Humanidades se ha configurado como un ambiente vibrante y estimulante lleno de vida y actividad por parte de los estudiantes y las constantes actividades en progreso que refleja un equilibrio ideal entre la carga académica y la vida social. Los eventos que alberga reflejan tanto el respeto por la tradición académica como el entusiasmo por el pensamiento crítico y la innovación que tanto atraen a una estudiante curiosa como Andrómeda. |
    | **Arquitectura** | El edificio histórico de la facultad es de estilo neoclásico, su fachada es de piedra labrada y columnas imponentes. Los pasillos que llevan a sus pequeñas salas de seminario son amplios y están adornados con bustos de filósofos y escritores famosos. |
    | **Edificaciones** | Sus salones de clase están equipados con tecnología de punta y se cuenta con grandes auditorios cuyos asientos emulan un anfiteatro. Su biblioteca es una de las joyas de la facultad, con tres pisos llenos de estanterías de madera oscura que alojan libros en constante actualización y salas estudio silenciosas para trabajar en grupo. Además, cuenta con una amplia Sala de Lectura donde los estudiantes pueden leer y estudiar en la comodidad de suaves sillones a la luz natural que dejan pasar unos hermosos y grandes ventanales. Su Sala de Estudiantes es un espacio de relajo donde estudiantes como Andrómeda se reúnen y debaten sentados en los sillones, jugando ping-pong y o cocinando en la pequeña cocina. |
    | **Lugares de ocio** | En el centro de la facultad se encuentra un pequeño jardín interior con bancos y mesas al aire libre donde los estudiantes se relajan y disfrutan entre clases. Un espacio acogedor donde los estudiantes se reúnen con mesas y sillas de madera para trabajar en sus proyectos mientras disfrutan de un café o un té es la cafetería de la facultad; aunque en los alrededores también existe un café literario donde se organizan micrófonos abiertos de *spoken word*, presentaciones de libros y debates improvisados sobre temas cotidianos. El teatro universitario ofrece una variedad de obras de teatro y conferencias; y la galería de arte ofrece un espacio dentro del campus donde se exhiben obras de arte creadas por estudiantes y artistas locales. |


    </div>
    """
    # Mostramos la tabla
    st.markdown(tabla_escenario1, unsafe_allow_html=True)
    
    # Escribimos un subtítulo
    st.markdown("<h3 style='text-align: center;'>Alex QX-17</h3>", unsafe_allow_html=True)


    # Creamos una tabla con la información de los personajes
    tabla_personaje2 = """
    <div style='text-align: center;'>

    |----|Perfil descriptivo| 
    |-------|--------------|
    | **Edad** | 25 años |
    | **Identidad de género** | Fluido |
    | **Ocupación** | Especialista en Tecnociencia y Ética Algorítmica. Tiene conocimientos en bioingeniería e inteligencia artificial. Oficialmente trabaja en un laboratorio de investigación avanzada para una corporación desarrollando algoritmos; también estudia las implicaciones éticas de la tecnología.|  
    | **Descripción física** | Con su figura andrógina y su metro setenta, es un individuo ágil y delgado, cuya postura relajada refleja aires de confianza. Gracias a la tecnología capilar de la época, su cabello teñido de color plata, puede cambiar su tono según su estado de ánimo o contexto. Su piel clara y delicados rasgos suaves, junto con su mirada de un profundo azul eléctrico se alojan en un rostro ovalado tanto masculino como femenino. | 
    | **Personalidad** | Su mente analítica y altamente inteligente hace de Alex una persona intelectual; ello junto con su capacidad de adaptabilidad le han permitido moverse entre diferentes campos de conocimiento, contextos sociales y profesionales, y así desarrollar una habilidad innata para empatizar con otros a partir de la comprensión de perspectivas diversas. Por el contexto en el que ha crecido, siente una presión constante propia de su lucha interna por trabajar en una corporación alineada a un sistema que prioriza la eficiencia sobre la ética. | 
    | **Pasatiempos** | Además de crear y mejorar algoritmos para sus proyectos personales, disfruta también de pasar largas horas en mundos virtuales para la experimentación científica y para visualizar escenarios que nunca ha conocido. Por las noches, frecuenta los clubes de debate clandestinos, donde participa en foros y paneles de discusión, y luego se une a reuniones de la resistencia para la que utiliza su habilidad para hackear sistemas y acceder a información clasificada para desmantelar las estructuras de control. |
    | **Relaciones personales** | Su mejor amigo, Kai, es un experto en biotecnología, por lo que siempre debaten sobre sus responsabilidades éticas como miembros de la comunidad científica. Su interés por la ética algorítmica lo aprendió de su guía el Dr. Lyra, una prominente figura en la comunidad que le enseñó la importancia de considerar las consecuencias humanas de la tecnología. Su relación con sus padres ingenieros es distante y complicada, ya que su enfoque científico no es nada holístico. |
    | **Aspiraciones** | Su verdadera meta en esta vida es reintegrar aspectos de las humanidades en la tecnociencia, desarrollando tecnologías que sean empáticas y responsables alineadas con el progreso ético; así quiere restaurar la libre voluntad de las personas y libertar a Nueva Horizonte del control de las corporaciones. |

    </div>
    """
    # Mostramos la tabla
    st.markdown(tabla_personaje2, unsafe_allow_html=True)

    

    # Escribimos un subtítulo
    st.markdown("<h3 style='text-align: center;'>Mega-ciudad de Nueva Horizonte</h3>", unsafe_allow_html=True)

    tabla_escenario2 = """
    <div style='text-align: center;'>

    |----|Perfil descriptivo| 
    |-------|--------------|
    | **Descripción general** | La mega-ciudad ultra tecnológica de Nueva Horizonte está ubicada en la Latinoamérica del futuro. Se trata de una metrópolis distópica plagada de rascacielos que tocan las nubes, vehículos autónomos y drones. Allí la mayoría de los habitantes viven una existencia casi automatizada, actuando como personajes no jugables de videojuegos en una simulación controlada por corporaciones tecnológicas y gobiernos autoritarios. |
    | **Urbanismo** | Los espacios verdes son escasos, por lo que la naturaleza se ha tenido que integrar a la arquitectura para sobrevivir, con jardines verticales y parques flotantes que son accesibles solamente para las élites conformadas por los miembros de las corporaciones tecnológicas. La infraestructura urbana está equipada con tecnología avanzada que monitorea y controla casi todos los aspectos de la vida diaria de los ciudadanos. |
    | **Edificaciones** |  |
    | **Lugares de ocio** |  |


    </div>
    """
    # Mostramos la tabla
    st.markdown(tabla_escenario2, unsafe_allow_html=True)

elif pagina_principal == "Relato":
    # Agregamos un subtítulo
    st.markdown("<h2 style='text-align: center;'>Relato</h2>", unsafe_allow_html=True)

    # Escribe tu relato
    texto = """
    Aquí escribe tu relato.
    """

    # Mostramos el texto
    st.markdown(f"<div style='text-align: justify; font-size: 15px;'>{texto}", unsafe_allow_html=True)   

elif pagina_principal == "Escenarios":
    # Agregamos un subtítulo
    st.markdown("<h2 style='text-align: center;'>Escenarios</h2>", unsafe_allow_html=True)

    # Creamos dos columnas separadas para las imágenes
    #
    col1, col2 = st.columns(2)

    # Colocamos las imágenes en las columnas
    col1.image("escenario1.webp", caption='Alex QX-17 frente a la Facultad de Humanidades. Se ve la luz de la máquina del tiempo en el fondo.', width=700)
    col2.image("escenario2.webp", caption='Vista interior del club de debate clandestino debajo de la antigua Facultad de Humanidades.', width=700)

    # Creamos dos columnas separadas para las imágenes
    #col3, col4 = st.columns(2)

    # Colocamos las imágenes en las columnas
    col3.image("escenario3.webp", caption='Vista interior de la sala de seminario de la Facultad de Humanidades con una mesa redonda para los alumnos.', width=700)
    col4.image("escenario4.webp", caption='Vista panorámica de los rascacielos de las corporaciones de tecnología de la mega-ciudad de Nueva Horizonte', width=700)

elif pagina_principal == "Verso":
    # Agregamos un subtítulo
    st.markdown("<h2 style='text-align: center;'>Verso</h2>", unsafe_allow_html=True)

    # Escribe tu verso
    texto2 = """
    Aquí escribe tu verso.
    """
     # Mostramos el texto
    st.markdown(f"<div style='text-align: centre; font-size: 15px;'><em>{texto2}</em></div>", unsafe_allow_html=True)   

elif pagina_principal == "Diálogo":
    # Agregamos un subtítulo
    st.markdown("<h2 style='text-align: center;'>Diálogo</h2>", unsafe_allow_html=True)

    # Creamos dos columnas separadas para las diálogos
    col5, col6 = st.columns(2)

    # Colocamos los diálogos en las columnas
    texto3 = """
    Diálogo 1
    """
    col5.markdown(f"<div style='text-align: justify; font-size: 15px;'>{texto3}</div>", unsafe_allow_html=True)

      # Creamos dos columnas separadas para las diálogos
    col7, col8 = st.columns(2)

    # Colocamos los diálogos en las columnas
    texto4 = """
    Diálogo 2
    """
    col8.markdown(f"<div style='text-align: justify; font-size: 15px;'>{texto4}</div>", unsafe_allow_html=True)
