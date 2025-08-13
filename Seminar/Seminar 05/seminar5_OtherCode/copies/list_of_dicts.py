import copy
from colorama import Fore, Style


def copy_list_of_dicts(lst: list) -> list:
    list_copy = []
    for elem_dict in lst:
        new_dict = {}
        for key, value in elem_dict.items():
            new_dict[key] = value
        list_copy.append(new_dict)

    return list_copy


#V1: append la aceeasi lista
l1 = [{'key1': 10, 'key2': 18}, {'key1': 3, 'key2': 18}]
undo_list = []
undo_list.append(l1)
print("Initial l1:", l1)
print("Initial undo_list:", undo_list)

print(Fore.GREEN + "Executing l1.append({'key1': 10, 'key2': 18})..." + Style.RESET_ALL)
l1.append({'key1': 10, 'key2': 18})

print("l1:", l1)
print("undo_list:", undo_list)
print('ID l1:', id(l1))
print('ID undo_list[0]', id(undo_list[0]))

print(Fore.GREEN + "Executing l1[0] = {'key1': -55, 'key2': -22}..." + Style.RESET_ALL)

l1[0] = {'key1': -55, 'key2': -22}
print("l1:", l1)
print("undo_list:", undo_list)

print('----' * 25)

#V2: .copy() sau [:]
print('Shallow copy:')
l2 = [{'key1': 10, 'key2': 18}, {'key1': 3, 'key2': 18}]
l2_copy = l2.copy()

print(Fore.MAGENTA + "IDs:" + Style.RESET_ALL)
print('ID lista originala (l2):', id(l2))
print('ID copie lista (l2_copy):', id(l2_copy))
print('ID-uri elemente din lista:')
for i in range(len(l2)):
    print(f'id(l2[{i}])={id(l2[i])}')
    print(f'id(l2_copy[{i}])={id(l2_copy[i])}')

print(Fore.MAGENTA + "Modificari cu shallow list:" + Style.RESET_ALL)
print(Fore.GREEN + "Executam l2[0]['key1'] = -55..." + Style.RESET_ALL)

l2[0]['key1'] = -55
print('l2', l2)
print('l2_copy', l2_copy)

undo_list2 = []
undo_list2.append(l2_copy)
print(Fore.GREEN + "Executing l2.append({'key1': 100, 'key2': 8})" + Style.RESET_ALL)

l2.append({'key1': 100, 'key2': 8})

print('l2', l2)
print('l2_copy', l2_copy)
print('undo_list', undo_list2)

print(Fore.GREEN + "l2[0]['key1'] = 99" + Style.RESET_ALL)

l2[0]['key1'] = 99
print('l2', l2)
print('l2_copy', l2_copy)
print('undo_list', undo_list2)

# V3: copy.deepcopy() sau propria noastra functie de copiere
print('----' * 25)
print("Deep copy:")

l3 = [{'key1': 10, 'key2': 18}, {'key1': 3, 'key2': 18}]
l3_copy = copy_list_of_dicts(l3)

print(Fore.MAGENTA + "IDs:" + Style.RESET_ALL)
print(f'id(l3)={id(l3)}')
print(f'id(l3_copy)={id(l3_copy)}')

for i in range(len(l3)):
    print(f'id(l3[{i}])={id(l3[i])}')
    print(f'id(l3_copy[{i}])={id(l3_copy[i])}')

print(Fore.GREEN + "Executing l3[0]['key1'] = -55" + Style.RESET_ALL)

l3[0]['key1'] = -55
print('l3', l3)
print('l3_copy', l3_copy)

undo_list3 = []
undo_list3.append(l3_copy)
print(Fore.GREEN + "Executing l3.append({'key1': 100, 'key2': 8})" + Style.RESET_ALL)

l3.append({'key1': 100, 'key2': 8})
print('l3', l3)
print('l3_copy', l3_copy)
print('undo_list', undo_list3)

print(Fore.GREEN + "Executing l3[0]['key1'] = 99" + Style.RESET_ALL)

l3[0]['key1'] = 99
print('l3', l3)
print('l3_copy', l3_copy)
print('undo_list', undo_list3)
