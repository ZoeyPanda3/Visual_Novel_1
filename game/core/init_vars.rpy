# game/init_vars.rpy
# Central place for runtime state. Use `default` for saveable vars.
# For persistent flags, initialize via Python (not `default`).

default player_name = "Astra"
default player_sex = "female"      # "female" | "male"
default player_class = "warrior"   # "warrior" | "rogue" | "mage"

init -1 python:
    # Initialize once; survives across playthroughs.
    if not hasattr(persistent, "did_customize"):
        persistent.did_customize = False
