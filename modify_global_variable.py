enemies = 1

def increase_enemies():
    global enemies
    enemies += 1
    print(f"count - {enemies}")

increase_enemies()
print(f"count - {enemies}")