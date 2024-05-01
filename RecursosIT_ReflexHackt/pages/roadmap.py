import reflex as rx
import RecursosIT_ReflexHackt.estilos.sections as stylesections

def roadmap():
    return rx.vstack(
        stylesections.style_titles("RUTAS PARA EMPEZAR"),
        rx.text(
            """¿No sabes por dónde comenzar? Aquí tienes una web con una guía a
            seguir en función de lo que más te llame la atención."""
            ),
        rx.link(
            rx.button(
                rx.image(
                src="roadmapsh_icon.png",
                width = "2em",
                height = "2em",
                border_radius = "8px 8px 8px 8px"
                ),
                rx.text(
                    "Roadmap.sh",
                    color = "#0A0A0A"),
                size = "3",
                padding = "1em",
                border_radius= "8px",
                margin_top = "0.5em",
                variant = "surface",
                color_scheme = "gray"
            ),
            href = "https://roadmap.sh/",
            is_external = True
            )
        )
