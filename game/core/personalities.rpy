# game/core/personalities.rpy
# --------------------------------
# Personality overlays & helpers

init python:
    # Warrior overlay
    def warrior_traits(gender):
        return {
            "overlay": "warrior",
            "voice":   "stoic_brutal_disciplined",
            "tone":    "blunt/controlled",
            "notes":   "Suppressed doubt via action; respects directness.",
            "gender":  gender,
        }

    # Rogue overlay
    def rogue_traits(gender):
        return {
            "overlay": "rogue",
            "voice":   "charming_witty_trickster",
            "tone":    "coy/playful/sardonic",
            "notes":   "Looks for angles; playful danger.",
            "gender":  gender,
        }

    # Mage overlay
    def mage_traits(gender):
        return {
            "overlay": "mage",
            "voice":   "analytical_mystical_detached",
            "tone":    "measured/contemplative",
            "notes":   "Truth-seeking; cosmic curiosity.",
            "gender":  gender,
        }

    def compute_overlay_traits(overlay_key, gender):
        if overlay_key == "warrior":
            return warrior_traits(gender)
        if overlay_key == "rogue":
            return rogue_traits(gender)
        if overlay_key == "mage":
            return mage_traits(gender)
        return {}

    # Hook for inner-voice flavor if/when you want to branch by overlay
    def inner_voice(line):
        return line
