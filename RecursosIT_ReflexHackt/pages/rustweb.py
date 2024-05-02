import reflex as rx
from RecursosIT_ReflexHackt.webparts.navbar import navbar
from RecursosIT_ReflexHackt.webparts.footer import footer
import RecursosIT_ReflexHackt.estilos.sections as stylesections
from RecursosIT_ReflexHackt.estilos.button_links import button_link

@rx.page("/rustweb")
def rust():
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                stylesections.style_langs("RUST"),
                rx.text(
                    """Rust aparece en 2010 de la mano de Graydon Hoare."""
                ),
                rx.text(
                    """Rust se puede usar para cosas como hacer cosas con CLI, redes,
                    crear APIs, programar sistemas entre más cosas."""
                ),
                button_link("Un día, Un lenguaje (Rust) : MoureDev",
                            "#ACACAC",
                            "https://www.youtube.com/watch?v=GWprpnIG-w4"
                            ),
                button_link("Rust en español",
                            "#ACACAC",
                            "https://www.rustlang-es.org/rust-book-es/title-page.html"
                            ),
                button_link("Playlist en Youtube de Luis Serrano Donaire",
                            "#ACACAC",
                            "https://www.youtube.com/playlist?list=PLAMfQH2NKM_tyKzBV1iJf5L8j7oJl6KHl"
                            ),
                button_link("Tutorial introductorio de MiduDev",
                            "#ACACAC",
                            "https://www.youtube.com/watch?v=WMeM7-JswKQ"
                            ),
                button_link("Playlist en Youtube por Stan Tech",
                            "#ACACAC",
                            "https://www.youtube.com/playlist?list=PL1GmZplwRjmNIdo_G2-Jl9mGEsDNHcOPe"
                            ),
                
            max_width = "50em",
            padding = "1em",
            padding_left = "2em",
            padding_bottom = "3em",
            margin_bottom = "2em",
            margin_right = "2em"
            )
        ),
        footer()
    )

rust_app = rx.App()
