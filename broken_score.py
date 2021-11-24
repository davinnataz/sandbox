"""
score
"""

def main():
    score = getscore()
    print(score_status(score))

def getscore():
    score =  float(input("Enter your score : "))

def score_status():
    if score >= 50 and score < 90:
        print("Passable")
    elif score > 90 and score <= 100:
        print("Excellent")
    elif score >= 0 and score < 50:
        print("Bad")
    else:
        print("Invalid Score")

