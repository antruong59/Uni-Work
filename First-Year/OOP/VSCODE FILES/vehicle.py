class Vehicle:
    def __init__(self, speed):
        self.speed = speed

class PassengerVehicle(Vehicle):
    def __init__(self, seats):
        super().__init__(60)
        #self.speed += 1
        self.seats = seats
        #print(self.seats, self.speed)

class EmergencyVehicle(Vehicle):
    def __init__(self):
        super().__init__(100)
    
    def siren(self):
        print('Wee-oww Wee-oww!')

class Truck(Vehicle):
    def __init__(self, max_load):
        super().__init__(50)
        self.max_load = max_load

class Bus(PassengerVehicle):
    def __init__(self):
        super().__init__(35)
        #print(self.speed, self.seats)
        print('')

class Car(PassengerVehicle):
    def __init__(self):
        super().__init__(5)
        print('')

class Ambulance(EmergencyVehicle):
    def __init__(self):
        super().__init__()
        #print(self.speed)
        self.siren()
        self.checkVitalSign()

    def checkVitalSign(self):
        print('Beep, beep, beep...')

class FireEngine(EmergencyVehicle):
    def __init__(self):
        super().__init__()
        self.siren()
        self.sprayWater()

    def sprayWater(self):
        print('Splish Splash!')

class CementMixer(Truck):
    def __init__(self):
        super().__init__(10)
        print('')

class Pickup(Truck):
    def __init__(self):
        super().__init__(2)
        print('')


s = [FireEngine(), Pickup(), Car(), Ambulance(), Bus(), CementMixer()]
v = [FireEngine, Pickup, Car, Ambulance, Bus, CementMixer]
p = [EmergencyVehicle, PassengerVehicle, Truck]
v1 = ['FireEngine', 'Pickup', 'Car', 'Ambulance', 'Bus', 'CementMixer']
p1 = ['EmergencyVehicle', 'PassengerVehicle', 'Truck']

for x in range(len(v)):
    for y in range(len(p)):
        if issubclass(v[x], p[y]) == True:
            if p1[y] == 'PassengerVehicle':
                print(f'{v1[x]} is a subclass of {p1[y]}')
                print(f'v[{y}] is a {p1[y]} with {s[y].seats} seats, moving at {s[y].speed}km/h.')
        








