with open('input.txt') as f:
    specs = [line.strip() for line in f.readlines()]

highest = 0
seats = set()
for spec in specs:
    row = int(spec[:7].replace('F', '0').replace('B', '1'), 2)
    col = int(spec[7:].replace('L', '0').replace('R', '1'), 2)
    seat_id = row * 8 + col
    seats.add(seat_id)
    highest = max(seat_id, highest)

for i in range(highest):
    if i in seats:
        continue
    if i-1 in seats and i+1 in seats:
        my_seat = i

print("Part 1:", highest)
print("Part 2:", my_seat)
