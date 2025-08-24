# game/ui/screens/customization_screen.rpy
# -------------------------------------------------------------------
# Character Creator screen (name + gender + class). Designed for Ren'Py 8.4.1.

screen character_creator():
    modal True
    tag character_creator

    # Dim the world behind.
    add Solid("#0008")

    frame:
        style "cc_frame"
        align (0.5, 0.5)

        vbox:
            spacing 12

            text "Character Setup" style "cc_title"

            # --- Name -------------------------------------------------------
            text "Enter your name:" style "cc_label"
            input:
                style "cc_input"
                value VariableInputValue("player_name")
                length 20
                allow "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz -' "
                pixel_width 600

            # Optional hint shown below the field (Input has no true placeholder).
            if player_name == "":
                text "{i}Type a name...{/i}" style "cc_hint"

            null height 18

            # --- Gender -----------------------------------------------------
            text "Gender:" style "cc_label"
            hbox:
                spacing 12
                textbutton "Female" action SetVariable("pc_gender", "female") style "cc_button"
                textbutton "Male"   action SetVariable("pc_gender", "male")   style "cc_button"
            text "[pc_gender!t]" style "cc_value"

            null height 12

            # --- Class ------------------------------------------------------
            text "Class:" style "cc_label"
            hbox:
                spacing 12
                textbutton "Warrior" action SetVariable("pc_class", "warrior") style "cc_button"
                textbutton "Rogue"   action SetVariable("pc_class", "rogue")   style "cc_button"
                textbutton "Mage"    action SetVariable("pc_class", "mage")    style "cc_button"
            text "[pc_class!t]" style "cc_value"

            null height 24

            # --- Actions ----------------------------------------------------
            hbox:
                spacing 18
                textbutton "Confirm" action Return(True)  style "cc_cta"
                textbutton "Cancel"  action Return(False) style "cc_button"

# ====================== Styles (8.4.1-safe) ================================

style cc_frame is frame:
    xmaximum 900
    xpadding 48
    ypadding 36

style cc_title is text:
    size 42
    bold True
    xalign 0.0
    color "#FFFFFF"

style cc_label is text:
    size 24
    color "#EDE6FF"
    outlines [(1, "#000a", 0, 0)]

style cc_value is text:
    size 22
    color "#C8C0FF"
    outlines [(1, "#000a", 0, 0)]

style cc_hint is text:
    size 18
    color "#BBBBBB"
    italic True

style cc_input is input:
    size 26
    color "#FFFFFF"
    outlines [(1, "#000a", 0, 0)]
    hover_color "#FFFFFF"
    insensitive_color "#AAAAAA"

style cc_button is button:
    padding (12, 8)

# Button text styling must use the *_text companion style.
style cc_button_text is button_text:
    size 22

style cc_cta is cc_button
style cc_cta_text is cc_button_text:
    bold True
