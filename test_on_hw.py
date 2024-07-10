from datetime import datetime


def logger(old_function):
    def new_function(*args, **kwargs):
        curr_date_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S.%f")
        result = old_function(*args, **kwargs)
        log_string = (f'{curr_date_time} | '
                      f'Function name: {old_function.__name__} | '
                      f'Function args: {args} | '
                      f'Function kwargs: {kwargs} | '
                      f'Function result: {result}\n')
        with open('test_on_hw.log', 'a') as f:
            f.write(log_string)
        return result
    return new_function


class FlatIterator:

    @logger
    def __init__(self, list_of_list):
        self.list_of_list = iter(list_of_list)

    @logger
    def __iter__(self):
        self.curr_list = next(self.list_of_list)
        self.cursor = 0
        return self

    @logger
    def __next__(self):
        if self.cursor >= len(self.curr_list):
            self.curr_list = next(self.list_of_list)
            self.cursor = 0
        item = self.curr_list[self.cursor]
        if self.curr_list == []:
            raise StopIteration
        self.cursor += 1
        return item


@logger
def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()
