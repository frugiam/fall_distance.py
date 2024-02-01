# Author: Michelle Frugia
# GitHub username: frugiam
# Date: 01/31/2024
# Description: Project 4a

def fall_distance(time):
    """
    Calculate the distance an object falls due to gravity in a specific time period.

    Args:
    time (float): The time in seconds.

    Returns:
    float: The distance in meters.
    """
    # Acceleration due to gravity (m/s^2)
    g = 9.8

    # Calculate the distance using the formula 1/2gt^2
    distance = 1/2 * g * time * time
    # Round the distance to three decimal places
    distance = round(distance,3)
    # Return distance
    return distance