# game/features/goddess_intro.rpy
# -------------------------------------------------------------------
# Prologue intro flow:
# 1) Black screen
# 2) Three mythic lines (FreakySmoke style via style.prologue_whisper)
# 3) Fade to looping video background
# 4) Goddess shadow sprite fades in lower-left
# 5) Dialogue window appears when she speaks

# === TRANSFORMS =============================================================
transform fade_center:
    alpha 0.0
    xalign 0.5
    yalign 0.5
    linear 0.8 alpha 1.0
    on hide:
        linear 0.5 alpha 0.0

transform goddess_entrance:
    alpha 0.0
    xalign 0.05
    yanchor 1.0
    yalign 0.98
    linear 0.8 alpha 1.0

# === GODDESS SHADOW SPRITE ==================================================
# Using your actual file from the screenshot:
#   game/images/goddess_mystery.png
image nyxara shadow = "images/goddess_mystery.png"

label prologue_intro:

    # Start from clean visuals.
    window hide
    scene black
    with Dissolve(0.4)

    # --- Opening Line 1 -----------------------------------------------------
    show expression Text("A lone soul drifts into my dominion... how curious.", style="prologue_whisper") as proline at fade_center
    with Dissolve(0.8)
    pause 1.8
    hide proline
    with Dissolve(0.5)

    # --- Opening Line 2 -----------------------------------------------------
    show expression Text("Few dare the embrace of shadow, yet here you are—unbidden, unveiled.", style="prologue_whisper") as proline at fade_center
    with Dissolve(0.8)
    pause 2.0
    hide proline
    with Dissolve(0.5)

    # --- Opening Line 3 -----------------------------------------------------
    show expression Text("Shall I weave you into my lies... or will you chase the truth I conceal?", style="prologue_whisper") as proline at fade_center
    with Dissolve(0.8)
    pause 2.0
    hide proline
    with Dissolve(0.6)

    # === FADE BLACK AWAY -> REVEAL VIDEO BACKGROUND =========================
    # start_video_bg() is defined in game/core/video_background.rpy
    $ start_video_bg("bg prologue")
    with Dissolve(1.0)

    # === GODDESS SHADOW FADE-IN (LOWER-LEFT) ================================
    show nyxara shadow at goddess_entrance
    with Dissolve(0.6)
    pause 0.2

    # === DIALOGUE BOX APPEARS WHEN SHE SPEAKS ===============================
    window show
    nyx "You do not belong here... and yet, here you stand."
    nyx "A fragile soul, trembling on the edge of truth and shadow."
    nyx "Tell me... will you be my lie, or will you chase your own truth?"

    return
