Erin_GPA=4.5
Erin_score=75

if Erin_GPA>=3.5:
    if 50<=Erin_score<=65:
        print("Partial Scholarship")
    elif Erin_score>65:
        print("Full Scholarship")
    else:
        print("No Scholarship")
else:
    print("No Scholarship")