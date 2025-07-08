# ///////////////////////////////////
# 1st test of the module
# ///////////////////////////////////

# -- imports ---

import os

from dotenv import load_dotenv
from rich import print as rpr

from .utz import he1

# --- Vars ---
load_dotenv("src/.azz")
NOV_T = os.getenv("NOV")


# -- Main Function ----


def b1_main():
    brint()


# ---sub functions ---

#  Brintaz envz

def brint():
    he1("Brintaz envz")
    rpr(NOV_T)
