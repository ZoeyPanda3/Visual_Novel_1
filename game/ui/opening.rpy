# game/ui/opening.rpy
# --------------------------------
# Black-screen opening that auto-uses FreakySmoke if present,
# then hands off to the goddess intro.

# Prepare text kwargs (font, size, color, outlines, alignment) at a safe init time.
init 10 python:
    # Candidate locations for your font
    _font_candidates = [
        "assets/fonts/FreakySmoke.otf",
        "fonts/FreakySmoke.otf",
        "FreakySmoke.otf",
    ]

    _opening_font = None
    for _fp in _font_candidates:
        if renpy.loadable(_fp):
            _opening_font = _fp
            break

    # Build kwargs to pass into Text(...)
    _opening_text_kwargs = dict(
        size=42,
        color="#EDE8FF",
        outlines=[ (2, "#000000", 0, 0) ],
        xalign=0.5,
        yalign=0.5,
        text_align=0.5,
    )
    if _opening_font:
        _opening_text_kwargs["font"] = _opening_font
        try:
            if hasattr(config, "preload_fonts"):
                config.preload_fonts = list(set((config.preload_fonts or []) + [_opening_font]))
        except Exception:
            pass
    else:
        renpy.log("opening.rpy: FreakySmoke.otf not found; using default font for opening titles.")

# Gentle fade-in, hold, fade-out
transform fade_hold:
    alpha 0.0
    linear 0.8 alpha 1.0
    pause 1.6
    linear 0.6 alpha 0.0

label opening_titles:
    scene black with fade
    $ renpy.pause(0.4)

    # Line 1
    show expression Text("A lone soul drifts into my dominion... how curious.", **_opening_text_kwargs) at fade_hold
    $ renpy.pause(3.2)

    # Line 2
    show expression Text("Few dare the embrace of shadow, yet here you are — unbidden, unveiled.", **_opening_text_kwargs) at fade_hold
    $ renpy.pause(3.2)

    # Line 3
    show expression Text("Shall I weave you into my lies, or will you prove bold enough to seek the truth I conceal?", **_opening_text_kwargs) at fade_hold
    $ renpy.pause(3.2)

    scene black with fade
    $ renpy.pause(0.3)

    jump prologue_intro
