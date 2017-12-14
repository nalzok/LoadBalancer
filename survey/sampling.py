#!/usr/bin/env python3
from array import array
from itertools import repeat
from random import seed, randrange


# Number of dormitories each floor in all dormitory buildings
# TODO: Figure this out
dorms_per_floor_list = [20, 20, 20, 20, 30, 30, 30, 25, 25, 27, 34, 19, 25, 21]
floors_per_building = 6
dorms_sum = sum(dorms_per_floor_list) * floors_per_building


def main(size):
    """Construct a SRS sample of dorms, and write it to a file named "sample.txt"

    Arguments:
    size -- the size of the SRS sample

    Assumptions:
    + Each dormitory building has less than ten floors.
    + Floors in one dormitory building are laid out identically.
    + Each floor has less than one hundred dormitories.
    + Each dormitory holds exactly four students (no empty dorms).
    + Every student lives in a dormitory.
    """
    if size > dorms_sum:
        raise SampleSizeTooLarge('The size of a sample ({}) exceeds that of the population ({}).'.format(size, dorms_sum))

    sample = []
    for _ in repeat(None, size):
        insert_random_element(sample, dorms_sum)

    with open('sample.txt', 'w') as f:
        f.write('!!!DRAFT!!!\n')
        f.write('ID | Dorm number\n')
        sample = humanize(sample)
        output = '\n'.join('{} | {}'.format(*k) for k in enumerate(sample))
        f.write(output)
        f.write('\n')


def insert_random_element(sample, max_element):
    idx_candidate = randrange(max_element)
    for idx in sample:
        if idx == idx_candidate:
            insert_random_element(sample, max_element)
            break
    else:
        sample.append(idx_candidate)


def humanize(sample):
    humanized = []
    for idx in sample:
        for building, dorms_per_floor in enumerate(dorms_per_floor_list):
            for floor in range(floors_per_building):
                idx -= dorms_per_floor
                if idx < 0:
                    humanized.append("{:02d}-{:1d}{:02d}".format(building + 1, floor + 1, idx + dorms_per_floor + 1))
                    break
            else:
                continue
            break
    return humanized


class SampleSizeTooLarge(Exception):
    pass

if __name__ == '__main__':
    seed()
    main(1000)
