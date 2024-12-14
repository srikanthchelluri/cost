from collections import defaultdict

# Read and parse config
with open('./config.txt', 'r') as f:
    config = [line.strip() for line in f if line.strip()]

total = 0
items = []
for line in config:
    key, value = map(str.strip, line.split(':'))
    if key == 'total':
        total = float(value)
    else:
        price, people = map(str.strip, value.split(';'))
        items.append({
            'name': key,
            'price': float(price),
            'people': 'all' if people == 'all' else [p.strip() for p in people.split(' ')]
        })

# Determine unique people
all_people = list(set(p for item in items for p in (item['people'] if item['people'] != 'all' else [])))

# Calculate subtotals
subtotal_people_to_price = defaultdict(float)
for item in items:
    people = all_people if item['people'] == 'all' else item['people']
    price_per_person = item['price'] / len(people)
    for person in people:
        subtotal_people_to_price[person] += price_per_person

# Calculate total
subtotal = sum(item['price'] for item in items)
total_people_to_price = {
    person: (person_subtotal / subtotal) * total
    for person, person_subtotal in subtotal_people_to_price.items()
}

# Print results
print(f"subtotal: {subtotal:.2f}")
print(f"total: {total:.2f}\n")
for person, person_total_price in total_people_to_price.items():
    print(f"{person}: {person_total_price:.2f}")
