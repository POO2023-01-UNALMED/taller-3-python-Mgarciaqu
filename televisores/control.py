class Control:

    def __init__(self):
        self._TV = None

    def turnOn(self):
        self._TV.turnOn()

    def turnOff(self):
        self._TV.turnOff()

    def canalUp(self):
        self._TV.canalUp()

    def canalDown(self):
        self._TV.canalDown()

    def canalUp(self):
        self._TV.canalUp()

    def volumeDown(self):
        self._TV.volumeDown()

    def volumenUp(self):
        self._TV.volumenUp()

    def setCanal(self, canal):
        self._TV.setCanal(canal)

    def enlazar(self, televisor):
        self._TV = televisor
        self._TV.setControl(self)

    def setTV(self, televisor):
        self._TV = televisor

    def getTv(self):
        return self._TV
