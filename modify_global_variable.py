enemies = 1

def increase_enemies():
    global enemies
    enemies += 1
    print(f"count - {enemies}")

increase_enemies()
print(f"count - {enemies}")

# Normally constants are written down in uppercase
PI = 3.1415
URL = "www.google.com"