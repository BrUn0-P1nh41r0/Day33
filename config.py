def is_iss_close(my_lat, my_long, iss_lat, iss_long, threshold=5):
    """
    Check if the ISS is within a certain degree range of your location.

    Args:
        my_lat (float): Your latitude.
        my_long (float): Your longitude.
        iss_lat (float): ISS latitude.
        iss_long (float): ISS longitude.
        threshold (float): The degree range for closeness (default is 5).

    Returns:
        bool: True if the ISS is close, False otherwise.
    """
    lat_diff = abs(my_lat - iss_lat)
    long_diff = abs(my_long - iss_long)

    return lat_diff <= threshold and long_diff <= threshold