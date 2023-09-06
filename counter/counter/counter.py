import reflex as rx


class State(rx.State):
    count: int = 0
    c = ["red","green","blue"]

    def increment(self):
        self.count += 1

    def decrement(self):
        self.count -= 1


def index():
    return rx.hstack(

        rx.button(
            "Decrement",
            color_scheme="red",
            border_radius="1em",
            on_click=State.decrement,
        ),
        rx.heading(State.count, font_size="2em", color=State.c[State.count%3]),
        rx.button(
            "Increment",
            color_scheme="green",
            border_radius="1em",
            on_click=State.increment,
        

        ),
       
    )


app = rx.App()
app.add_page(index)
app.compile()