with open('input.txt') as f:
    specs = [line.strip() for line in f.readlines()]

seats = set()
for spec in specs:
    seat_id = int(
        spec.replace('F', '0').replace('B', '1')
            .replace('L', '0').replace('R', '1'),
        2
    )
    seats.add(seat_id)

for i in range(min(seats), max(seats)):
    if i not in seats:
        my_seat = i

print("Part 1:", max(seats))
print("Part 2:", my_seat)
