from random import random

class PopulationSimulation():

    def __init__(self, no_families):
        self.is_boy = None
        self.family = None
        self.population = no_families

    def boy_or_girl(self):
        if random() > 0.5:
            self.is_boy = 1
        else:
            self.is_boy = 0
        return self.is_boy

    def run_one_family(self):
        no_boys = 0
        no_girls = 0
        while no_girls == 0:
            child_sex = self.boy_or_girl()
            if child_sex == 1:
                no_boys = no_boys + 1
            else:
                no_girls = no_girls + 1
        self.family = (no_boys, no_girls)

        return self.family

    def run_n_families(self):
        total_boys = 0
        total_girls = 0

        for families in range(self.population):
            no_boys, no_girls = self.run_one_family()
            total_boys = total_boys + no_boys
            total_girls = total_girls + no_girls

        return total_girls/(total_girls + total_boys)



simulation = PopulationSimulation(5000)
print('Despite of Queens decreet, the ratio of girls to boys remains: {}'.format(simulation.run_n_families()))

