rooms = {
    'A': 'Dirty',
    'B': 'Dirty',
    'C': 'Clean',
    'D': 'Dirty'
}

def vacuum():
    for room in rooms:
        print("Vacuum at", room, "- Status:", rooms[room])
        if rooms[room] == 'Dirty':
            rooms[room] = 'Clean'
            print("Cleaned", room)
        print()

vacuum()

print("Final:", rooms)
