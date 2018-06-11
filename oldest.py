ages={
    "john":66,
    "ridd":99,
    "tt":20,
    "ll":50
}
oldest_person= None
current_biggest_age=0
for name in ages:
    age = ages[name]
    if age>current_biggest_age:
        oldest_person=name
        current_biggest_age=age
print(oldest_person)