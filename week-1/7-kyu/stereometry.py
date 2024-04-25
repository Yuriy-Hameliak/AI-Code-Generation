'''https://www.codewars.com/kata/5970915e54c27bd71000007b/train/python'''

import math

def stereometry(r, h):
    """
    Calculates the surface area of the original sphere, area of the circle made by the cut,
    and perimeter of the circle.

    Args:
        r: Radius of the sphere.
        h: Distance between the centers of the sphere and the circle.

    Returns:
        A tuple containing the surface area of the sphere (rounded to 3 decimals),
        area of the circle (rounded to 3 decimals), 
        and perimeter of the circle (rounded to 3 decimals).
    """

    # Check if h is within valid range (0 <= h <= r)
    if h < 0 or h > r:
        raise ValueError("Distance h must be between 0 and the sphere's radius r.")

    # Calculate sphere surface area (4 * pi * r^2)
    sphere_surface_area = 4 * math.pi * (r**2)

    # Calculate circle radius (using Pythagorean theorem)
    circle_radius = math.sqrt(r**2 - h**2)

    # Calculate circle area (pi * r^2)
    circle_area = math.pi * (circle_radius**2)

    # Calculate circle perimeter (2 * pi * r)
    circle_perimeter = 2 * math.pi * circle_radius

    # Round all values to 3 decimal places
    sphere_surface_area = round(sphere_surface_area, 3)
    circle_area = round(circle_area, 3)
    circle_perimeter = round(circle_perimeter, 3)

    return sphere_surface_area, circle_area, circle_perimeter
