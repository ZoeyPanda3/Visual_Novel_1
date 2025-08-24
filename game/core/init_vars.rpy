# game/core/init_vars.rpy
# --------------------------------
# Global defaults, early constants, & persistent helpers

# Make sure shared constants exist BEFORE other files (like characters.rpy) are initialized.
init -10 python:
    COL_GODDESS = "#C38CFF"
    COL_PLAYER  = "#D0E0FF"

init -1 python:
    # Persistent: remember the most recently used player name across new plays.
    if not hasattr(persistent, "last_player_name"):
        persistent.last_player_name = ""

# Game-session defaults (reset on New Game)
default player_gender = None          # "male" or "female"
default player_name = ""              # Will be set during setup (prefilled from persistent if available)
default player_class = None           # "warrior" | "rogue" | "mage"
default overlay_traits = {}           # Personality tint dictionary (see personalities.rpy)
default overlay_key = None            # convenience mirror of player_class

# Flow control labels for easy maintenance
define START_LABEL = "prologue_intro"
define CH1_LABEL   = "chapter_1_start"

# Visual niceties
define fade_long   = Fade(1.0, 1.0, 1.0)
define fade_mid    = Fade(0.5, 0.5, 0.5)
define fade_short  = Fade(0.25, 0.25, 0.25)

# If you already set up a custom font elsewhere, Ren’Py will use it.
# Otherwise, you can set a default GUI font here (commented out):
# define gui.text_font = "game/assets/fonts/YourCustomFont.otf"
