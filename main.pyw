import time
import keyboard
from win10toast import ToastNotifier

# Function to display a notification
def display_notification():
    # Create a ToastNotifier object
    toaster = ToastNotifier()
    # Display a toast notification with a title and message for 10 seconds
    toaster.show_toast("Get Up and Move!", "It's time to take a break and stretch your legs.", duration=10)

# Main function
def main():
    # Infinite loop
    while True:
        # Check if the 'f8' key is pressed
        if keyboard.is_pressed('f8'):  
            # Print a message to the console
            print('You Pressed A Key!')
            # Break the loop
            break  
        # Call the function to display a notification
        display_notification()
        # Pause the execution of the program for 1200 seconds (20 minutes)
        time.sleep(1200)  

# Check if this script is the main program and not being imported as a module
if __name__ == "__main__":
    # Call the main function
    main()