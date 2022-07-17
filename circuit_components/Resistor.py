from circuit_components import Components


class Resistor(Components.PassiveComponent):
    def __init__(self, ref_name, resistance, max_pow=0):
        Components.PassiveComponent.__init__(self, ref_name, max_pow)
        self._resistance = resistance

    def getResistance(self):
        return self._resistance

    def setTerminals(self):
        pass

    def getTerminalVal(self, key):
        pass

    def getPropertyValue(self):
        return self._resistance

    def getComponentType(self):
        return "Resistor"
