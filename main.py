import ttg

# # prop_vars = [
# #     'p',  # It's rainy outside
# #     'q'   # I am inside
# # ]

# # prop_expressions = [
# #     'p and q', 
# #     'p or q', 
# #     '~p', 
# #     'p => q', 
# #     'p = q'
# # ]
# prop_vars = [
#     'P11',   #Pit in location(1,1)
#     'B11',
#     'P21',
#     'B21',
#     'P22',
#     'P31'
# ]

# prop_expressions = [
#     '~P11',  #There is no pit in location(1,1)
#     'B11 = (P11 or P21)',      #There is a breeze in 
#     'B21 = (P11 or P22 or P31)' # B2,1 ⇔ (P1,1 ∨ P2,2 ∨ P3,1).

# ]


# print(ttg.Truths(prop_vars, prop_expressions).as_prettytable())

# # perceptrons = [
# #     "~B11",
# #     "B21"
# # ]

# perceptrons = [
#     "~B11",
#     "B21"
# ]


# prop_expressions = prop_expressions + perceptrons

# print(ttg.Truths(prop_vars, prop_expressions))

'''
* If it is rainy outside I am inside
* If I am inside I am NOT outside and vice versa.
* If I am outside I am either in my car are on a walk
* If I am in my car, I am NOT on a walk and vice versa.
* IF I go on a walk I wear a sweater

Print out the truth table.

Now add two perceptrons:

* It is NOT raining outside
* I am on a walk

Print out the truth table again.'''

prop_vars = [
    "RainyOutside",
    "Inside",
    "Outside",
    "InCar",
    "OnWalk"
]
prop_expressions = [
    'RainyOutside => Inside',
    'Inside = ~Outside',
    'Outside => (InCar or OnWalk)  '
]
print(ttg.Truths(prop_vars, prop_expressions).as_prettytable())