
from rxconfig import config

import reflex as rx

docs_url = "https://reflex.dev/docs/getting-started/introduction"
filename = f"{config.app_name}/{config.app_name}.py"




def index() -> rx.Component:
    return rx.fragment(
        rx.color_mode_button(rx.color_mode_icon(), float="right"),
        rx.vstack(
            rx.heading("Welcome to Reflex!", font_size="2em"),
            rx.box("Get started by editing ", rx.code(filename, font_size="1em")),
            rx.link(
                "Check out our docs!",
                href=docs_url,
                border="0.1em solid",
                padding="0.5em",
                border_radius="0.5em",
                _hover={
                    "color": rx.color_mode_cond(
                        light="rgb(107,99,246)",
                        dark="rgb(179, 175, 255)",
                    )
                },
            ),
            spacing="1.5em",
            font_size="2em",
            padding_top="10%",
        ),
    )

class DrawerState(rx.State):
    show_right: bool = False
    show_top: bool = False

    def top(self):
        self.show_top = not (self.show_top)

    def right(self):
        self.show_right = not (self.show_right)

def navbar():
    return rx.box(
        rx.button(
            "Show Right Drawer", on_click=DrawerState.right
        ),
        rx.drawer(
            rx.drawer_overlay(
                rx.drawer_content(
                    rx.drawer_header("Confirm"),
                    rx.drawer_body(
                        "Do you want to confirm example?"
                    ),
                    rx.drawer_footer(
                        rx.button(
                            "Close", on_click=DrawerState.right
                        )
                    ),
                    bg="rgba(0, 0, 0, 0.3)",
                )
            ),
            is_open=DrawerState.show_right,
        ),
    )

# Add state and page to the app.
app = rx.App()
app.add_page(index)
app.add_page(navbar, route="/sb")
app.compile()
