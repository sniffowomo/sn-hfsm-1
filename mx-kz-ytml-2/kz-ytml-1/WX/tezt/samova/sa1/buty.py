# /////////////////////////////////////////////////////////////////////////////
# Main entrypoint for the sa1 module.
# /////////////////////////////////////////////////////////////////////////////

# --- Imports ---

from rich import print as rpr

from src.s2 import s2_file


# --- Funcz ---
def buty():
    s2_file()


if __name__ == "__main__":
    buty()
    rpr("[red]Sniffo... [/red]")
