from store_credit import find_two_items_with_sum


def test_that_it_finds_indices_that_adds_up_to_sum():
    """ Test that it can find indices of the two items
    whose value adds up to a given value.
    """
    j, k = find_two_items_with_sum([5, 75, 25], 100)
    assert (j, k) == (2, 3)
    j, k = find_two_items_with_sum([150, 24, 79, 50, 88, 345, 3], 200)
    assert (j, k) == (1, 4)
    j, k = find_two_items_with_sum([2, 1, 9, 4, 4, 56, 90, 3], 8)
    assert (j, k) == (4, 5)
