# Task 1:

all_factors: list[tuple[int, int]] = []
def generate_factors(start: int, end:int):
    for number in range(start, end):
        yield (number, int(end/number))

for item in generate_factors(1, 900900):
    all_factors.append(item)
print(all_factors[:10]) # Limited to display only 10's of the numbers