#!/usr/bin/python
#
#JulioGomez
#
#this program will tell us how many hours it takes to travel a certain amount of miles
#

def convert_hours(distance, speed):
    """
    this will convert to hours
    :param hours:
    :return:
    """
    hours = distance/speed
    return hours


def main():
    """
    This is the main functions
    :return:
    """
    user_distance = input("How far will you be traveling today? ")
    user_speed = input("At what speed will you be traveling? ")
    print str(convert_hours(float(user_distance), user_speed)) + " hours"

main()