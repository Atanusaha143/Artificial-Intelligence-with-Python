RomaniaMap = {
'Arad':['Zerind','Timisoara','Sibiu'],
'Zerind':['Arad','Oradea'],
'Oradea':['Zerind','Sibiu'],
'Sibiu':['Arad','Oradea','Fagaras','Rimnicu Vilcea'],
'Fagaras':['Sibiu','Bucharest'],
'Timisoara':['Arad','Lugoj'],
'Lugoj':['Timisoara','Mehadia'],
'Mehadia':['Lugoj','Drobeta'],
'Drobeta':['Mehadia','Craiova'],
'Craiova':['Drobeta','Rimnicu Vilcea','Pitesti'],
'Rimnicu Vilcea':['Sibiu','Craiova','Pitesti'],
'Pitesti':['Rimnicu Vilcea','Craiova','Bucharest'],
'Bucharest':['Fragras','Pitesti','Giurhiu','Urziceni'],
'Giurgiu':['Bucharest'],
'Urziceni':['Vaslui','Hirsova'],
'Eforie':['Hirsova'],
'Hirsova':['Urziceni','Eforie'],
'Vaslui':['Urziceni','Iasi'],
'Iasi':['Vaslui','Neamt']
}

def find_path(RomaniaMap, start, end, path = []):
    path = path + [start]
    if start not in RomaniaMap:
        return 0
    if start == end:
        return path
    for state in RomaniaMap[start]:
        if state not in path:
            if bool(find_path(RomaniaMap,state,end,path)):
                return find_path(RomaniaMap,state,end,path)

starting = input("Enter start position: ")
finishing = input("Enter end position: ")
ans = find_path(RomaniaMap,starting,finishing)
if ans == 0:
    print('Inavlid Input')
else:
    print('Path from {} to {} is : ' .format(starting,finishing))
    check = 0
    for i in range(len(ans)):
        if i is 0:
            print(ans[i], end = " ")
        else:
            print('-> ', ans[i], end = " ")
