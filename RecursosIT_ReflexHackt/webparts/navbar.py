import reflex as rx

def navbar():
    return rx.hstack(
        rx.image(
            src = "/IT_logofit2.png",
            width = "53px",
            height = "36.6px",
            padding_x = "8px",
            padding_y = "4px"
        ),
        rx.text("¡Bienvenido a Recursos-IT!",
                as_= "b",
                size = "5",
                align = "left",
                padding_x = "8px",
                padding_y = "4px"
                ),
        rx.spacer(),
        rx.text("¿Aprendemos a programar?",
                align = "right",
                padding_x = "8px",
                padding_y = "4px"
        ),
        bg = "#7f51fe",
        padding_x = "0.7em",
        padding_y = "4px",
        width = "100%",
        align = "center",
        direction = "row",
        position = "sticky",
        top = "0",
        z_index = "9"
    )
