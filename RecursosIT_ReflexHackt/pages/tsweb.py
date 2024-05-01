import reflex as rx
from RecursosIT_ReflexHackt.webparts.navbar import navbar
from RecursosIT_ReflexHackt.webparts.footer import footer
import RecursosIT_ReflexHackt.estilos.sections as stylesections
from RecursosIT_ReflexHackt.estilos.button_links import button_link

@rx.page("/tsweb")
def typescript():
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                stylesections.style_langs("TYPECRIPT"),
                rx.text(
                    """TypeScript aparece en 2012 y fue creado por Microsoft sobre JavaScript,
                    pero extendiendo su sintaxis."""
                ),
                rx.text(
                    """TypeScript es un lenguaje de programación construido a un nivel superior de
                    JavaScript. Esto quiere decir que TypeScript dota al lenguaje de varias características
                    adicionales que hacen que podamos escribir código con más limpio y sólido, y además
                    todo el código escrito en JS es válido para TS, pero no lo contrario."""
                ),
                button_link("Un día, Un lenguaje (TypeScript) : MoureDev",
                            "#017acc",
                            "https://www.youtube.com/watch?v=4W3UWjyyVkQ"
                            ),
                button_link("TypeScript en Microsoft Learn",
                            "#017acc",
                            "https://learn.microsoft.com/es-es/training/browse/?terms=typescript"
                            ),
                button_link("W3Schools",
                            "#017acc",
                            "https://www.w3schools.com/typescript/index.php"
                            ),
                
            max_width = "50em",
            padding = "1.5em",
            padding_bottom = "3em",
            margin_bottom = "2em",
            margin_right = "2em"
            )
        ),
        footer()
    )

ts_app = rx.App()
