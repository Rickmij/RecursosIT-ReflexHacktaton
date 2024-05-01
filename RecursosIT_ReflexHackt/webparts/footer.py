import reflex as rx

def footer():
    return rx.hstack(
        rx.spacer(),
        rx.text("Hackatón HolaMundoDay - 2024 by Brais Moure",
            color = "#ffffff",
            padding_y = "16px",
            padding_x = "8px"
        ),
        padding_x = "0.7em",
        bottom = "0",
        position = "absolute",
        align = "end",
        bg = "#181818",
        width = "100%"
    )
