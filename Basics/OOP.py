class Auto():
    def __init__(self, maxspeed = "", colour = ""):
        super(Auto, self).__init__()
        self.maxspeed = maxspeed
        self.colour = colour


class Autotyp(Auto):
    def __init__(self, brand, *args, **kwargs):
        super(Autotyp, self).__init__(*args, **kwargs)
        self.brand = brand



if __name__ == "__main__":
    EinAuto = Auto(299, "brown")
    EinBMW = Autotyp(brand="bmw", colour="red")
    print(EinBMW.maxspeed)