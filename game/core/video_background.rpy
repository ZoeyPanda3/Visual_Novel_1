# game/core/video_background.rpy
# -------------------------------------------------------------------
# Reusable helpers and screen to run a looping video behind the UI.

# IMPORTANT: `default` must be top-level (not in an init python block).
default _current_video_bg_image = None

screen video_background():
    zorder -100  # Under everything.
    if _current_video_bg_image:
        add _current_video_bg_image fit "cover"

init -40 python:
    def start_video_bg(image_name):
        """
        image_name: An image key defined via `image bg <name> = Movie(...)`
        Example: start_video_bg("bg prologue")
        """
        store._current_video_bg_image = image_name
        renpy.show_screen("video_background")

    def stop_video_bg():
        store._current_video_bg_image = None
        renpy.hide_screen("video_background")

# === DEFINE YOUR VIDEO AS AN IMAGE =========================================
# Using your actual file seen in the screenshot:
#   game/images/Prologue_Background.mp4
# Ren'Py (via ffmpeg) can play mp4; WEBM is preferred but not required.
image bg prologue = Movie(play="images/Prologue_Background.mp4", loop=True)
