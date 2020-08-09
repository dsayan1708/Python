class Phone:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def cameraa(self):
        raise NotImplementedError("This method must be defined in each and every subclass")

class SmartPhone(Phone):
    def __init__(self, brand, model, camera):
        super().__init__(brand, model)
        self.camera = camera

class FlagshipPhone(Phone):
    def __init__(self, brand, model, front_camera, rear_camera):
        super().__init__(brand, model)
        self.front_camera = front_camera
        self.rear_camera = rear_camera

S = SmartPhone("POCO", "X2", "64MP")
print(S.cameraa())