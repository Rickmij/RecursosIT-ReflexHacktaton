import reflex as rx
from RecursosIT_ReflexHackt.webparts.navbar import navbar
from RecursosIT_ReflexHackt.webparts.footer import footer
import RecursosIT_ReflexHackt.estilos.sections as stylesections
from RecursosIT_ReflexHackt.estilos.button_links import button_link

@rx.page("/swiftweb")
def swift():
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                stylesections.style_langs("SWIFT"),
                rx.text(
                    """Swift nació en 2014 gracias a Apple."""
                ),
                rx.text(
                    """Sirve para desarrollar apps para dispositivos iOS y macOS."""
                ),
                button_link("Un día, Un lenguaje (Swift) : MoureDev",
                            "#ef5138",
                            "https://www.youtube.com/watch?v=kpsVJptSv1U"
                            ),
                button_link("Swift Playground",
                            "#ef5138",
                            "https://developer.apple.com/swift-playgrounds/"
                            ),
                button_link("SwiftUI (para apps)",
                            "#ef5138",
                            "https://developer.apple.com/xcode/swiftui/"
                            ),
                button_link("Vapor (para backend)",
                            "#ef5138",
                            "https://vapor.codes/"
                            ),
                button_link("Tutorialspoint",
                            "#ef5138",
                            "https://www.tutorialspoint.com/swift/index.htm"
                            ),
                button_link("Swift con Paul Hudson",
                            "#ef5138",
                            "https://www.hackingwithswift.com/100"
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

swift_app = rx.App()
