#!/usr/bin/env python
# -*- coding: utf-8 -*-


import math

def square_root(a: float) -> float:
    root = math.sqrt(a)
    return root


def square(a: float) -> float:
    square = a * a
    return square


def average(a: float, b: float, c: float) -> float:
    average = (a + b + c) / 3
    return average


def to_radians(angle_degs: float, angle_mins: float, angle_secs: float) -> float:
    radians = math.pi * (angle_degs + angle_mins / 60 + angle_secs / 3600) / 180
    return radians


def to_degrees(angle_rads: float) -> tuple:
    degrees = angle_rads * (180 / math.pi)
    minutes = (degrees - int(degrees)) * 60
    secondes = (minutes - int(minutes)) * 60

    return int(degrees), int(minutes), int(secondes)


def to_celsius(temperature: float) -> float:
    Tc = (temperature - 32) / 1.8
    return Tc


def to_farenheit(temperature: float) -> float:
    Tf = temperature * 1.8 + 32
    return Tf


def main() -> None:
    print(f"La racine carré de 144 est : {square_root(144)}")

    print(f"Le carré de 12 est : {square(12)}")

    print(f"Moyenne des nombres 2, 4, 6: {average(2, 4, 6)}")

    print(f"Conversion de 100 degres, 2 minutes et 45 secondes en radians: {to_radians(180, 2, 45)}")
    
    degrees, minutes, seconds = to_degrees(1.0)
    print(f"Conversion de 1 radian en degres: {degrees} degres, {minutes} minutes et {seconds} secondes")

    print(f"Conversion de 100 Celsius en Farenheit: {to_farenheit(100.0)}")
    print(f"Conversion de 451 Farenheit en Celsius: {to_celsius(451.0)}")


if __name__ == '__main__':
    main()
