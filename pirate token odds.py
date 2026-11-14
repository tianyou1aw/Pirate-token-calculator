import random
while True:
    attempts = 0
    pirate_token = random.randint(1,137500)
    while True:
        attempts += 1
        rarity2 = random.randint(1,137500)
    
        if rarity2 == pirate_token:
            print("You got it")
            print(f"{attempts} attempts")
            break
    

    choice = input("Roll again, Y/N?: ").upper()
    if choice != "Y":
        break
    
        
        
