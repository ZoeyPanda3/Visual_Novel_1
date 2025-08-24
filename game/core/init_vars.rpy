# game/core/init_vars.rpy
# -------------------------------------------------------------------
# Core styles, font hookup, character definitions, and persistent defaults.

init -20 python:
    # === FONT SETUP =========================================================
    # Place your font at: game/FreakySmoke.otf
    FONT_PATH = "FreakySmoke.otf"
    try:
        if not renpy.loadable(FONT_PATH):
            renpy.log("NOTE: Custom font not found at '{}' — using default font.".format(FONT_PATH))
    except Exception as e:
        renpy.log("Font load check skipped: {}".format(e))

init -10 python:
    # === TEXT STYLE FOR THE 3 OPENING LINES ================================
    style.prologue_whisper = Style("default")
    style.prologue_whisper.font = FONT_PATH
    style.prologue_whisper.size = 72
    style.prologue_whisper.color = "#EDE6FF"
    style.prologue_whisper.outlines = [(2, "#00000080", 0, 0)]
    style.prologue_whisper.line_spacing = 2
    style.prologue_whisper.text_align = 0.5
    style.prologue_whisper.kerning = 0.0

    if renpy.variant("small"):
        style.prologue_whisper.size = 54

    # === SAY WINDOW LEGIBILITY OVER VIDEO =================================
    style.say_dialogue.outlines = [(1, "#000a", 0, 0)]
    style.say_label.outlines = [(1, "#000a", 0, 0)]

# === CHARACTER DEFINITIONS =================================================
define nyx = Character("???", what_prefix="“", what_suffix="”")

# === GAME STATE DEFAULTS (must be TOP-LEVEL, not inside init python) =======
default player_name = ""
default pc_gender   = "female"   # "female" or "male"
default pc_class    = "warrior"  # "warrior", "rogue", "mage"
