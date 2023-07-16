"""
Write a program that allows the user to input a temperature in Celsius for a specific day
and time.

If asked the program should then print out the temperatures as well as statistics like:
- the average temperature
- the highest temperature
- the lowest temperature

The commands are:
- `add` - adds a temperature for a specific day and time
- `print` - prints the temperatures
- `done` - exits the application

Extra:
    - Instead of using strings for the date and time, use the `datetime` module.
    - Allow the user to input temperatures inline using `add <date> <time> <temperature>`.
    - Allow the user to save the temperatures to a file via `save <filename>`.
    - Allow the user to load the temperatures from a file via `load <filename>`.

Example:
    Input: add
    Date: 2021-01-01
    Time: 12:00
    Temperature: 10
    Input: add
    Date: 2021-01-01
    Time: 13:00
    Temperature: 11
    Input: add
    Date: 2021-01-01
    Time: 14:00
    Temperature: 12
    Input: add
    Date: 2021-01-01
    Time: 15:00
    Temperature: 13
    Input: print
    Output:
        2021-01-01 12:00: 10°C
        2021-01-01 13:00: 11°C
        2021-01-01 14:00: 12°C
        2021-01-01 15:00: 13°C
        ---
        Average: 11.5°C
        Highest: 13°C
        Lowest: 10°C
    Input: done
"""

# Write your code below this line 👇

import datetime

temperatures = {}
while True:
    command = input("Input: ")
    args = command.split()

    match args:
        case ["done"]:
            break
        case ["add", date, time, temperature]:
            date = datetime.datetime.strptime(date, "%Y-%m-%d")
            time = datetime.datetime.strptime(time, "%H:%M")
            date_time = datetime.datetime.combine(date, time.time())
            temperatures[date_time] = float(temperature)

        case ["print"]:
            print("Output:")
            print("\n".join(
                f"    {date_time}: {temperature}°C" for date_time, temperature in
                temperatures.items()))
            print("     ---")
            print(f"    Average: {sum(temperatures.values()) / len(temperatures):.1f}°C")
            print(f"    Highest: {max(temperatures.values())}°C")
            print(f"    Lowest: {min(temperatures.values())}°C")

        case ["save", filename]:
            with open(filename, "w") as file:
                for date_time, temperature in temperatures.items():
                    file.write(f"{date_time.isoformat()} {temperature}\n")
        case ["load", filename]:
            with open(filename, "r") as file:
                for line in file:
                    date_time, temperature = line.split()
                    date_time = datetime.datetime.fromisoformat(date_time)
                    temperatures[date_time] = float(temperature)
        case _:
            print("Invalid command")
