import numpy as np
import skfuzzy as fuzz
import matplotlib
from skfuzzy import control as ctrl
import time

# New Antecedent/Consequent objects hold universe variables and membership
# functions

sexualO = ctrl.Antecedent(np.arange(0, 4, 1), 'Sexual Orientation')
age = ctrl.Antecedent(np.arange(0, 101, 1), 'Age')
personalC = ctrl.Antecedent(np.arange(0, 11, 1), 'Personal Characteristics')
education = ctrl.Antecedent(np.arange(0, 11, 1), 'Education and Major')
financial = ctrl.Antecedent(np.arange(0, 11, 1), 'Financial Standing')
career = ctrl.Antecedent(np.arange(0, 11, 1), 'Career')
habits = ctrl.Antecedent(np.arange(0, 11, 1), 'Habits')
so = ctrl.Antecedent(np.arange(0, 11, 1), 'Significant Others')
origin = ctrl.Antecedent(np.arange(0, 11, 1), 'Originality')
family = ctrl.Antecedent(np.arange(0, 11, 1), 'Family')
future = ctrl.Antecedent(np.arange(0, 11, 1), 'Future Plans')
beauty = ctrl.Antecedent(np.arange(0, 11, 1), 'Beauty')
religion = ctrl.Antecedent(np.arange(0, 11, 1), 'Religion')
politic = ctrl.Antecedent(np.arange(0, 11, 1), 'Political Standing')

match = ctrl.Consequent(np.arange(0, 101, 1), "Match Likelihood")

# Auto-membership function population is possible with .automf(3, 5, or 7)
#age.automf(3)
personalC.automf(3)
education.automf(3)
financial.automf(3)
career.automf(3)
habits.automf(3)
so.automf(3)
origin.automf(3)
family.automf(3)
future.automf(3)
beauty.automf(3)
religion.automf(3)
politic.automf(3)

# Custom membership functions can be built interactively with a familiar,
# Pythonic API
age['Not Legal'] = fuzz.trimf(age.universe, [0, 0, 18])
age['Legal'] = fuzz.trimf(age.universe, [18, 18, 60])
age['Old'] = fuzz.trimf(age.universe, [60, 100, 100])

sexualO['Match'] = fuzz.trimf(sexualO.universe, [0, 0, 1])
sexualO['Semi-Match'] = fuzz.trimf(sexualO.universe, [0, 1, 2])
sexualO['No Match'] = fuzz.trimf(sexualO.universe, [2, 3, 3])

match['Low'] = fuzz.trimf(match.universe, [0, 0, 33])
match['Medium'] = fuzz.trimf(match.universe, [0, 33, 67])
match['High'] = fuzz.trimf(match.universe, [67, 100, 100])

rule1 = ctrl.Rule(age['Legal'] & sexualO['Match'] | age['Legal'] & sexualO['Semi-Match'], match['Low'])

