import time

def countdown_timer(seconds):
    print(f"⏳ Starting countdown for {seconds} seconds")
    while seconds:
        mins, secs = divmod(seconds, 60)
        print(f"Time left: {mins:02}:{secs:02}", end='\r')
        time.sleep(1)
        seconds -= 1
    print("\n⏰ Time's up!")

try:
    user_seconds = int(input("Enter countdown time in seconds: "))
    countdown_timer(user_seconds)
except ValueError:
    print("⚠️ Please enter a valid number!")

countdown_timer()