import reflex as rx
from RecursosIT_ReflexHackt.webparts.navbar import navbar
from RecursosIT_ReflexHackt.webparts.footer import footer
import RecursosIT_ReflexHackt.estilos.sections as stylesections
from RecursosIT_ReflexHackt.estilos.button_links import button_link

@rx.page("/goweb")
def go():
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                stylesections.style_langs("GO"),
                rx.text(
                    """Go fue creado en 2009 por Google."""
                ),
                rx.text(
                    """Sus usos principales son orientados al backend y a APIs."""
                ),
                button_link("Un día, Un lenguaje (Go) : MoureDev",
                            "#00acd9",
                            "https://www.youtube.com/watch?v=AGiayASyp2Q"
                            ),
                button_link("Microsoft Learn sobre Go",
                            "#00acd9",
                            "https://learn.microsoft.com/es-es/training/paths/go-first-steps/"
                            ),
                button_link("W3Schools",
                            "#00acd9",
                            "https://www.w3schools.com/go/index.php"
                            ),
                button_link("Tutorial básico en Youtube de Go",
                            "#00acd9",
                            "https://www.youtube.com/watch?v=7SLBaY3jetM"
                            ),
                button_link("Playlist en Youtube de Eduar Tua",
                            "#00acd9",
                            "https://www.youtube.com/playlist?list=PLSAQnrUqbx7sOdjJ5Zsq5FvvYtI8Kc-C5"
                            ),
                
            #max_width = "50em",
            padding = "1em",
            padding_bottom = "3em",
            margin_bottom = "2em",
            margin_right = "2em"
            )
        ),
        footer()
    )

go_app = rx.App()
