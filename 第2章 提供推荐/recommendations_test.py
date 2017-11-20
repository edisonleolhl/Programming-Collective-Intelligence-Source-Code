# coding:utf-8
from pprint import pprint

from recommendations import critics

pprint (critics['Lisa Rose']['Lady in the Water'])
# 2.5
critics['Toby']['Snakes on a Plane'] = 4.5
pprint (critics['Toby'])
# {'Snakes on a Plane': 4.5, 'You, Me and Dupree': 1.0, 'Superman Returns': 4.0}

import recommendations

pprint (recommendations.sim_distance (recommendations.critics, 'Lisa Rose', 'Gene Seymour'))
# 0.14814814814814814  (different from book???)

pprint (recommendations.sim_pearson (recommendations.critics, 'Lisa Rose', 'Gene Seymour'))
# 0.39605901719066977  (the same as book)

# 为Toby寻找品味相同的用户
pprint (recommendations.topMatches (recommendations.critics, 'Toby', n=3))
# [(0.9912407071619299, 'Lisa Rose'),
# (0.9244734516419049, 'Mick LaSalle'),
# (0.8934051474415647, 'Claudia Puig')]

# 为Toby寻找他可能感兴趣的电影（基于用户的协作型过滤，用欧几里德距离作为相似度评估）
pprint (recommendations.getRecommendations (recommendations.critics, 'Toby'))
# [(3.3477895267131017, 'The Night Listener'),
# (2.8325499182641614, 'Lady in the Water'),
# (2.530980703765565, 'Just My Luck')]

# 为Toby寻找他可能感兴趣的电影（基于用户的协作型过滤，用皮尔逊系数作为相似度评估）
pprint (recommendations.getRecommendations (recommendations.critics, 'Toby', similarity=recommendations.sim_distance))
# [(3.5002478401415877, 'The Night Listener'),
# (2.7561242939959363, 'Lady in the Water'),
# (2.461988486074374, 'Just My Luck')]

# 为Superman Returns寻找相似的电影
movies = recommendations.transformPrefs (recommendations.critics)
pprint (recommendations.topMatches (movies, 'Superman Returns'))
# [(0.6579516949597695, 'You, Me and Dupree'),
# (0.4879500364742689, 'Lady in the Water'),
# (0.11180339887498941, 'Snakes on a Plane'),
# (-0.1798471947990544, 'The Night Listener'),  # 这说明看过 Superman Returns 的人，可能不会喜欢 The Night Listener
# (-0.42289003161103106, 'Just My Luck')]

# 为Superman Return寻找合适的影评人
pprint (recommendations.getRecommendations (movies, 'Just My Luck'))
# [(4.0, 'Michael Phillips'), (3.0, 'Jack Matthews')]

# 计算物品相似度的数据集
itemsim = recommendations.calculateSimilarItems (recommendations.critics)
pprint (itemsim)
# {'Just My Luck': [(0.2222222222222222, 'Lady in the Water'),
#                   (0.18181818181818182, 'You, Me and Dupree'),
#                   (0.15384615384615385, 'The Night Listener'),
#                   (0.10526315789473684, 'Snakes on a Plane'),
#                   (0.06451612903225806, 'Superman Returns')],
#  ...
#  'You, Me and Dupree': [(0.4, 'Lady in the Water'),
#                         (0.18181818181818182, 'Just My Luck'),
#                         (0.14814814814814814, 'The Night Listener'),
#                         (0.05333333333333334, 'Superman Returns'),
#                         (0.05128205128205128, 'Snakes on a Plane')]}

# 基于物品的协作型过滤
pprint (recommendations.getRecommendedItems (recommendations.critics, itemsim, 'Toby'))
# [(3.182634730538922, 'The Night Listener'),
#  (2.5983318700614575, 'Just My Luck'),
#  (2.4730878186968837, 'Lady in the Water')]

# 载入数据集prefs
prefs = recommendations.loadMovieLens ()
# 查看MovieLens 100K数据集中用户87的评分情况
# pprint(prefs['87'])
# {'2001: A Space Odyssey (1968)': 5.0,
#  'Ace Ventura: Pet Detective (1994)': 4.0,
#   ...
#  'Young Guns II (1990)': 2.0}

# 为用户87推荐电影，基于用户的协作型过滤
# pprint(recommendations.getRecommendations(prefs, '87')[0:30])
# [(5.0, 'They Made Me a Criminal (1939)'),
#  (5.0, 'Star Kid (1997)'),
#  (5.0, 'Santa with Muscles (1996)'),
#  ...
#  (4.367437266504598, 'Close Shave, A (1995)')]

# 基于物品的协作型过滤
# itemsim = recommendations.calculateSimilarItems(prefs, n=50)
# pprint(itemsim)
# 为用户87推荐电影，基于物品的协作型过滤
# pprint(recommendations.getRecommendedItems(prefs, itemsim, '87')[0:30])
# [(5.0, "What's Eating Gilbert Grape (1993)"),
#  (5.0, 'Vertigo (1958)'),
#  ...
#  (4.75, 'Broken English (1996)')]


# 课后练习3：计算用户相似度的数据集
usersim = recommendations.calculateSimilarUsers (prefs, n=50)
# pprint(usersim)
# {
#     '99': [(1.0, '375'),
#            (0.5, '855'),
#             ...
#            (0.125, '147'),
#            (0.125, '111')]
#     ...
# }

# 课后练习3 ：基于用户算法的执行效率
pprint (recommendations.getRecommendations_exercise (prefs, '344', usersim)[0:30])
# [(5.0, 'Jackie Brown (1997)'),
#   ...
#  (3.4696191891071564, 'Cape Fear (1991)'),
#  (3.360001033003341, 'Hoodlum (1997)')]
