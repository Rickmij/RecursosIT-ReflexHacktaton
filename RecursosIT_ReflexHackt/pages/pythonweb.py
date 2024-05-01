import reflex as rx
from RecursosIT_ReflexHackt.webparts.navbar import navbar
from RecursosIT_ReflexHackt.webparts.footer import footer
import RecursosIT_ReflexHackt.estilos.sections as stylesections
from RecursosIT_ReflexHackt.estilos.button_links import button_link

@rx.page("/pythonweb")
def python():
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                stylesections.style_langs("PYTHON"),
                rx.text(
                    """Python es un lenguaje de programación fuertemente
                        tipado, dinámico, interpretado y de alto nivel creado en 1991 por
                        Guido Van Rossum."""
                ),
                rx.text(
                    """Sus usos son muy numerosos como puede
                        ser web (con frameworks como Django, Flask o Reflex) sobretodo
                        usado en Backend, muy usado en el campo de la IA y aprendizaje automático
                        (con librerías como PyTorch o TensorFlow), para crear scripts y automatizar tareas,
                        para Ciencia de Datos y análisis (con librerías como Pandas, NumPy o Matplolib), o
                        incluso la electrónica"""
                ),
                button_link("Un día, Un lenguaje (Python) : MoureDev",
                            "#3771a2",
                            "https://www.youtube.com/watch?v=5NzfqW_Yt6Y"
                            ),
                button_link("Curso de Python en Youtube por MoureDev",
                            "#ffd141",
                            "https://www.youtube.com/playlist?list=PLNdFk2_brsRdgQXLIlKBXQDeRf3qvXVU_"
                            ),
                button_link("W3Schools",
                            "#3771a2",
                            "https://www.w3schools.com/python/"
                            ),
                button_link("Vídeo explicativo de SoyDalto",
                            "#ffd141",
                            "https://www.youtube.com/watch?v=nKPbfIU442g"
                            ),
                button_link("Programación Fácil",
                            "#3771a2",
                            "https://www.youtube.com/watch?v=tQZy0U8s9LY"
                            ),
                button_link("Vídeo explicativo de HolaMundo",
                            "#ffd141",
                            "https://www.youtube.com/watch?v=nKPbfIU442g"
                            ),
                button_link("Tutorialspoint",
                            "#3771a2",
                            "https://www.tutorialspoint.com/python/index.htm"
                            ),
                
            max_width = "50em",
            padding = "1em",
            padding_bottom = "3em",
            margin_bottom = "2em",
            margin_right = "2em"
            )
        ),
        footer()
    )

python_app = rx.App()
