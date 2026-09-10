from client import ChaseLevDeque

def main():
    print("=== Testing Chase-Lev Work-Stealing Deque ===")
    deque = ChaseLevDeque(capacity=8)
    deque.push_bottom("TASK_A")
    deque.push_bottom("TASK_B")
    deque.push_bottom("TASK_C")

    stolen = deque.steal()
    print("Stealer stole:", stolen)
    assert stolen == "TASK_A"

    popped = deque.pop_bottom()
    print("Worker popped:", popped)
    assert popped == "TASK_C"

    print("=== All tests passed successfully! ===")

if __name__ == "__main__":
    main()
