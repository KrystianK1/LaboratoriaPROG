x = 1
sum = 0
numOfStudents = int(input("Wprowadz liczbe studentow:"))
while True:
    points = int(input(f"Wprowadz liczbe punktow studenta {x}: "))
    if points < 0 or points > 100:
        continue
    sum += points
    x+=1
    if x > numOfStudents:
        break
median = sum/numOfStudents
print("Średnia punktów uczniów wynosi:", median)