import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# New Antecedent/Consequent objects hold universe variables and membership
# functions

sexualO = ctrl.Antecedent(np.arrange(0, 4, 1), 'Sexual Orientation')
age = ctrl.Antecedent(np.arrange(0, 101, 1), 'Age')
personalC = ctrl.Antecedent(np.arrange(0, 10, 1), 'Personal Characteristics')
education = ctrl.Antecedent(np.arrange(0, 5, 1), 'Education and Major')
financial = ctrl.Antecedent(np.arrange(0, 11, 1), 'Financial Standing')
career = ctrl.Antecedent(np.arrange(0, 11, 1), 'Career')
habits = ctrl.Antecedent(np.arrange(0, 11, 1), 'Habits')
so = ctrl.Antecedent(np.arrange(0, 101, 1), 'Significant Others')
origin = ctrl.Antecedent(np.arrange(0, 11, 1), 'Originality')
family = ctrl.Antecedent(np.arrange(0, 11, 1), 'Family')
future = ctrl.Antecedent(np.arrange(0, 11, 1), 'Future Plans')
beauty = ctrl.Antecedent(np.arrange(0, 11, 1), 'Beauty')
religion = ctrl.Antecedent(np.arrange(0, 11, 1), 'Religion')
politic = ctrl.Antecedent(np.arrange(0, 11, 1), 'Political Standing')




