import reflex as rx
from RecursosIT_ReflexHackt.webparts.navbar import navbar
from RecursosIT_ReflexHackt.webparts.footer import footer
from RecursosIT_ReflexHackt.pages.roadmap import roadmap
from RecursosIT_ReflexHackt.webparts.languageslinks.languageslinks import languages
from RecursosIT_ReflexHackt.estilos.sections import style_langs


def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                rx.text(
                    "RECURSOS IT",
                    as_ = "b",
                    size = "9",
                    margin_left = "0.5em",
                    margin_bottom = "0.3em",
                    font_family = "Antonio, sans serif",
                    color = "#D1D1D1"
                ),
                rx.text(
                    """Bienvenido a Recursos-IT.
                        En esta web encontrarás recursos para empezar tu viaje en la programación. Podrás encontrar
                        recursos para aprender algunos de los lenguajes de programación más conocidos o incluso
                        Bases de Datos."""
                        ),
                rx.text(
                    "¡Se acabó la excusa de no saber por dónde empezar a programar!"
                        ),
                roadmap(),
                languages(),
                display = "flex",
                padding = "1em",
                padding_bottom = "4em",
                margin_top = "1em",
                margin_bottom = "1.5em",
                max_width= "50em",
            ),
        ),
        footer()
    )
