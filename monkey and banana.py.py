initial_state = {'monkey': 'floor', 'box': 'corner', 'banana': 'ceiling', 'has_banana': False}

def move_box(s):
    if s['monkey'] == 'floor' and s['box'] == 'corner':
        s['box'] = 'under_banana'
        print("Monkey moves box under banana.")
    return s

def climb_box(s):
    if s['box'] == 'under_banana':
        s['monkey'] = 'on_box'
        print("Monkey climbs box.")
    return s

def grab_banana(s):
    if s['monkey'] == 'on_box':
        s['has_banana'] = True
        print("Monkey grabs banana.")
    return s

def monkey_banana():
    s = initial_state.copy()
    print("Initial State:", s)
    s = move_box(s)
    s = climb_box(s)
    s = grab_banana(s)
    print("Final State:", s)

monkey_banana()
