def to_int(str_arr):
    new_arr = str_arr.split()
    return map(int, new_arr)


def test_solution(func, input_file, output_file, input_fmt=to_int):
    with open(input_file) as input, open(output_file) as output:
        input_lines = [input_fmt(x) for x in input.readlines()[1::2]]
        output_lines = output.readlines()

        all_ok = True
        print("#" * 60)

        for i, out_line in enumerate(output_lines):
            in_line = list(input_lines[i])
            my_output = str(func(in_line))
            matches = my_output == out_line.strip()

            if not matches:
                print("-" * 30)
                print("sucks")
                print("Expected:", out_line)
                print("Actual:", my_output)

            all_ok = all_ok and matches

        if all_ok:
            print("Works!")

        return all_ok
