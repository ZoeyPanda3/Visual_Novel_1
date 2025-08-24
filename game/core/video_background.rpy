# game/video_background.rpy
# Safe video background helper + helpers to start/stop.
# Will fall back cleanly if assets are missing.

init python:
    def _loadable(path):
        try:
            return renpy.exports.loadable(path)
        except Exception:
            return False

screen video_background(video=None, image=None, loop=True):
    zorder 0
    if video and _loadable(video):
        add Movie(play=video, loop=loop)
    elif image and _loadable(image):
        add image
    else:
        null

label start_video_bg(path=None, still=None, loop=True):
    if path and renpy.exports.loadable(path):
        show screen video_background(video=path, loop=loop)
    elif still and renpy.exports.loadable(still):
        show screen video_background(image=still)
    return

label stop_video_bg():
    hide screen video_background
    return
