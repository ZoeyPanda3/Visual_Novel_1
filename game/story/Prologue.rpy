# game/story/prologue.rpy
label start:
    call goddess_intro
    jump prologue_after_cc

label prologue_after_cc:
    "Prologue begins after character creation."
    return