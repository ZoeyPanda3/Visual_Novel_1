# game/features/customization_flow.rpy
# --------------------------------
# Orchestrates: gender -> name (preserved) -> class/overlay -> confirmation -> jump to Chapter 1

label customization_entry:
    # 1) Choose gender (drives default name + narration flavor later)
    call choose_gender
    # 2) Enter name (prefill from persistent or gender-based default)
    call enter_name
    # 3) Choose class/overlay (warrior/rogue/mage)
    call choose_overlay
    # 4) Confirm & allow edits
    call confirm_setup
    # 5) Proceed to Chapter 1
    jump expression CH1_LABEL


label choose_gender:
    scene bg_cosmos_void with fade_short
    show nyxara_silhouette at truecenter with dissolve
    nyx "Let us begin with form. What mask of mortal flesh will you wear?"

    # Keep the menu question as narration, and only choices inside the menu.
    n "Select your form."
    menu:
        "Female":
            $ player_gender = "female"
        "Male":
            $ player_gender = "male"

    # Assign a sensible default based on gender, but prefer persistent memory if present.
    if persistent.last_player_name:
        $ player_name = persistent.last_player_name
    else:
        if player_gender == "female":
            $ player_name = "Aya"   # from Female PC dossier
        else:
            $ player_name = "Jin"   # from Male PC dossier

    return


label enter_name:
    $ prompt = "Your name is written between shadow and star. Speak it."
    $ entered = renpy.input(prompt, default=player_name, allow=" ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-_.")
    $ entered = entered.strip()
    if entered:
        $ player_name = entered

    # Persist this across future sessions (prefill next time)
    $ persistent.last_player_name = player_name

    nyx "Very well, [player_name]. Your name now threads my veil."
    return


label choose_overlay:
    show nyxara_silhouette at truecenter
    nyx "Now, the tint of your will. How shall your spirit lean?"

    n "Choose the path that colors your voice."
    menu:
        "Warrior - stoic, brutal, disciplined":
            $ player_class = "warrior"
        "Rogue - charming, witty, trickster":
            $ player_class = "rogue"
        "Mage - analytical, mystical, detached":
            $ player_class = "mage"

    # Compute overlay traits for later narration/UI hooks.
    $ overlay_key = player_class
    $ overlay_traits = compute_overlay_traits(overlay_key, player_gender)

    if player_class == "warrior":
        nyx "A blade wrapped in silence. Direct. Predictable... yet not without poetry."
    elif player_class == "rogue":
        nyx "A smile with a knife behind it. Masks upon masks. How delicious."
    else:
        nyx "A mind turned toward the abyss between truths. Careful—stare too long, and the abyss answers."

    return


label confirm_setup:
    # Summary panel with the option to revise any step.
    call screen confirm_setup_screen(
        name_text = player_name,
        gender_text = player_gender.capitalize(),
        class_text = player_class.capitalize()
    )

    # The screen will set _confirm_result to one of:
    # "continue", "edit_name", "edit_gender", "edit_class"
    if _confirm_result == "edit_gender":
        call choose_gender
        call enter_name
        call confirm_setup
        return
    elif _confirm_result == "edit_name":
        call enter_name
        call confirm_setup
        return
    elif _confirm_result == "edit_class":
        call choose_overlay
        call confirm_setup
        return
    else:
        nyx "So be it. A name, a mask, a leaning of soul. Walk, [player_name]—and see if the world believes what you become."
        return
