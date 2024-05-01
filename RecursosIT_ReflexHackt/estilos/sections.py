import reflex as rx

def style_titles(word):
    return rx.text(
            word,
            color = "#3dc48d",
            size = "8",
            weight = "bold",
            margin_top = "1em",
            margin_left = "1em",
            margin_right = "1em",
            margin_bottom = "0.5em",
            font_family = "Antonio, sans serif"
            )

def style_langs(word):
    return rx.text(
            word,
            color = "#3dc48d",
            size = "8",
            weight = "bold",
            margin_top = "1em",
            margin_left = "0.5em",
            font_family = "Lato, sans-serif"
            )
