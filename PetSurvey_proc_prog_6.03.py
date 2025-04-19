survey_responses = []

def get_yes_no(q): 
    a = input(q).strip().lower() 
    return a if a in ["yes", "no"] else get_yes_no(q)

def survey():
    print("Pet Surrender Survey (Yes/No only)")
    ans = [get_yes_no(q) for q in [
        "1. Financial constraints? ", 
        "2. Behavioral problems? ", 
        "3. Trial adoption help? ", 
        "4. Education on behavior? "]]
    survey_responses.append(ans)

def show():
    if not survey_responses: 
        print("No responses yet.")
        return
    print("\nFinancial, Behavior, Trial, Education")
    for r in survey_responses:
        print(r[0].capitalize(), r[1].capitalize(), r[2].capitalize(), r[3].capitalize())
    total = len(survey_responses)
    counts = [sum(1 for r in survey_responses if r[i] == "yes") for i in range(4)]
    print("\nYes%     : " +
          str(round(counts[0]*100/total, 1)) + "%" + ", " +
          str(round(counts[1]*100/total, 1)) + "%" + ", " +
          str(round(counts[2]*100/total, 1)) + "%" + ", " +
          str(round(counts[3]*100/total, 1)) + "%")


def main():
    while True:
        c = input("\n1=Survey 2=Show Table 3=Exit: ")
        if c == "1": survey()
        elif c == "2": show()
        elif c == "3": break

main()
