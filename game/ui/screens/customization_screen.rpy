# game/ui/screens/customization_screens.rpy
# --------------------------------
# Reusable confirmation screen for summary & edits

screen confirm_setup_screen(name_text, gender_text, class_text):
    modal True
    zorder 200

    # Dark veil overlay
    add Solid("#0008")

    frame:
        style "confirm_frame"
        xalign 0.5
        yalign 0.5
        padding (30, 30)

        vbox:
            spacing 18

            text "Confirm Your Shape" style "confirm_title"
            vbox:
                spacing 6
                text "Name: [name_text]" style "confirm_line"
                text "Form: [gender_text]" style "confirm_line"
                text "Path: [class_text]" style "confirm_line"

            hbox:
                spacing 12
                textbutton "Change Name" action [SetVariable("_confirm_result", "edit_name"), Return(True)]
                textbutton "Change Form" action [SetVariable("_confirm_result", "edit_gender"), Return(True)]
                textbutton "Change Path" action [SetVariable("_confirm_result", "edit_class"), Return(True)]

            null height 8

            hbox:
                spacing 12
                textbutton "Continue" action [SetVariable("_confirm_result", "continue"), Return(True)]
                textbutton "Cancel" action Return(False)

# Styles (tweak for your UI theme)
style confirm_frame is frame:
    background Frame(Solid("#1a1328CC"), 12, 12)
    xminimum 640
    yminimum 320

style confirm_title is text:
    size 42
    color "#E5D1FF"
    outlines [ (2, "#000", 0, 0) ]
    xalign 0.5

style confirm_line is text:
    size 28
    color "#EDE8FF"
