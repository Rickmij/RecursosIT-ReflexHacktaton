import reflex as rx
from RecursosIT_ReflexHackt.webparts.navbar import navbar
from RecursosIT_ReflexHackt.webparts.footer import footer
import RecursosIT_ReflexHackt.estilos.sections as stylesections
from RecursosIT_ReflexHackt.estilos.button_links import button_link

@rx.page("/kotlinweb")
def kotlin():
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                stylesections.style_langs("KOTLIN"),
                rx.text(
                    """Kotlin fue creado en 2016 por la empresa JetBrains como sustituto
                    a Java para desarrollo en dspositivos Android."""
                ),
                rx.text(
                    """Kotlin tiene total interoperabilidad con Java, pues funciona también sobre la
                    JVM. Es un lenguaje multiparadigma, pues además de para móviles Android sirve para el
                    backend igual que Java, para web e incluso con el lanzamiento de Kotlin Multiplatform,
                    también se pueden desarrollar apps mobile multiplataforma."""
                ),
                button_link("Un día, Un lenguaje (Kotlin) : MoureDev",
                            "linear-gradient(45deg, #844dfc, #e14361)",
                            "https://www.youtube.com/watch?v=T3ugOYTRF7c"
                            ),
                button_link("Developers Android",
                            "linear-gradient(45deg, #844dfc, #e14361)",
                            "https://developer.android.com/?hl=es-419"
                            ),
                button_link("W3Schools",
                            "linear-gradient(45deg, #844dfc, #e14361)",
                            "https://www.w3schools.com/kotlin/index.php"
                            ),
                button_link("Canal de DevExpert (Antonio Leiva)",
                            "linear-gradient(45deg, #844dfc, #e14361)",
                            "https://www.youtube.com/@devexpert_io/playlists"
                            ),
                button_link("Canal de AristiDev",
                            "linear-gradient(45deg, #844dfc, #e14361)",
                            "https://www.youtube.com/@AristiDevs/playlists"
                            ),
                button_link("JetBrains Academy",
                            "linear-gradient(45deg, #844dfc, #e14361)",
                            "https://www.jetbrains.com/pages/academy/kotlin/"
                            ),
                button_link("Playlist de Píldoras Informáticas sobre Kotlin",
                            "linear-gradient(45deg, #844dfc, #e14361)",
                            "https://www.youtube.com/playlist?list=PLU8oAlHdN5BkdfBPpNv_lVCJxJgE87cr0"
                            ),
                button_link("Tutorialspoint",
                            "linear-gradient(45deg, #844dfc, #e14361)",
                            "https://www.tutorialspoint.com/kotlin/index.htm"
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

kt_app = rx.App()
