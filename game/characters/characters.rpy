# game/characters/characters.rpy
# --------------------------------
# Character definitions & image placeholders

# Dynamic player character (uses the variable player_name)
define p = Character("[player_name]", color=COL_PLAYER)

# Narration helper (plain ADV narrator)
define n = Character(None)

# The Goddess of Shadow and Lies — Nyxara
define nyx = Character("Nyxara", color=COL_GODDESS)

# Image placeholders (replace with your actual files once ready)
# Put art in: game/assets/images/...
image bg_cosmos_void      = Solid("#0A0812")    # Placeholder: deep space backdrop
image nyxara_silhouette   = Solid("#1A0F2E")    # Placeholder block; swap to sprite file
image nyxara_revealed     = Solid("#2A0F3E")
image nyxara_combat       = Solid("#3A0F4E")

# Suggested real declarations (commented):
# image bg cosmos void = "assets/images/backgrounds/cosmos_void.png"
# image nyxara silhouette = "assets/images/sprites/nyxara_silhouette.png"
# image nyxara revealed   = "assets/images/sprites/nyxara_revealed.png"
# image nyxara combat     = "assets/images/sprites/nyxara_combat.png"
