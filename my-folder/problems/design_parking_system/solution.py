class ParkingSystem:
    parking=[0]*3
    def __init__(self, big: int, medium: int, small: int):
        self.parking[0] = big
        self.parking[1]=medium
        self.parking[2]=small

    def addCar(self, carType: int) -> bool:
        if self.parking[carType-1]:
            self.parking[carType-1]-=1
            return True
        return False


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)