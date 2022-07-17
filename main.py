from circuit_components import Resistor as rstr

r1 = rstr.Resistor("R1", 2.5, 0.25)
print(r1.name)
print(r1.hasPolarity())
print(r1.terminal_count)
print(r1.getTerminals())
print(r1.getResistance())
print(r1.getPropertyValue())
print(r1.getComponentType())