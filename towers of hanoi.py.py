def hanoi(n, source, aux, target):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    hanoi(n-1, source, target, aux)
    print(f"Move disk {n} from {source} to {target}")
    hanoi(n-1, aux, source, target)

hanoi(3, 'A', 'B', 'C')