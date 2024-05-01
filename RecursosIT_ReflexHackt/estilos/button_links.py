import reflex as rx

def button_link(text, color, url):
    return rx.link(
        rx.button(
            rx.icon(tag = "chevrons-right"),
            rx.text(
                text,
                weight = "bold"
            ),
            size = "3",
            width = "100%",
            border_radius = "1em",
            margin = "1em",
            margin_right = "1em",
            padding = "1em",
            bg = color,
            color = "#000000"
        ),
        href = url,
        is_external = True
        

    )
