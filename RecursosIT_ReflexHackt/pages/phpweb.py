import reflex as rx
from RecursosIT_ReflexHackt.webparts.navbar import navbar
from RecursosIT_ReflexHackt.webparts.footer import footer
import RecursosIT_ReflexHackt.estilos.sections as stylesections
from RecursosIT_ReflexHackt.estilos.button_links import button_link

@rx.page("/phpweb")
def php():
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                stylesections.style_langs("PHP"),
                rx.text(
                    """PHP fue creado en 1995 por Rasmus Lerdof."""
                ),
                rx.text(
                    """Es usado sobre todo en el ámbito web (sobre todo con su framework Laravel)."""
                ),
                button_link("Un día, Un lenguaje (PHP) : MoureDev",
                            "#6c7eb7",
                            "https://www.youtube.com/watch?v=nPCJAx5c1uE"
                            ),
                button_link("Tutorial introductorio a PHP 8 por MiduDev",
                            "#6c7eb7",
                            "https://www.youtube.com/watch?v=BcGAPkjt_IE"
                            ),
                button_link("W3Schools",
                            "#6c7eb7",
                            "https://www.w3schools.com/php/default.asp"
                            ),
                button_link("Playlist en Youtube por Carlos Alfaro",
                            "#6c7eb7",
                            "https://www.youtube.com/playlist?list=PLH_tVOsiVGzmnl7ImSmhIw5qb9Sy5KJRE"
                            ),
                button_link("Tutorialspoint",
                            "#6c7eb7",
                            "https://www.tutorialspoint.com/php/index.htm"
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

php_app = rx.App()
