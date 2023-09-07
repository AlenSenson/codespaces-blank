import reflex as rx

from tut import style

class State(rx.State):

    pass

def about():
    return rx.text("about page")

def qa(question,answer):
    return rx.box(
        rx.box(
            rx.text(question, style=style.question_style),
            text_align="right",
        ),
        rx.box(
            rx.text(answer, style=style.answer_style),
            text_align="left",
        ),
        margin_y='1em',
    )


def chat():
    qa_pair = [
        (
            "What is Reflex?",
            "A way to build web apps in pure Python!",
        ),
        (
             "What can I make with it?",
            "Anything from a simple website to a complex web app!",
        ),
        (
            "What is Reflex?",
            "A way to build web apps in pure Python!",
        ),
        (
             "What can I make with it?",
            "Anything from a simple website to a complex web app!",
        ),
        (
            "What is Reflex?",
            "A way to build web apps in pure Python!",
        ),
        (
             "What can I make with it?",
            "Anything from a simple website to a complex web app!",
        ),
    ]

    return rx.box(
        *[
            qa(question,answer)
            for question,answer in qa_pair
        ]
    )
    
def action_bar():
    return rx.hstack(
        rx.input(
            placeholder='Ask a question',
            style=style.input_style,
        ),
        rx.button('Ask',style=style.button_style,),
    )

def index() -> rx.Component:
    return rx.container(
        chat(),
        action_bar(),
        )


# Add state and page to the app.
app = rx.App()
app.add_page(index,route="/")
app.add_page(about,route="/about")
app.compile()
