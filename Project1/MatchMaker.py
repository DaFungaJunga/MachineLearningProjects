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
kin = ctrl.Antecedent(np.arange(0, 11, 1), 'Children')
religion = ctrl.Antecedent(np.arange(0, 11, 1), 'Religion')
politic = ctrl.Antecedent(np.arange(0, 11, 1), 'Political Standing')

match = ctrl.Consequent(np.arange(0, 101, 1), "Match Likelihood")

# Auto-membership function population is possible with .automf(3, 5, or 7)
# age.automf(3)
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
kin.automf(3)
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

rule1 = ctrl.Rule(age['Legal'] & sexualO['Match'] | age['Legal'] & sexualO['Semi-Match'], match['Medium'])
rule2 = ctrl.Rule(education['poor'], match['Low'])
rule3 = ctrl.Rule(age['Not Legal'], match['Low'])
rule4 = ctrl.Rule(financial["good"], match['Medium'])
rule5 = ctrl.Rule(so["good"] & kin['average'], match['Low'])
rule6 = ctrl.Rule(personalC["good"], match['Medium'])
rule7 = ctrl.Rule(personalC["average"], match['High'])
rule8 = ctrl.Rule(habits["poor"], match['Low'])
rule9 = ctrl.Rule(kin["good"] & family["average"], match['Medium'])
rule10 = ctrl.Rule(beauty["good"], match['High'])
rule11 = ctrl.Rule(politic["average"], match['Medium'])
rule12 = ctrl.Rule(religion["average"], match['High'])
rule13 = ctrl.Rule(personalC["average"] & future["average"], match['Low'])
rule14 = ctrl.Rule(personalC["average"] & habits['average'], match['Medium'])
rule15 = ctrl.Rule(so["poor"], match['Medium'])
rule16 = ctrl.Rule(personalC['poor'], match['Low'])
rule17 = ctrl.Rule(financial["poor"], match['Low'])
rule18 = ctrl.Rule(personalC["good"] & so['average'], match['Medium'])
rule19 = ctrl.Rule(career["good"], match['Medium'])
rule20 = ctrl.Rule(future["average"], match['Medium'])

matching_ctrl = ctrl.ControlSystem(
    [rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9, rule10, rule11, rule12, rule13, rule14, rule15,
     rule16, rule17, rule18, rule19, rule20])

matching = ctrl.ControlSystemSimulation(matching_ctrl)
# Pass inputs to the ControlSystem using Antecedent labels with Pythonic API
# Note: if you like passing many inputs all at once, use .inputs(dict_of_data)


matching.input['Sexual Orientation'] = 1
matching.input['Age'] = 21
matching.input['Personal Characteristics'] = 6
matching.input['Education and Major'] = 8
matching.input['Financial Standing'] = 7
matching.input['Career'] = 7
matching.input['Habits'] = 5
matching.input['Significant Others'] = 1
#matching.input['Originality'] = 9
matching.input['Family'] = 6.6
matching.input['Future Plans'] = 5.5
matching.input['Beauty'] = 8
matching.input['Children'] = 1
matching.input['Religion'] = 6
matching.input['Political Standing'] = 6

matching.compute()

print(matching.output['Match Likelihood'])
rule1.view()
match.view(sim=matching)
while 1:
    print(1)
