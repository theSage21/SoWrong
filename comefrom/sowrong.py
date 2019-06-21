wormholes = {}


class Comefrom:
    def __getattr__(self, x):
        print("comefrom", x)


class Label:
    def __getattr__(self, x):
        print("label", x)


comefrom, label = Comefrom(), Label()
