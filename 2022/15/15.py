def parse(file):
    sensors = []
    beacons = set()
    with open(file) as f:
        for line in f.readlines():
            line = line.strip().replace(',', '').replace(':', '')
            p = line.split()

            sensor = (
                int(p[2].split('=').pop()),
                int(p[3].split('=').pop()),
            )

            beacon = (
                int(p[8].split('=').pop()),
                int(p[9].split('=').pop()),
            )

            d = distance(sensor, beacon)

            y_range = sensor[1] - d, sensor[1] + d

            sensors.append((sensor, d, y_range))
            beacons.add(beacon)

    return sensors, beacons

def distance(a, b):
    ax, ay = a
    bx, by = b
    return abs(bx - ax) + abs(by - ay)

def range_at_y(y, sensor, d):
    delta_y = y - sensor[1]
    if delta_y < 0:
        delta_y = -delta_y

    if delta_y > d:
        return None

    delta_x = d - delta_y

    return sensor[0] - delta_x, sensor[0] + delta_x

def sensor_ranges(y, sensors):
    ranges = []
    for s, d, (bottom, top) in sensors:
        if not (bottom < y < top):
            continue
        sensor_range = range_at_y(y, s, d)
        if sensor_range is not None:
            ranges.append(sensor_range)
    return ranges

def find_beacon(sensors, m):
    for y in range(0, m + 1):
        ranges = sensor_ranges(y, sensors)
        x = 0
        while True:
            previous = x
            for first, last in ranges:
                if first <= x <= last:
                    x = last + 1
            if x == previous:
                break

        if x < m:
            return x, y

def tuning_frequency(b):
    x, y = b
    return x * 4000000 + y

def cannot_be_beacon(y, sensors, beacons):
    ranges = sorted(sensor_ranges(y, sensors))
    x = ranges[0][0]
    count = 0
    for mi, ma in ranges:
        count += ma - x
        x = ma

    beacons_on_line = len([bx for bx, by in beacons if by == y])
    return count + 1 - beacons_on_line

sensors, beacons = parse("input.txt")
print("Part 1:", cannot_be_beacon(2000000, sensors, beacons))

beacon = find_beacon(sensors, 4000000)
print("Part 2:", tuning_frequency(beacon))
