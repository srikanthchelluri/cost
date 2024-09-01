from collections import defaultdict

config = None
with open('./config.txt', 'r') as f:
    config = f.readlines()

total = 0
items = []
for line in config:
    if line == '':
        continue

    print(line.strip())
    split_colon = [s.strip() for s in line.split(':')]

    if split_colon[0] == 'total':
        total = float(split_colon[1])
        continue

    split_semi_colon = [s.strip() for s in split_colon[1].split(';')]
    items.append({
        'name': split_colon[0],
        'price': float(split_semi_colon[0]),
        'people': [s.strip() for s in split_semi_colon[1].split(',')]
    })
print()

subtotal_people_to_price = defaultdict(float)
for item in items:
    price_per_person = item['price'] / len(item['people'])
    for person in item['people']:
        subtotal_people_to_price[person] += price_per_person

subtotal = sum([item['price'] for item in items])
print('subtotal', "%.2f" % subtotal)
print('total', "%.2f" % total, '\n')

total_people_to_price = defaultdict(float)
for person, person_subtotal_price in subtotal_people_to_price.items():
    total_people_to_price[person] = (person_subtotal_price / subtotal) * total

for person, person_total_price in total_people_to_price.items():
    print(person, "%.2f" % round(person_total_price, 2))
