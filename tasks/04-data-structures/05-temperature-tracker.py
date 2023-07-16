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
