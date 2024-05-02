import reflex as rx
from RecursosIT_ReflexHackt.webparts.navbar import navbar
from RecursosIT_ReflexHackt.webparts.footer import footer
import RecursosIT_ReflexHackt.estilos.sections as stylesections
from RecursosIT_ReflexHackt.estilos.button_links import button_link
from RecursosIT_ReflexHackt.estilos.stilos import ESTILO

@rx.page("/csweb")
def csharp():
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                stylesections.style_langs("C# (c sharp)"),
                rx.text(
                    """C# aparece en el año 2000 gracias a Microsoft como parte de su plataforma .NET."""
                ),
                rx.text(
                    """Es el sucesor de los lenguajes C y C++, y es usado sobre todo para aplicaciones
                    de escritorio, backend, APIs y el entorno Microsoft.
                    Es muy usado también en el ámbito de videojuegos, siendo el lenguaje principal para
                    programar del mayor motor de videojuegos del mercado: Unity"""
                ),
                button_link("Un día, Un lenguaje (C#) : MoureDev",
                            "#832699",
                            "https://www.youtube.com/watch?v=L-f8u0hwi4Y"
                            ),
                button_link("Playlist de Héctor de León (hdeleon.net)",
                            "#832699",
                            "https://www.youtube.com/playlist?list=PLWYKfSbdsjJgKGeP2OmTJWXz8qZ7N8xU2"
                            ),
                button_link("W3Schools",
                            "#832699",
                            "https://www.w3schools.com/cs/index.php"
                            ),
                button_link("Microsoft Learn",
                            "#832699",
                            "https://learn.microsoft.com/es-es/training/browse/?products=dotnet"
                            ),
                button_link("Plataforma .NET de Microsoft",
                            "#832699",
                            "https://dotnet.microsoft.com/es-es/learn/csharp"
                            ),
                button_link("Programación Fácil (CURSO AÚN EN DESARROLLO)",
                            "#832699",
                            "https://www.programacionfacil.org/cursos/c_sharp/c_sharp_index.html"
                            ),
                button_link("Playlist en youtube de Informática EJN",
                            "#832699",
                            "https://www.youtube.com/playlist?list=PL7tWmaH04EfLjESN9pYsGhkphQkX3HSDP"
                            ),
                button_link("Vídeo en Youtube de ATL Academy",
                            "#832699",
                            "https://www.youtube.com/watch?v=TqiysLEBZo4"
                            ),
                button_link("Tutorialspoint",
                            "#832699",
                            "https://www.tutorialspoint.com/csharp/index.htm"
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
