# Break Reminder

This is a simple Python script that reminds you to take a break every 20 minutes.

## Dependencies

This script uses the following Python libraries:

- `keyboard`
- `win10toast`

You can install these using pip:

```bash
pip install -r requirements.txt
```
# Usage 

Run the script using Python:

```bash
python main.pyw
```
The script will display a notification every 20 minutes reminding you to get up and move. Press the 'F8' key to stop the script.

# Add to Startup(Windows)

To have this script run automatically when you start your computer, follow these steps:

1. Create a shortcut of the `main.pyw` file.
2. Press `Win + R` to open the Run dialog.
3. Type `shell:startup` and press Enter. This will open the Startup folder.
4. Copy the shortcut to the Startup folder.

Now, the script will run automatically every time you start your computer.

# License
This project is licensed under the terms of the Apache License.