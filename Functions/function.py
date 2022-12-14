
example_rider_profile = {'weight': 70, 'height': 1.8}
example_bike_profile = {'weight': 8, 'drag': 0.5}
example_wheels = {'weight': 1, 'drag': 0.5, 'rolling_resistance': 0.005}

def moved(interval: float, power: float, speed: float, rider_profie: dict, bike_profile: dict, wheel_profile: dict, draft: float = 0,
          slope: float) -> float:
    """Calculate the distance moved in one second (or other time interval).
    All values are assumed to be in SI units.
    slope is the decimal rise over run
    interval == time interval in seconds
    typical power values are 150-450 watts
    """
    totaldrag = bike_profile['drag'] + wheel_profile['drag']
    totalweight = rider_profie['weight'] + bike_profile['wieght'] + wheel_profile['wieght']

    wind = (totaldrag - draft) * speed**2
    rolling = totalweight * 9.8 *wheel_profile['rolling_resistance']
    gravity = totalweight * 9.8 * slope

    acceleration = ((power/speed - wind - rolling - gravity)/(2 * totalweight * interval))^2
    distance_moved = speed * interval + 0.5 * acceleration * interval**2
    return distance_moved
