"""
score
"""

def main():
    score = float(input("Enter your score : "))
    print(score_status(score))

def score_status(score):
    if score >= 50 and score < 90:
        print("Passable")
    elif score > 90 and score <= 100:
        print("Excellent")
    elif score >= 0 and score < 50:
        print("Bad")
    else:
        print("Invalid Score")

main()
