from itertools import islice
import heapq
import random
import tempfile


def generate_file(file_name, count, range_number=1000000):
    with open(file_name, "w") as f:
        f.writelines("{}\n".format(random.randint(-range_number, range_number)) for _ in xrange(count))


def merge_sort(file_name, buffer_size=1000000):
    with open(file_name, "r") as file_input:
        temp_file = tempfile.TemporaryFile()
        temp_files = []
        while True:
            elements = list(islice(file_input, buffer_size))
            if not elements:
                break

            elements.sort(key=int)
            temp_files.append(elements)

            temp_file.writelines(elements)
            temp_file.flush()
            temp_file.seek(0)

        with open("sorted_" + file_name, "w") as output_file:
            int_streams = (map(int, f) for f in temp_files)
            int_stream = heapq.merge(*int_streams)
            line_stream = map("{}\n".format, int_stream)
            output_file.writelines(line_stream)
