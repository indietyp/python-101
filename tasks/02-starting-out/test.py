"""
You can execute this file to verify that your solution to all tasks is correct.

This file uses pytest and hypothesis to verify that your solution to each task is correct.

You can run this file with the following command:

    pytest tasks/02-starting-out/test.py


To install all the required packages, run the following command:

    micromamba create -f environment.yml

"""
import datetime
import os
import math
from pathlib import Path
from unittest.mock import Mock, call

import hypothesis.strategies as st
from _pytest.monkeypatch import MonkeyPatch
from hypothesis import given

DIRECTORY = Path(__file__).parent

if os.environ.get("SOLUTIONS") == "1":
    DIRECTORY /= "solutions"


def mock_input(monkeypatch, values):
    """
    Mock the input() function to return a fixed value.
    """

    mock = Mock(side_effect=values)
    monkeypatch.setattr("builtins.input", mock)


def mock_print(monkeypatch):
    """
    Mock the print() function to do nothing.
    """

    mock = Mock()
    monkeypatch.setattr("builtins.print", mock)
    return mock


def test_task_00(monkeypatch):
    mock = mock_print(monkeypatch)

    with open(DIRECTORY / "00-hello-world.py") as file:
        exec(file.read())

    mock.assert_called_with("Hello, World!")


@given(name=st.text())
def test_task_01(name):
    with MonkeyPatch().context() as m:
        mock_input(m, [name])
        mock = mock_print(m)

        with open(DIRECTORY / "01-hello-name.py") as file:
            exec(file.read())

        mock.assert_called_with(f"Hello, {name}!")


@given(value=st.integers())
def test_task_02(value):
    with MonkeyPatch().context() as m:
        mock_input(m, [value])
        mock = mock_print(m)

        with open(DIRECTORY / "02-add-one.py") as file:
            exec(file.read())

        mock.assert_called_with(value + 1)


@given(lhs=st.integers(), rhs=st.integers())
def test_task_03(lhs, rhs):
    with MonkeyPatch().context() as m:
        mock_input(m, [lhs, rhs])
        mock = mock_print(m)

        with open(DIRECTORY / "03-primitive-calculator.py") as file:
            exec(file.read())

        mock.assert_called_with(lhs + rhs)


THIS_YEAR = datetime.datetime.now().year


@given(value=st.integers().filter(lambda x: x > 0).filter(lambda x: x < THIS_YEAR))
def test_task_04(value):
    with MonkeyPatch().context() as m:
        mock_input(m, [value])
        mock = mock_print(m)

        with open(DIRECTORY / "04-age-calculator.py") as file:
            exec(file.read())

        this_year = datetime.datetime.now().year
        expected = this_year - value

        mock.assert_called_with(expected)


@given(lhs=st.text(), rhs=st.text())
def test_task_05(lhs, rhs):
    with MonkeyPatch().context() as m:
        mock_input(m, [lhs, rhs])
        mock = mock_print(m)

        with open(DIRECTORY / "05-string-length-concat.py") as file:
            exec(file.read())

        output = f'Output: {lhs} {rhs}'
        length = f'Length: {len(lhs) + len(rhs) + 1}'

        mock.assert_has_calls([call(output), call(length)])


@given(celsius=st.floats().filter(lambda x: not math.isnan(x)))
def test_task_06(celsius):
    with MonkeyPatch().context() as m:
        mock_input(m, [celsius])
        mock = mock_print(m)

        with open(DIRECTORY / "06-temperature-conversion.py") as file:
            exec(file.read())

        fahrenheit = celsius * 9 / 5 + 32
        mock.assert_called_with(fahrenheit)


# Usually we would not filter by NaN or specify a value range,
# but these are exercises for beginners.
@given(
    radius=st.floats().filter(lambda x: 0 < x < 100).filter(lambda x: not math.isnan(x)))
def test_task_07(radius):
    with MonkeyPatch().context() as m:
        mock_input(m, [radius])
        mock = mock_print(m)

        with open(DIRECTORY / "07-calculate-circle-area.py") as file:
            exec(file.read())

        area = math.pi * radius**2
        mock.assert_called_with(area)


@given(bill=st.floats().filter(lambda x: not math.isnan(x)),
       tip=st.floats().filter(lambda x: not math.isnan(x)))
def test_task_08(bill, tip):
    with MonkeyPatch().context() as m:
        mock_input(m, [bill, tip])
        mock = mock_print(m)

        with open(DIRECTORY / "08-tip-calculator.py") as file:
            exec(file.read())

        tip = bill * tip / 100
        total = bill + tip

        amount = f"The tip amount is ${tip}"
        total = f"The total amount is ${total}"

        mock.assert_has_calls([call(amount), call(total)])


@given(text=st.text())
def test_task_09(text):
    with MonkeyPatch().context() as m:
        mock_input(m, [text])
        mock = mock_print(m)

        with open(DIRECTORY / "09-palindrome.py") as file:
            exec(file.read())

        if text == text[::-1]:
            mock.assert_called_with(f"{text} is a palindrome")
        else:
            mock.assert_not_called()
