import reflex as rx
from .components.stats_cards import stats_cards_group
from .views.navbar import navbar
from .views.table import main_table
from .components.sidebar import sidebar_bottom_profile

def index() -> rx.Component:
    return rx.hstack(
        # Sidebar
        rx.box(
            sidebar_bottom_profile(),
            width="16em",
            height="100vh",
            border_right="1px solid",
            border_color="border",
            padding_y="1em",
        ),
        # Main content
        rx.box(
            rx.vstack(
                navbar(),
                stats_cards_group(),
                rx.box(
                    main_table(),
                    width="100%",
                ),
                width="100%",
                spacing="6",
                padding_x=["1.5em", "1.5em", "3em"],
            ),
            flex="1",
        ),
        width="100%",
        height="100vh",
        overflow="hidden",
    )


app = rx.App(
    theme=rx.theme(
        appearance="dark", has_background=True, radius="large", accent_color="grass"
    ),
)

app.add_page(
    index,
    title="Student Registration App",
    description="A simple app to manage student data.",
)
