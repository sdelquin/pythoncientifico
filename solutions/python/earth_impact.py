OBJECT_DESIGNATION = 0
IMPACT_PROBABILITY = 3
SPEED = 5
DIAMETER = 6

avg_prob = 0
max_diameter = 0
max_speed = 0
num_objects = 0

with open('data/cneos_sentry_summary_data.csv') as f:
    # skip column of title
    f.readline()
    for line in f.readlines():
        fields = [v.strip('"') for v in line.split(',')]
        name = fields[OBJECT_DESIGNATION]
        prob = float(fields[IMPACT_PROBABILITY])
        speed = float(fields[SPEED])
        diameter = float(fields[DIAMETER])

        avg_prob += prob
        if diameter > max_diameter:
            max_diameter = diameter
        if speed > max_speed:
            max_speed = speed
            fastest_object = name

        num_objects += 1

avg_prob /= num_objects

print(f'Average Impact Probability: {avg_prob}')
print(f'Maximum object diameter (km): {max_diameter}')
print(f'Fastest object: {fastest_object} ({max_speed} km/s)')
