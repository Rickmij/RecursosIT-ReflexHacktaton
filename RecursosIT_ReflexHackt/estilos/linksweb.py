import reflex as rx

def linkwebs(image, lang, bg, color, url):
    return rx.link(
        rx.box(
            rx.vstack(
                rx.image(
                    src = image,
                    width = "4em",
                    height = "4em"
                ),
                rx.text(
                    lang,
                    color = color,
                    size = "3",
                    as_= "b"
                ),
                height = "100%",
                width = "100%",
                align="center",
                spacing= "3",
            ),
            background = bg,
            padding_y = "1.5em",
            padding_x = "2em",
            border_radius = "16px",
            width = "9.5em",
            height = "9.5em"
        ),
        href = url
    )

