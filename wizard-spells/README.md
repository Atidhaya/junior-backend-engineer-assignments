# Wizard Progression System

## Overview
In this magical realm, a wizard's strength grows as they earn experience through their journeys. As they gain experience, they rise through the ranks, unlocking new titles, completing challenges, and evolving into more powerful beings. The wizard's journey involves progressing through levels, gaining job levels through class challenges, and attaining mastery in their magical craft with **Ascended Titles**.

## Features
- **Leveling System**: The wizard increases their level by gaining experience points.
- **Job Titles**: Based on class challenges completed, the wizard earns various job titles.
- **Ascended Titles**: After completing multiple class challenges, the wizard gains access to prestigious ascended titles.
- **Class Challenges**: Every 5 levels, the wizard faces a new challenge that earns them a job level.
- **Extra Hard Class Challenges**: After every 25 levels (5 class challenges), the wizard is tasked with a harder challenge that grants them an ascended title.

## Progression System

### Wizard's Journey

As a wizard advances through their path, their strength grows. Their journey begins as a **Novice**, but through effort and perseverance, they will be called upon to face greater and greater challenges. 

1. **Leveling Up**: The wizard starts with a base level and earns experience. Each 100 XP grants them a level, and the experience required to level up increases with each level. Every time the wizard levels up, the next level requires additional 100 xp. E.g. 100 xp for level 1, 200 xp for level 2, 300 xp for level 3, etc.
2. **Class Challenges**: Every 5 levels, the wizard completes a class challenge. These challenges represent key milestones in the wizard's growth. After completing 5 class challenges, they will also be ready for **Extra Hard Class Challenges**, marking their evolution into ascended mastery.
3. **Job Titles**: Based on the wizard's class challenges, their job title evolves:
    - **Novice**: 0 - 9 class challenges
    - **Commoner**: 10 - 19 class challenges
    - **Advanced**: 20 - 29 class challenges
    - **Master**: 30 - 39 class challenges
    - **Grandmaster**: 40 or more class challenges
4. **Ascended Titles**: With each set of 20 class challenges completed, the wizard becomes eligible for an ascended title. These represent the wizard's true mastery:
    - **Apprentice**: 0 ascended titles
    - **Mage**: 1 ascended title
    - **Sage**: 2 ascended titles
    - **Archmage**: 3 ascended titles
    - **Dark Lord**: 4 ascended titles
    - **Elder Mage**: 5 or more ascended titles

## Example

For a wizard with **13410 XP**:

```text
Wizard's Level: 15, Job Title: Novice, Ascended Title: Apprentice, Class Challenges Completed: 3, Extra Hard Class Challenges Completed: 0
```

This is because level 15 requires 12,000 XP.

## Setup

### Install the dependencies:

To install the required dependencies, run the following command:

```bash
pip install -r requirements.txt
```

### pytest
