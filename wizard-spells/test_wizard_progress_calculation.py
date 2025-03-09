from wizard_progress_calculation import wizard_progress

def test_1():
    xp = 13410
    result = wizard_progress(xp)

    expected_result = "Wizard's Level: 15, Job Title: Novice, Ascended Title: Apprentice, Class Challenges Completed: 3, Extra Hard Class Challenges Completed: 0"
    assert result == expected_result, f"Expected: {expected_result}, but got: {result}"


def test_2():
    xp = 450
    result = wizard_progress(xp)

    expected_result = "Wizard's Level: 2, Job Title: Novice, Ascended Title: Apprentice, Class Challenges Completed: 0, Extra Hard Class Challenges Completed: 0"

    assert result == expected_result, f"Expected: {expected_result}, but got: {result}"


def test_3():
    xp = 34000
    result = wizard_progress(xp)

    expected_result = "Wizard's Level: 25, Job Title: Novice, Ascended Title: Apprentice, Class Challenges Completed: 5, Extra Hard Class Challenges Completed: 0"

    assert result == expected_result, f"Expected: {expected_result}, but got: {result}"

def test_4():
    xp = 50050
    result = wizard_progress(xp)

    expected_result = "Wizard's Level: 31, Job Title: Novice, Ascended Title: Apprentice, Class Challenges Completed: 6, Extra Hard Class Challenges Completed: 0"

    assert result == expected_result, f"Expected: {expected_result}, but got: {result}"


# Test Case 5: XP is 2000 (Should be Advanced with Sage ascended title)
def test_5():
    xp = 200000
    result = wizard_progress(xp)

    expected_result = "Wizard's Level: 62, Job Title: Commoner, Ascended Title: Apprentice, Class Challenges Completed: 12, Extra Hard Class Challenges Completed: 0"

    assert result == expected_result, f"Expected: {expected_result}, but got: {result}"

def test_6():
    xp = 600000
    result = wizard_progress(xp)

    expected_result = "Wizard's Level: 109, Job Title: Advanced, Ascended Title: Mage, Class Challenges Completed: 21, Extra Hard Class Challenges Completed: 1"

    assert result == expected_result, f"Expected: {expected_result}, but got: {result}"

def test_7():
    xp = 3900000
    result = wizard_progress(xp)

    expected_result = "Wizard's Level: 278, Job Title: Grandmaster, Ascended Title: Sage, Class Challenges Completed: 55, Extra Hard Class Challenges Completed: 2"

    assert result == expected_result, f"Expected: {expected_result}, but got: {result}"


def test_8():
    xp = 60000000
    result = wizard_progress(xp)

    expected_result = "Wizard's Level: 1094, Job Title: Grandmaster, Ascended Title: Elder Mage, Class Challenges Completed: 218, Extra Hard Class Challenges Completed: 10"

    assert result == expected_result, f"Expected: {expected_result}, but got: {result}"
