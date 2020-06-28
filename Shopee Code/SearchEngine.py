numTestCase = int(input())

testCases = {}

for i in range(numTestCase):
    testCases[i] = {}
    numItems, numQueries = input().split()

    for j in range(int(numItems)):
        if 'items' not in testCases[i]:
            testCases[i]['items'] = [input()]
        else:
            testCases[i]['items'].append(input())
    for j in range(int(numQueries)):
        if 'queries' not in testCases[i]:
            testCases[i]['queries'] = [input()]
        else:
            testCases[i]['queries'].append(input())

def checkQuery(item, query):
    itemName = item.split()
    queryName = query.split()

    if len(queryName) > len(itemName):
        return False
    else:
        for i in range(len(itemName)-len(queryName)+1):
            itemQuery = itemName[i:i+len(queryName)]
            if queryName == itemQuery:
                return True
        return False

for i in range(len(testCases)):
    items = testCases[i]['items']
    queries = testCases[i]['queries']
    print(f'Case {i+1}:')
    for query in queries:
        counter = 0
        for item in items:
            if checkQuery(item, query):
                counter += 1
        print(counter)
