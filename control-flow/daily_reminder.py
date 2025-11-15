Task = input("Enter your task: ")
Time_Bound = input("Is the task time-bound (yes/no)? ")
Priority = input("Priority (high/medium/low): ")

reminder_message = ""

match priority:
    case "high":
        reminder_message = f"PRIORITY ALERT: Focus on '{task}'. It is a high-level task."
    case "medium":
        reminder_message = f"Remember to tackle '{task}'. It has a medium priority."
    case "low":
        reminder_message = f"You can get to '{task}' when you have spare time. It is a low priority task."
    case _:
        # Handles any unknown priority input
        reminder_message = f"ATTENTION: Task '{task}' was given an unknown priority level."

if time_bound == "yes":
    reminder_message += " that requires immediate attention today!"

print("-" * 40)
print("--- Daily Task Reminder ---")
print(reminder_message)
print("-" * 40)