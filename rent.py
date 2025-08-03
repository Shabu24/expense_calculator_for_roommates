def chatty_input(prompt):
    """Gets input with a more conversational tone"""
    print()
    response = input(f"👉 {prompt} ").strip()
    return response

def friendly_rent_calculator():
    print("\nHey there! 👋 Let's figure out how to split those living expenses fairly.")
    print("I'll need some details about your shared costs. Ready when you are!\n")
    
    # Get basic info conversationally
    rent = float(chatty_input("First, what's the total rent for your place?"))
    roommates = int(chatty_input(f"Got it! ₹{rent} total rent. How many people are sharing this place?"))
    
    print("\nOkay, let's talk about other shared expenses...")
    food = float(chatty_input("How much did you all spend on food/groceries this month?"))
    
    print("\nNow about utilities...")
    units = float(chatty_input("How many electricity units did you use?"))
    unit_cost = float(chatty_input(f"And how much does each unit cost? (₹ per unit)"))
    
    print("\nAny other shared bills we should include?")
    internet = float(chatty_input("Internet bill amount? (Enter 0 if none)"))
    water = float(chatty_input("Water bill? (Enter 0 if none)"))
    print("\nGot all that! Let me crunch the numbers...\n")
    
    # Pause for dramatic effect
    import time
    time.sleep(1)
    print("🧮 Calculating...")
    time.sleep(1)
    
    # Do the math
    electricity = units * unit_cost
    total = rent + food + electricity + internet + water
    share = total / roommates
    
    # Explain the breakdown
    print(f"\nHere's the breakdown:")
    print(f"🏠 Rent: ₹{rent:.2f}")
    print(f"🍕 Food: ₹{food:.2f}")
    print(f"💡 Electricity: ₹{electricity:.2f} ({units} units @ ₹{unit_cost})")
    if internet > 0:
        print(f"🌐 Internet: ₹{internet:.2f}")
    if water > 0:
        print(f"🚰 Water: ₹{water:.2f}")
    
    print(f"\n💰 Total shared expenses: ₹{total:.2f}")
    print(f"👥 Split between {roommates} people")
    
    # Final result with personality
    if share < 1000:
        print(f"\nNot bad! Each person pays: ₹{share:.2f}")
    elif share < 5000:
        print(f"\nOof, that adds up! Each person pays: ₹{share:.2f}")
    else:
        print(f"\nYikes! That's steep. Each person pays: ₹{share:.2f}")
    
    print("\nHope this helps! Let me know if you need to calculate again 😊")

if __name__ == "__main__":
    friendly_rent_calculator()