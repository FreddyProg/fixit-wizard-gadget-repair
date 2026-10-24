from js import document
from pyodide.ffi import create_proxy


def show_status(message):
    document.getElementById("form-status").textContent = message


def handle_quote(event):
    event.preventDefault()
    name = document.getElementById("name").value.strip()
    if not name:
        show_status("Please enter your name so we can get back to you.")
        return
    project = document.getElementById("project").value
    show_status(f"Thanks, {name}! We received your {project.lower()} request.")
    document.getElementById("quote-form").reset()


def toggle_menu(event):
    menu = document.getElementById("main-nav")
    button = document.getElementById("menu-toggle")
    is_open = menu.classList.toggle("open")
    button.setAttribute("aria-expanded", str(is_open).lower())


document.getElementById("quote-form").addEventListener(
    "submit", create_proxy(handle_quote)
)
document.getElementById("menu-toggle").addEventListener(
    "click", create_proxy(toggle_menu)
)
