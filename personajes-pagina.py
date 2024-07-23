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

    # Colocamos las imágenes en las columnas
    st.image("escenario1.webp", caption='Alex QX-17 frente a la Facultad de Humanidades. Se ve la luz de la máquina del tiempo en el fondo.', width=700)
    st.image("escenario2.webp", caption='Vista interior del club de debate clandestino debajo de la antigua Facultad de Humanidades.', width=700)
    st.image("escenario3.webp", caption='Vista interior de la sala de seminario de la Facultad de Humanidades con una mesa redonda para los alumnos.', width=700)
    st.image("escenario4.webp", caption='Vista panorámica de los rascacielos de las corporaciones de tecnología de la mega-ciudad de Nueva Horizonte', width=700)

elif pagina_principal == "Verso":
    # Agregamos un subtítulo
    st.markdown("<h2 style='text-align: center;'>Verso</h2>", unsafe_allow_html=True)

    # Escribe tu verso
    texto1 = """
    Aquí escribe tu verso.
    """
     # Mostramos el texto
    st.markdown(f"<div style='text-align: centre; font-size: 15px;'><em>{texto1}</em></div>", unsafe_allow_html=True)   

elif pagina_principal == "Diálogo":
    # Agregamos un subtítulo
    st.markdown("<h2 style='text-align: center;'>Diálogo</h2>", unsafe_allow_html=True)

    texto2 = """
    *En esta ocasión, el personaje del profesor Rivas está siendo interpretado por ChatGPT. El personaje de Celeste será interpretado por su servidora.*
    """
    st.markdown(f"<div style='text-align: centre; font-size: 15px;'><em>{texto2}</em></div>", unsafe_allow_html=True)
    
    # Creamos dos columnas separadas para las diálogos
    col1, col2 = st.columns(2)

    # Colocamos los diálogos en las columnas
    texto3 = """
    **Profesor Rivas:** *(Sentado detrás de su escritorio, ajustando sus gafas mientras revisa unos documentos)* Buenas tardes, Celeste. ¿Cómo estás hoy? ¿Hay algo en particular que te gustaría discutir después de nuestro seminario?
    """
    col1.markdown(f"<div style='text-align: justify; font-size: 15px;'>{texto3}</div>", unsafe_allow_html=True)

      # Creamos dos columnas separadas para las diálogos
    col3, col4 = st.columns(2)

    # Colocamos los diálogos en las columnas
    texto4 = """
    **Celeste:** Buen día profesor, lo que pasa es que hace unos días tuve un encuentro muy particular y he recibido unas notas que me han dejado pensando.
    ¿Usted cree que en un futuro los viajes en el tiempo sean posibles? Digamos que le planteo una situación hipotética en la que es posible, ¿consideraría ético hacer el viaje con el objetivo de cambiar el pasado ya que el futuro no es lo que esperaba? o, quizá, ¿solo para aprender del pasado aquellas cosas que considera importantes y se han perdido, como las humanidades tal vez, y llevar esos conocimientos de vuelta al futuro? 
    """
    col4.markdown(f"<div style='text-align: justify; font-size: 15px;'>{texto4}</div>", unsafe_allow_html=True)

    # Creamos dos columnas separadas para las diálogos
    col5, col6 = st.columns(2)
    
    texto5 = """
    **Profesor Rivas:** *(Frunce el ceño ligeramente, intrigado)* Vaya, Celeste, eso suena realmente fascinante y, debo admitir, un poco fuera de lo común. La cuestión de los viajes en el tiempo ha sido un tema recurrente en la literatura y la filosofía durante décadas, incluso siglos.
    Si consideramos que los viajes en el tiempo son posibles, la ética detrás de cambiar el pasado o aprender de él se vuelve un tema muy complejo.
    *(Hace una pausa, reflexionando)*
    En primer lugar, cambiar el pasado podría tener consecuencias imprevisibles y posiblemente desastrosas. La teoría del caos sugiere que incluso pequeñas alteraciones pueden tener efectos masivos, un concepto a menudo referido como el "efecto mariposa". La intención de mejorar el futuro podría, paradójicamente, empeorarlo de maneras que no podemos prever.
    Por otro lado, si el objetivo es simplemente aprender del pasado, como rescatar conocimientos perdidos de las humanidades, la situación se torna diferente. La adquisición de conocimiento es una búsqueda noble y podría tener menos riesgos asociados si no interfiere directamente con eventos históricos. Sin embargo, siempre existe la posibilidad de que la mera presencia en el pasado pueda alterar de alguna manera el curso natural de los eventos.
    *(Se inclina hacia adelante, mostrando interés)*
    Dime, Celeste, ¿qué te ha hecho pensar en estas cuestiones tan profundas y particulares?
    """
    col5.markdown(f"<div style='text-align: justify; font-size: 15px;'>{texto5}</div>", unsafe_allow_html=True)

      # Creamos dos columnas separadas para las diálogos
    col7, col8 = st.columns(2)

    # Colocamos los diálogos en las columnas
    texto6 = """
    **Celeste:** *(Dubitativa)* Como dije antes, una situación hipotética, profe. Nada de que preocuparse, solo supuse que, ya que usted es un experto en ética, especialmente aplicada a casos ficcionales, me ayudaría a pensar.
    Imagínese un futuro en el que las tecnologías de inteligencia artificial están a tal punto de desarrollo que a diario se trabaja en algoritmos para que predigan el comportamiento de los ciudadanos, que los oriente a tomar las decisiones que las personas en el poder desean y en consecuencia, la ciudad es tecnológicamente floreciente, la mayor parte de la población son personas instruidas en las ciencias, pero se ha perdido todo lo que intentamos promover en nuestra facultad. La homogeneización de la población es inminente, la pérdida de estilos literarios, recursos retóricos, variedades lingüísticas, técnicas de artes plásticas o preservación de tradiciones y patrimonio cultural, ha generado que virtualmente no haya conflicto porque todos son iguales. ¿Sería ético volver al pasado para tratar de detener el desarrollo de las IA o cambiarlo? 
    """
    col8.markdown(f"<div style='text-align: justify; font-size: 15px;'>{texto6}</div>", unsafe_allow_html=True)

    col9, col10 = st.columns(2)

    texto7 = """
    **Profesor Rivas:** *(Asintiendo lentamente, con una expresión pensativa)* Entiendo, Celeste. Esta situación hipotética que planteas es, en efecto, una exploración profunda y perturbadora de los posibles futuros que podemos enfrentar.
    Si nos encontramos en un futuro donde las tecnologías de inteligencia artificial han avanzado hasta el punto de controlar y homogenizar completamente la sociedad, perderíamos algo fundamental de lo que nos hace humanos. Las artes, la literatura, la diversidad cultural y el pensamiento crítico son esenciales para nuestra identidad y desarrollo como individuos y como sociedad.
    Desde una perspectiva ética, volver al pasado para detener o alterar el desarrollo de las IA plantea varias preguntas. Primero, ¿tenemos el derecho de intervenir en el curso de la historia? ¿Quién decide qué es lo mejor para la humanidad? Estas decisiones pueden parecer claras cuando se enfrentan a un futuro distópico, pero las implicaciones son vastas y complicadas.
    Segundo, la intención detrás de tal intervención es crucial. Si el objetivo es preservar la diversidad, el pensamiento crítico y las artes, entonces podríamos argumentar que existe un valor moral en esa acción. No obstante, la manera en que se realice es igualmente importante. ¿Podríamos influir en el desarrollo de las IA de una manera que no suprima completamente su potencial beneficioso? ¿Podríamos encontrar un equilibrio entre tecnología y humanidades?
    *(Se recuesta en su silla, cruzando las manos)* En última instancia, es una cuestión de balance y de entender que nuestras acciones, incluso bien intencionadas, pueden tener consecuencias imprevistas. La ética no siempre ofrece respuestas claras, sino más bien un marco para considerar las implicaciones de nuestras decisiones.
    *(Mira a Celeste con una sonrisa leve)* Creo que tu situación hipotética toca temas muy relevantes para nuestra época y nos recuerda la importancia de las humanidades en cualquier escenario futuro. Gracias por traer esta discusión tan fascinante.
    """
    col9.markdown(f"<div style='text-align: justify; font-size: 15px;'>{texto7}</div>", unsafe_allow_html=True)

    col11, col12 = st.columns(2)

    texto8 ="""
    **Celeste:** *(Con una insistencia casi conflictuada)* Entonces, ¿usted no cree que sea el desarrollo de las IA el culpable de esta pérdida?
    *(Exhala)* Ya hoy en día he notado que hay compañeros que utilizan estas tecnologías para responder exámenes, escribir ensayos o incluso crear el arte para sus congresos o ponencias. Realmente no se puede saber si la información que plantean es fiable, ¿realmente vale la pena que se gradúen como profesionales? *(Reflexiona por unos segundos)* Y luego está la cuestión laboral, porque ¿será posible que artistas, diseñadores, escritores, editores, correctores de estilo pierdan sus trabajos como consecuencia del uso masivo de las IA?
    Me imagino que en un futuro en el que todos se desempeñan en campos similares propios de la ciencia y todos orientados por IA, deben ser muy pocas las personas que consigan trabajos buenos en grandes corporaciones.
    """
    col12.markdown(f"<div style='text-align: justify; font-size: 15px;'>{texto8}</div>", unsafe_allow_html=True)

    col13, col14 = st.columns(2)

    texto9 ="""
    **Profesor Rivas:** *(Asintiendo con una expresión seria)* Has tocado un punto crucial, Celeste. El desarrollo de las IA y su integración en nuestra vida diaria plantea desafíos significativos, no solo para la ética y la educación, sino también para la estructura del mercado laboral y la autenticidad en la producción intelectual y artística.
    Es cierto que la proliferación de herramientas basadas en IA está cambiando la manera en que muchos estudiantes abordan sus tareas académicas. La facilidad con la que se pueden generar respuestas, ensayos e incluso obras de arte plantea preguntas sobre la autenticidad y el valor de esos trabajos. Si un estudiante se gradúa habiendo dependido en gran medida de la IA para sus tareas, podemos cuestionar la validez de su formación y su capacidad para enfrentarse a desafíos reales en su campo profesional.
    En cuanto al mercado laboral, la preocupación de que artistas, diseñadores, escritores, editores y correctores de estilo puedan perder sus trabajos debido al uso masivo de IA es legítima. Las IA pueden producir contenido a una velocidad y costo mucho menores que los humanos, lo que puede hacer que las empresas prefieran utilizarlas. Sin embargo, la creatividad y la capacidad de pensamiento crítico que los humanos poseen siguen siendo insustituibles por las máquinas.
    *(Hace una pausa, considerando sus palabras)* Ahora, si pensamos en un futuro donde todos los trabajos están dominados por las ciencias y orientados por IA, perderíamos una parte vital de nuestra humanidad. Las humanidades nos enseñan a pensar críticamente, a entender y apreciar la diversidad cultural, y a expresar nuestras emociones y experiencias de maneras profundas y significativas. Sin estas disciplinas, la sociedad se volvería mucho más uniforme y menos rica en términos de experiencia humana.
    La clave, creo, está en encontrar un equilibrio. Las IA pueden ser herramientas poderosas para asistirnos y mejorar nuestra eficiencia, pero no deben reemplazar la esencia de lo que significa ser humano. Debemos fomentar una educación que valore tanto la tecnología como las humanidades, y preparar a los estudiantes para usar la IA de manera ética y responsable.
    *(Mira a Celeste con empatía)* Tus preocupaciones son muy válidas y reflejan un tema crítico de nuestra época. Como educadores, debemos trabajar para asegurarnos de que las futuras generaciones estén equipadas no solo con habilidades técnicas, sino también con una comprensión profunda de las humanidades. De esta manera, podemos intentar asegurar un futuro donde la tecnología y la humanidad coexistan de manera armoniosa. 
    ¿Te gustaría explorar más este tema en clase? Podríamos organizar un debate o una serie de conferencias para discutir estas cuestiones en profundidad.
    """
    col13.markdown(f"<div style='text-align: justify; font-size: 15px;'>{texto9}</div>", unsafe_allow_html=True)