def wizard_progress(xp: int):
    level = 0
    xp_required = 100
    class_challenges = 0
    extra_hard_challenges = 0
    job_levels = 0
    tier_2_job_levels = 0
    count_tw = 0
    eligible = False
    # Loop to calculate the level
    while xp >= xp_required:
        xp -= xp_required
        level += 1
        xp_required += 100

        # Every 5 levels, the wizard completes a class challenge and gains a job level
        if level % 5 == 0:
            class_challenges += 1
            job_levels += 1  # Job level increases every time a class challenge is completed
            count_tw += 1
        print(count_tw, count_tw % 20 == 0)
        if count_tw == 20:
            count_tw = 0
            eligible = True
        # print(count_tw)
        # Every 25 levels (20 class challenges), the wizard completes an extra hard challenge and gains tier 2 job level
        if eligible:
            eligible = False
            extra_hard_challenges += 1
            tier_2_job_levels += 1  # Tier 2 job level increases after 5 class challenges (25 levels)

    # Determine job title based on class challenges
    if class_challenges < 10:
        job_title = "Novice"
    elif 10 <= class_challenges < 20:
        job_title = "Commoner"
    elif 20 <= class_challenges < 30:
        job_title = "Advanced"
    elif 30 <= class_challenges < 40:
        job_title = "Master"
    else:
        job_title = "Grandmaster"
    # Determine tier 2 job title based on tier 2 job levels
    if tier_2_job_levels == 0:
        tier_2_job_title = "Apprentice"
    elif tier_2_job_levels == 1:
        tier_2_job_title = "Mage"
    elif tier_2_job_levels == 2:
        tier_2_job_title = "Sage"
    elif tier_2_job_levels == 3:
        tier_2_job_title = "Archmage"
    elif tier_2_job_levels == 4:
        tier_2_job_title = "Dark Lord"
    else:
        tier_2_job_title = "Elder Mage"
    print(f"Wizard's Level: {level}, Job Title: {job_title}, Ascended Title: {tier_2_job_title}, " \
           f"Class Challenges Completed: {class_challenges}, Extra Hard Class Challenges Completed: {extra_hard_challenges}"
)
    # Single print statement for combined results, without job levels and tier 2 job levels
    return f"Wizard's Level: {level}, Job Title: {job_title}, Ascended Title: {tier_2_job_title}, " \
           f"Class Challenges Completed: {class_challenges}, Extra Hard Class Challenges Completed: {extra_hard_challenges}"
