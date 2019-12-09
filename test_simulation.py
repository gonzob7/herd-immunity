from Person import Person
from Simulation import Simulation
from Virus import Virus

HIV = Virus("HIV", 0.50, 0.3)

def test_virus_initializer():
    assert HIV.name == "HIV"
    assert HIV.reproduction_num == 0.50
    assert HIV.mortality_num == 0.3
