import reflex as rx
from RecursosIT_ReflexHackt.webparts.navbar import navbar
from RecursosIT_ReflexHackt.webparts.footer import footer
import RecursosIT_ReflexHackt.estilos.sections as stylesections
from RecursosIT_ReflexHackt.estilos.button_links import button_link

@rx.page("/javaweb")
def java():
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                stylesections.style_langs("JAVA"),
                rx.text(
                    """Java fue creado en 1995 por Sun Microsystems."""
                ),
                rx.text(
                    """Fue un lenguaje muy usado en su día, y aunque esté perdiendo mercado, sigue
                    siendo muy usado y solicitado en el backend a día de hoy. Java funciona gracias a
                    la JVM (Java Virtual Machine)."""
                ),
                button_link("Un día, Un lenguaje (Java) : MoureDev",
                            "#ffffff",
                            "https://www.youtube.com/watch?v=W86KTBSiX2o"
                            ),
                button_link("Playlist de TodoCode",
                            "#5382a1",
                            "https://www.youtube.com/playlist?list=PLQxX2eiEaqbwxYrMUJ6gRz82mLzUeeJy9"
                            ),
                button_link("W3Schools",
                            "#e76f00",
                            "https://www.w3schools.com/java/default.asp"
                            ),
                button_link("Tutorialspoint",
                            "#ffffff",
                            "https://www.tutorialspoint.com/java/index.htm"
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

java_app = rx.App()
