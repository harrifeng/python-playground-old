# coding: utf-8

cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpoll_capacity = cars_driven * space_in_a_car
averge_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "ddrivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpoll_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", averge_passengers_per_car, "in each car."
