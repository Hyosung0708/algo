blood_type = ['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']


blood_dict = {
    'A': 0,
    'B': 0,
    'AB': 0,
    'O': 0,
}

for blood in blood_list:
    blood_dict[blood] += 1

print(blood_dict)


location_list = ['서울', '부산', '서울', '서울', '대전', '제주', '광주', '부산']

location_dict = {
    '서울'
}

for location in location_list:
    if location in location_dict.keys():

    else:
        location_dict[location] = 1
        location['서울'] = 1