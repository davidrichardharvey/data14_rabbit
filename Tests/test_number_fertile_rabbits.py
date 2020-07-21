from data14_rabbit.number_of_babies import RabbitBirths

test = RabbitBirths()

def test_fertile_rabbits():
    assert test.fertile_rabbits({3: 1}, {3: 1}) == [1, 1]
    assert test.fertile_rabbits({1: 4}, {2: 3}) == [0, 0]
    assert test.fertile_rabbits({0: 4, 3: 5}, {2: 8, 5: 3, 6: 7}) == [5, 10]
    assert test.fertile_rabbits({0: 6, 2: 7}, {1: 4, 3: 5, 4: 3}) == [0, 8]

