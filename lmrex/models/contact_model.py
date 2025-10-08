import reflex as rx

class Contact(rx.Model):
    name: str
    thumbnail_path: str  # Path to the uploaded image
    link_url: str        # URL for the contact's link
