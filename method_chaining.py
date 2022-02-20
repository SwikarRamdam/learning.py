class car:
    def start(self):
        print("start")
        return self
    def move(self):
        print("Moving")
        return self
    def brake(self):
        print("Brake applied")
        return self
    def stop(self):
        print("stop")
        return self

vehicle = car()
# vehicle.start().move().brake().stop()
vehicle.start()\
    .move()\
    .brake()\
    .stop()