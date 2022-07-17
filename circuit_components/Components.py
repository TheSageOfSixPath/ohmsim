from abc import ABC, abstractmethod


class Component(ABC):

    _terminal = {1: '', 2: ''}

    def __init__(self, ref_name, polarized=False):
        self._name = ref_name
        self._polarized = polarized
        self._terminal_count = len(self._terminal)

    @property
    def name(self, name):
        self._name = name

    @name.getter
    def name(self):
        return self._name

    @property
    def terminal_count(self):
        return self._terminal_count

    def hasPolarity(self):
        return self._polarized

    def getTerminals(self):
        return self._terminal

    @abstractmethod
    def setTerminals(self):
        pass

    @abstractmethod
    def getTerminalVal(self, key):
        pass

    @abstractmethod
    def getPropertyValue(self):
        pass

    @abstractmethod
    def getComponentType(self):
        pass


class PassiveComponent(Component):
    def __init__(self, ref_name, max_pow=0, polarized=False):
        Component.__init__(self, ref_name, polarized)
        self._max_absorbing_power = 0 - max_pow

    def getMaxPower(self):
        return self._max_absorbing_power

    @abstractmethod
    def setTerminals(self):
        pass

    @abstractmethod
    def getTerminalVal(self, key):
        pass

    @abstractmethod
    def getPropertyValue(self):
        pass

    @abstractmethod
    def getComponentType(self):
        pass


class ActiveComponent(Component):
    def __init__(self, ref_name, max_pow=0, polarized=False):
        Component.__init__(self, ref_name, polarized)
        self._max_power_supply = max_pow

    def getMaxPower(self):
        return self._max_power_supply

    @abstractmethod
    def setTerminals(self):
        pass

    @abstractmethod
    def getTerminalVal(self, key):
        pass

    @abstractmethod
    def getPropertyValue(self):
        pass

    @abstractmethod
    def getComponentType(self):
        pass


class Connector(Component):
    @abstractmethod
    def setTerminals(self):
        pass

    @abstractmethod
    def getTerminalVal(self, key):
        pass

    @abstractmethod
    def getPropertyValue(self):
        pass

    @abstractmethod
    def getComponentType(self):
        pass


class CircuitElement(Component):
    @abstractmethod
    def setTerminals(self):
        pass

    @abstractmethod
    def getTerminalVal(self, key):
        pass

    @abstractmethod
    def getPropertyValue(self):
        pass

    @abstractmethod
    def getComponentType(self):
        pass
