# game/personalities.rpy
# Class overlay descriptors (used anywhere via overlay_voice_desc()).

init python:
    CLASS_OVERLAYS = {
        "warrior": "brutal, stoic, blunt, disciplined",
        "rogue":   "charming, witty, opportunistic, trickster",
        "mage":    "analytical, mystical, sometimes detached, cryptic",
    }

    def overlay_voice_desc():
        return CLASS_OVERLAYS.get(store.player_class, "")
