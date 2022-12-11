#Locate a number in a decreasing ordered list

from jovian.pythondsa import evaluate_test_case

def locate(cards, query):
    if bool(cards):   
        for count,num in enumerate(cards):
            if num==query:
                return count
    return -1
    

tests = []

tests.append({
    'input':{
        'cards': [13,11,10,7,4,3,1,0],
        'query': 7
        },
    'output': 3
    })

tests.append({
    'input':{
        'cards': [4,2,1,-1],
        'query': 4
        },
    'output': 0
    })

tests.append({
    'input':{
        'cards': [20,15,-5,-10],
        'query': -10
        },
    'output': 3
    })

tests.append({
    'input':{
        'cards': [3],
        'query': 3
        },
    'output': 0
    })

tests.append({
    'input':{
        'cards': [10,7,5,0],
        'query': 3
        },
    'output': -1
    })

tests.append({
    'input':{
        'cards': [],
        'query': 7
        },
    'output': -1
    })

tests.append({
    'input':{
        'cards': [10,8,8,7,3,2,0],
        'query': 7
        },
    'output': 3
    })

tests.append({
    'input':{
        'cards': [],
        'query': 7
        },
    'output': -1
    })


for i in tests:
    evaluate_test_case(locate, i)
  



    
    

