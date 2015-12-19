import argparse

from algo_sorted import merge_sort, quick_sort
from word_count import word_count, top_ten_words


def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--method', type=int,
                        help='1 - word count, 2 - top 10, 3 - quicksort, 4 - mergesort, 5 - fibonacci',
                        choices=[1, 2, 3, 4, 5])
    parser.add_argument('-f', '--file', metavar='in-file', type=argparse.FileType('r'))
    parser.add_argument('-t', '--text', type=str)
    return parser


def fibonacci_generator(n):
    a, b = 0, 1
    for i in xrange(n):
        yield a
        a, b = b, a + b


def main():
    args = get_parser().parse_args()

    input_data = ''
    if args.file:
        with open(args.file.name) as f:
            input_data = f.read()
    elif args.text:
        input_data = args.text

    if args.method == 1:
        print(word_count(input_data))
    elif args.method == 2:
        print(top_ten_words(input_data))
    elif args.method == 3:
        print(quick_sort(input_data.split()))
    elif args.method == 4:
        print(merge_sort(input_data.split()))
    elif args.method == 5:
        number = int(raw_input())
        generator = fibonacci_generator(number)
        for i in generator:
            print(i)

main()
