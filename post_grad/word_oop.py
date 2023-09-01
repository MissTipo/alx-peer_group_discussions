'''
module(lA, lB):
    if obstruction:
        return true
    return False

    for obstruction

    if d_time - e_time >= 60 mins:
        obstruction is impenetrable

    else:
        penetrable


    From another member

    TimeDuration(pointA, pointB) -> 78mins

    Module(pointA, pointB) -> 15.2mins 78


'''
import math


class Obstruction:
    '''Determine obstruction and if it is penetrable or not'''
    timeDuration = 8
    machine_speed = 1

    def __init__(self, p_a, p_b):
        '''Iniitalize the class'''
        self.p_a = p_a
        self.p_b = p_b

    def distance(self):
        '''Determines the distance b/w p_a and p_b.'''
        # Radius of the Earth in miles
        earth_radius = 3958.8  # Mean radius in miles

        # Convert latitude and longitude from degrees to radians
        lat1_rad = math.radians(self.p_a[0])
        lon1_rad = math.radians(self.p_a[1])
        lat2_rad = math.radians(self.p_b[0])
        lon2_rad = math.radians(self.p_b[1])

        # Differences between the coordinates
        delta_lat = lat2_rad - lat1_rad
        delta_lon = lon2_rad - lon1_rad

        # Haversine formula
        a = math.sin(delta_lat / 2) ** 2 + math.cos(lat1_rad) * \
            math.cos(lat2_rad) * math.sin(delta_lon / 2) ** 2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

        # Calculate distance
        distance = earth_radius * c
        return distance

    def time_taken(self):
        '''Calculate the time taken'''

        dist = self.distance()

        time = dist / self.machine_speed

        return time

    def obstruction(self):
        '''Gives final report'''
        expected_time = self.time_taken()

        return (self.timeDuration > expected_time)

    def impenetrable(self):
        '''Determines if the obstruction is penetrable or not'''

        if self.obstruction():
            return ((self.timeDuration - self.time_taken()) >= 60)

        return False

    # THE END.


PointA = [53.5872, -2.4138]
PointB = [53.474, -2.2388]

test = Obstruction(PointA, PointB)
print('Distance =', test.distance())
print()
print('Time taken =', test.time_taken())
print()
print('Obstruction?', test.obstruction())
print()
print('Impenetrable?', test.impenetrable())
