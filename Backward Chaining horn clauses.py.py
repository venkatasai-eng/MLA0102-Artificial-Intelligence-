kb = {
    "mammal(A)": ["vertebrate(A)"],
    "vertebrate(A)": ["animal(A)"],
    "bird(A)": ["vertebrate(A)", "flying(A)"],
    "vertebrate('duck')": [],
    "flying('duck')": [],
    "mammal('cat')": []
}

def backward_chain(goal):
    print(f"Goal: {goal}")
    if goal in kb and kb[goal] == []:
        print(f"{goal} is a known fact.")
        return True
    if goal in kb:
        for cond in kb[goal]:
            if not backward_chain(cond):
                print(f"{goal} cannot be proven.")
                return False
        print(f"{goal} proven using {kb[goal]}")
        return True
    print(f"{goal} cannot be proven.")
    return False

backward_chain("bird(A)")
