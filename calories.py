import os

# Global variables (initialized with defaults)
food_list = []
calorie_goal = 2000
FILENAME = "calories.txt"

def add_food():
    name = input("Enter food name: ")
    try:
        calories = int(input("Enter calories: "))
        # Replacing the C struct with a simple dictionary
        food_list.append({"name": name, "calories": calories})
        print("Food added successfully!")
    except ValueError:
        print("Invalid input! Please enter a number for calories.")

def view_foods():
    if not food_list:
        print("No food entries yet.")
        return

    print("\n---- Food List ----")
    for i, food in enumerate(food_list, 1):
        print(f"{i}. {food['name']} - {food['calories']} kcal")

def total_calories():
    # Uses a generator expression to sum calories quickly
    return sum(food['calories'] for food in food_list)

def set_goal():
    global calorie_goal
    try:
        calorie_goal = int(input("Enter your daily calorie goal: "))
        print("Goal updated!")
    except ValueError:
        print("Invalid input!")

def save_to_file():
    try:
        with open(FILENAME, "w") as f:
            f.write(f"{calorie_goal}\n")
            # In Python, we don't strictly need to save the 'count' 
            # because lists track their own length, but we'll follow the C logic.
            f.write(f"{len(food_list)}\n")
            for food in food_list:
                f.write(f"{food['name']}|{food['calories']}\n")
    except Exception as e:
        print(f"Error saving file: {e}")

def load_from_file():
    global calorie_goal, food_list
    if not os.path.exists(FILENAME):
        return

    try:
        with open(FILENAME, "r") as f:
            lines = f.readlines()
            if lines:
                calorie_goal = int(lines[0].strip())
                # lines[1] would be the count, which we can skip in Python
                for line in lines[2:]:
                    if "|" in line:
                        name, cal = line.strip().split("|")
                        food_list.append({"name": name, "calories": int(cal)})
    except Exception:
        print("Starting with a fresh log.")

def main():
    load_from_file()

    while True:
        print("\n====== FITNESS CALORIE TRACKER ======")
        print("1. Add Food")
        print("2. View All Foods")
        print("3. View Total Calories")
        print("4. Set Calorie Goal")
        print("5. Save & Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            add_food()
        elif choice == '2':
            view_foods()
        elif choice == '3':
            total = total_calories()
            print(f"\nTotal Calories Today: {total} kcal")
            print(f"Goal: {calorie_goal} kcal")
            print(f"Remaining: {calorie_goal - total} kcal")
        elif choice == '4':
            set_goal()
        elif choice == '5':
            save_to_file()
            print("Data Saved. Stay Fit 💪")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
