class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        self.price = price
        if price > 10000:
            self.tax = .15
        else:
            self.tax = .12
        self.display_all()

    def display_all(self):
        print 'Price:' + str(self.price)
        print 'Speed:' + str(self.speed) + 'mph'
        print 'Fuel:' + str(self.fuel)
        print 'Mileage:' + str(self.mileage) + 'mpg'
        print 'Tax:' + str(self.tax)


car1 = Car(2000, 50, 'Full', 100)
