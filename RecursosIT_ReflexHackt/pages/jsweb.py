import reflex as rx
from RecursosIT_ReflexHackt.webparts.navbar import navbar
from RecursosIT_ReflexHackt.webparts.footer import footer
import RecursosIT_ReflexHackt.estilos.sections as stylesections
from RecursosIT_ReflexHackt.estilos.button_links import button_link

@rx.page("/jsweb")
def javascript():
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                stylesections.style_langs("JAVASCRIPT"),
                rx.text(
                    """JavaScript fue creado por la empresa Netscape en 1995."""
                ),
                rx.text(
                    """JavaScript es el rey indiscutible de la web, siendo el lenguaje más usado en
                    el frontend ayudándose de HTML y CSS y muchos frameworks como React, Angular, Vue
                    o Svelte entre otros, y para el backend también existe la posibilidad de usar JavaScript
                    con NodeJS,e incluso se pueden hacer aplicaciones."""
                ),
                button_link("Un día, Un lenguaje (JavaScript) : MoureDev",
                            "#f7df1e",
                            "https://www.youtube.com/watch?v=5NzfqW_Yt6Y"
                            ),
                button_link("Aprende JavaScript",
                            "#f7df1e",
                            "https://www.aprendejavascript.dev/"
                            ),
                button_link("W3Schools",
                            "#f7df1e",
                            "https://www.w3schools.com/js/default.asp"
                            ),
                button_link("The Odin Project",
                            "#f7df1e",
                            "https://www.theodinproject.com/"
                            ),
                button_link("Curso de Programación Fácil",
                            "#f7df1e",
                            "https://www.programacionfacil.org/cursos/javascript/javascript_index.html"
                            ),
                button_link("Lenguaje JS (por ManzDev)",
                            "#f7df1e",
                            "https://lenguajejs.com/"
                            ),
                button_link("Tutorialspoint",
                            "#f7df1e",
                            "https://www.tutorialspoint.com/javascript/index.htm"
                            ),
                
            max_width = "50em",
            padding = "0.5em",
            padding_left = "2em",
            padding_bottom = "3em",
            margin_bottom = "2em",
            margin_right = "2em"
            )
        ),
        footer()
    )

js_app = rx.App()
