from pprint import pprint

import treepredict

pprint (treepredict.divideset (treepredict.my_data, 2, 'yes'))
# ([['slashdot', 'USA', 'yes', 18, 'None'],
#   ['google', 'France', 'yes', 23, 'Premium'],
#   ['digg', 'USA', 'yes', 24, 'Basic'],
#   ['kiwitobes', 'France', 'yes', 23, 'Basic'],
#   ['slashdot', 'France', 'yes', 19, 'None'],
#   ['digg', 'New Zealand', 'yes', 12, 'Basic'],
#   ['google', 'UK', 'yes', 18, 'Basic'],
#   ['kiwitobes', 'France', 'yes', 19, 'Basic']],
#  [['google', 'UK', 'no', 21, 'Premium'],
#   ['(direct)', 'New Zealand', 'no', 12, 'None'],
#   ['(direct)', 'UK', 'no', 21, 'Basic'],
#   ['google', 'USA', 'no', 24, 'Premium'],
#   ['digg', 'USA', 'no', 18, 'None'],
#   ['google', 'UK', 'no', 18, 'None'],
#   ['kiwitobes', 'UK', 'no', 19, 'None'],
#   ['slashdot', 'UK', 'no', 21, 'None']])


print(treepredict.giniimpurity (treepredict.my_data))
# 0.6328125

print(treepredict.entropy (treepredict.my_data))
# 1.50524081494

set1, set2 = treepredict.divideset (treepredict.my_data, 2, 'yes')
print(treepredict.entropy (set1))
# 1.2987949407

print(treepredict.entropy (set2))
# 1.2987949407
