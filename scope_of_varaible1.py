enemies = 1

def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")

inrease_enemies()
print(f"enemies outside function: {enemies}")