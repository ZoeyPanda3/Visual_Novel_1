# game/script.rpy
# --------------------------------
# Canonical entrypoint. Shows the black-screen opening lines,
# then continues into the prologue flow.

label start:
    jump opening_titles


# If you ever need a quick test entry, you can comment the line above
# and jump directly to specific labels like:
#     jump prologue_intro
#     jump chapter_1_start
