def main():
    """
    CP1404/CP5632 - Practical
    Broken program to determine score status
    """

    score = float(input("Enter score: "))
    result = test_score(score)
    print(result)


def test_score(score):
    if score < 0:
        return "Invalid score"
    else:
        if score > 100:
            return "Invalid score"
        elif score > 50:
            return "Passable"
        elif score > 90:
            return "Excellent"
        elif score < 50:
            return "Bad"


main()