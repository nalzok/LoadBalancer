#!/usr/bin/env python3
from random import seed, sample


# Configuration Variables
BUILDING_COUNT = 20
FLOORS_PER_BUILDING = 6
DORMS_PER_FLOOR = 31


def main(size):
    """Construct a SRSWOR sample of dormitories, and write it to a file named "sample.txt"

    :param size: the size of the SRS sample
    """
    dorms_count = DORMS_PER_FLOOR * FLOORS_PER_BUILDING * BUILDING_COUNT
    sample_ = sample(range(dorms_count), size)

    with open('sample.txt', 'w') as f:
        f.write('\n  === DRAFT ===  \n\n')
        f.write('  ID | Dorm No.\n')
        f.write('-----------------\n')
        sample_ = humanize(sample_)
        output = '\n'.join('{:4d} | {}'.format(*k) for k in enumerate(sample_))
        f.write(output)
        # UNIX/Linux terminal compatibility.
        f.write('\n')


def humanize(sample_):
    """Make indexes of a sample human-readable, and sort them in ascending order

    :param sample_: a list of indexes forming an sample
    :return: humanized and sorted indexes
    """
    humanized = []
    # e.g. [1753, 1754] -> [12-411, 12-412]
    for idx in sample_:
        dorms_per_building = DORMS_PER_FLOOR * FLOORS_PER_BUILDING
        building, idx_in_building = divmod(idx, dorms_per_building)
        floor, dorm = divmod(idx_in_building, DORMS_PER_FLOOR)
        humanized.append('{:2d}-{}{:02d}'.format(map_bld(building), floor + 1, dorm + 1))
    humanized.sort()
    return humanized


def map_bld(building):
    """Maps the index of a dorm building to its number

    :param building: the index of a dorm building
    :return: the number of a dorm building
    """
    # Strangely, there is no dorm building No. 17 & 18
    # So 15 -> 16, 16 -> 19, 17 -> 20, ...
    return building + 1 if building < 16 else building + 3


if __name__ == '__main__':
    seed()
    main(200)
