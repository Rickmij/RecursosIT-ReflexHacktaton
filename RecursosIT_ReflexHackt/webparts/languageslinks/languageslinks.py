import reflex as rx
from RecursosIT_ReflexHackt.estilos.linksweb import linkwebs
import RecursosIT_ReflexHackt.estilos.sections as stylesections

def languages():
    return rx.vstack(
        stylesections.style_titles("LENGUAJES"),
        rx.flex(
            linkwebs("/python_logo.png", "Python", "linear-gradient(90deg, #f4ff4b, #1474d4)", "#F7F7F7", "/pythonweb"),

            linkwebs("/javascript_logoletras.png", "JavaScript", "#f7df1e", "#0F0F0F", "/jsweb"),

            linkwebs("/csharp_Clogo.png", "C#", "#832699", "#F7F7F7", "/csweb"),

            linkwebs("/java_logo.png", "Java", "#F5F5F5", "#0F0F0F", "/javaweb"),

            linkwebs("/Typescript_TS.png", "TypeScript", "#017acc", "#F7F7F7", "/tsweb"),

            linkwebs("/kotlin_logo.png", "Kotlin", "linear-gradient(45deg, #844dfc, #e14361)", "#F7F7F7", "/kotlinweb"),

            linkwebs("/swift_whitelogo.png", "Swift", "#ef5138", "#F7F7F7", "/swiftweb"),

            linkwebs("/golang_whitelogo.png", "Go", "#00acd9", "#F7F7F7", "/goweb"),

            linkwebs("/Rust_whitelogo.png", "Rust", "#000000", "#F7F7F7", "/rustweb"),

            linkwebs("/php.png", "PHP", "#6c7eb7", "#F7F7F7", "/phpweb"),

            flex_wrap = "wrap",
            spacing = "3",
            align = "baseline",
            justify = "center"
        ),
        margin_top ="0.5em"
    )
