new_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def duplicate_valor(element):
    return element*2

def es_par(element):
    if(element % 2 == 0):
        return True
    else:
        return False

map_list = map(duplicate_valor, new_list)
filter_list = filter(es_par, new_list)

print(new_list)
print(list(map_list))
print(list(filter_list))