# lmrex/ui/contact.py

from lmrex.components.contact_component import contact_component

from ..imports import rx

# from ..routes import contact_page
from ..template import template

contact_url = "pages/contact"


# @rx.page(route=contact_page)
def contact():
    return rx.box(
        template(),
        contact_component(),
        rx.vstack(
            template(),
            spacing="5",
            justify="center",
            align="center",
            min_height="80vh",
            text_align="center",
        ),
    )
