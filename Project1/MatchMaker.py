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

rule21 = ctrl.Rule(origin["average"] & career["average"], match['Low'])
rule22 = ctrl.Rule(origin["good"] | kin["good"], match['High'])
rule23 = ctrl.Rule(origin["poor"], match['Low'])



matching_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9, rule10, rule11, rule12, rule13, rule14, rule15, rule16, rule17, rule18, rule19, rule20, rule21, rule22, rule23])

#TEST CASE 1
matching1 = ctrl.ControlSystemSimulation(matching_ctrl)
# Pass inputs to the ControlSystem using Antecedent labels with Pythonic API
# Note: if you like passing many inputs all at once, use .inputs(dict_of_data)

matching1.input['Sexual Orientation'] = 1
matching1.input['Age'] = 21
matching1.input['Personal Characteristics'] = 6
matching1.input['Education and Major'] = 8
matching1.input['Financial Standing'] = 7
matching1.input['Career'] = 7
matching1.input['Habits'] = 5
matching1.input['Significant Others'] = 1
matching1.input['Originality'] = 9
matching1.input['Family'] = 6.6
matching1.input['Future Plans'] = 5.5
matching1.input['Beauty'] = 8
matching1.input['Children'] = 1
matching1.input['Religion'] = 6
matching1.input['Political Standing'] = 6

matching1.compute()

print("Test Case 1 match likelihood: " + str(matching1.output['Match Likelihood']))
rule1.view()
match.view()
time.sleep(2)
match.view(sim=matching1)




#TEST CASE 2
matching2 = ctrl.ControlSystemSimulation(matching_ctrl)
# Pass inputs to the ControlSystem using Antecedent labels with Pythonic API
# Note: if you like passing many inputs all at once, use .inputs(dict_of_data)

matching2.input['Sexual Orientation'] = 2
matching2.input['Age'] = 27
matching2.input['Personal Characteristics'] = 3
matching2.input['Education and Major'] = 2
matching2.input['Financial Standing'] = 4
matching2.input['Career'] = 2
matching2.input['Habits'] = 4
matching2.input['Significant Others'] = 2
matching2.input['Originality'] = 4
matching2.input['Family'] = 2.6
matching2.input['Future Plans'] = 7.5
matching2.input['Beauty'] = 5
matching2.input['Children'] = 2
matching2.input['Religion'] = 2
matching2.input['Political Standing'] = 1

matching2.compute()

print("Test Case 2 match likelihood: " + str(matching2.output['Match Likelihood']))
rule1.view()
match.view()
time.sleep(2)
match.view(sim=matching2)


#TEST CASE 3
matching3 = ctrl.ControlSystemSimulation(matching_ctrl)
# Pass inputs to the ControlSystem using Antecedent labels with Pythonic API
# Note: if you like passing many inputs all at once, use .inputs(dict_of_data)

matching3.input['Sexual Orientation'] = 3
matching3.input['Age'] = 50
matching3.input['Personal Characteristics'] = 9
matching3.input['Education and Major'] = 9
matching3.input['Financial Standing'] = 1
matching3.input['Career'] = 9
matching3.input['Habits'] = 1
matching3.input['Significant Others'] = 1
matching3.input['Originality'] = 4
matching3.input['Family'] = 9
matching3.input['Future Plans'] = 9
matching3.input['Beauty'] = 1
matching3.input['Children'] = 9
matching3.input['Religion'] = 9
matching3.input['Political Standing'] = 9

matching3.compute()

print("Test Case 3 match likelihood: " + str(matching3.output['Match Likelihood']))
rule1.view()
match.view()
time.sleep(2)
match.view(sim=matching3)

#TEST CASE 4
matching4 = ctrl.ControlSystemSimulation(matching_ctrl)
# Pass inputs to the ControlSystem using Antecedent labels with Pythonic API
# Note: if you like passing many inputs all at once, use .inputs(dict_of_data)

matching4.input['Sexual Orientation'] = 1
matching4.input['Age'] = 99
matching4.input['Personal Characteristics'] = 5
matching4.input['Education and Major'] = 5
matching4.input['Financial Standing'] = 5
matching4.input['Career'] = 5
matching4.input['Habits'] = 5
matching4.input['Significant Others'] = 5
matching4.input['Originality'] = 5
matching4.input['Family'] = 5
matching4.input['Future Plans'] = 5
matching4.input['Beauty'] = 5
matching4.input['Children'] = 5
matching4.input['Religion'] = 5
matching4.input['Political Standing'] = 5

matching4.compute()

print("Test Case 4 match likelihood: " + str(matching4.output['Match Likelihood']))
rule1.view()
match.view()
time.sleep(2)
match.view(sim=matching4)

#TEST CASE 5
matching5 = ctrl.ControlSystemSimulation(matching_ctrl)
# Pass inputs to the ControlSystem using Antecedent labels with Pythonic API
# Note: if you like passing many inputs all at once, use .inputs(dict_of_data)

matching5.input['Sexual Orientation'] = 3
matching5.input['Age'] = 18
matching5.input['Personal Characteristics'] = 4
matching5.input['Education and Major'] = 1
matching5.input['Financial Standing'] = 9
matching5.input['Career'] = 1
matching5.input['Habits'] = 9
matching5.input['Significant Others'] = 9
matching5.input['Originality'] = 1
matching5.input['Family'] = 1
matching5.input['Future Plans'] = 5
matching5.input['Beauty'] = 9
matching5.input['Children'] = 0
matching5.input['Religion'] = 0
matching5.input['Political Standing'] = 1

matching5.compute()

print("Test Case 5 match likelihood: " + str(matching5.output['Match Likelihood']))
rule1.view()
match.view()
time.sleep(2)
match.view(sim=matching5)