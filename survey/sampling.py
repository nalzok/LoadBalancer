#!/usr/bin/env python3
from random import seed, sample


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
    + Floors in one dormitory building are laid out identically.
    + Each floor has less than one hundred dormitories.
    + Each dormitory holds exactly four students (no empty dorms).
    + Every student lives in a dormitory.
    """
    sample_ = sample(range(dorms_sum), size)

    with open('sample.txt', 'w') as f:
        f.write('\n   === DRAFT ===   \n\n')
        f.write('  ID | Dorm No.\n')
        f.write('---------------\n')
        sample_ = humanize(sample_)
        output = '\n'.join('{:4d} | {}'.format(*k) for k in enumerate(sample_))
        f.write(output)
        # Extra newline for Unix utilities
        f.write('\n')


def humanize(sample_):
    """
    Make indexes of a sample more human readable
    """
    humanized = []
    for idx in sample_:
        for building, dorms_per_floor in enumerate(dorms_per_floor_list):
            dorms_per_building = dorms_per_floor * floors_per_building
            if idx < dorms_per_building:
                break
            idx -= dorms_per_building
        floor, dorm = divmod(idx, dorms_per_floor)
        humanized.append('{:2d}-{}{:02d}'.format(building + 1, floor + 1, dorm + 1))
    humanized.sort()
    return humanized


if __name__ == '__main__':
    seed()
    main(1000)

