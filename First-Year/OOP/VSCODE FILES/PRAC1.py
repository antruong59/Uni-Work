# task1
def distance(velocity, time):
    distanceTravelled = velocity * time
    return distanceTravelled

# task2
def kinetic_energy(velocity, mass):
    kinetic_energy = 0.5 * mass * velocity ^ 2
    return kinetic_energy

# task3
class MovingObject():
    def __init__(self, vel, time, mass):
        self.velocity = vel
        self.time = time
        self.mass = mass

    def distance(self):
        distanceTravelled = self.velocity * self.time
        return distanceTravelled

    def kinetic_energy(self):
        kineticEnergy = 0.5 * self.mass * (self.velocity ^ 2)
        return kineticEnergy

moving_obj = MovingObject(6, 12, 20)
print( 'The distance is:', moving_obj.distance(), 'meters')
print( 'The kinetic energy is:', moving_obj.kinetic_energy(), 'J')