# game/customization_screen.rpy
# Unique screen name to avoid collisions with defaults.

screen character_creator():
    modal True
    zorder 200
    frame:
        padding 30
        xalign 0.5
        yalign 0.5
        has vbox

        text "Character Setup" size 40 xalign 0.5
        null height 20

        text "Name:"
        input:
            value VariableInputValue("player_name")
            length 20
            allow "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz -'"

        null height 14

        text "Sex:"
        hbox:
            spacing 16
            textbutton "Female" action SetVariable("player_sex", "female") selected (player_sex == "female")
            textbutton "Male"   action SetVariable("player_sex", "male")   selected (player_sex == "male")

        null height 14

        text "Class:"
        hbox:
            spacing 16
            textbutton "Warrior" action SetVariable("player_class", "warrior") selected (player_class == "warrior")
            textbutton "Rogue"   action SetVariable("player_class", "rogue")   selected (player_class == "rogue")
            textbutton "Mage"    action SetVariable("player_class", "mage")    selected (player_class == "mage")

        null height 20
        text "Voice overlay: [overlay_voice_desc()]" italic True size 22

        null height 24
        hbox:
            spacing 20
            textbutton "Confirm" action Return(True)
            textbutton "Cancel"  action Return(False)
