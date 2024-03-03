def parse_table(table_string):
    results = []
    for line in table_string.split('\n'):
        inp = [x.strip() for x in line.strip().split(',')]
        if not line.strip() or not inp:
            print('ERROR: empty row')
        else:
            if inp[0] == 'sum':
                try:
                    results.append(sum([float(value_string) for value_string in inp[1:]]))
                except ValueError as err:
                    print(f'ERROR: {err}')
            elif inp[0] == 'avg':
                try:
                    n = [float(value_string) for value_string in inp[1:]]
                    results.append(sum(n)/len(n) if len(n) > 0 else 0)
                except ValueError as err:
                    print(f'ERROR: {err}')
            elif inp[0] == 'count':
                try:
                    results.append(len([float(value_string) for value_string in inp[1:]]))
                except ValueError as err:
                    print(f'ERROR: {err}')
            else:
                print(f'ERROR: Invalid operation "{inp[0]}"')
    return results


def aggregate_table(table_string):
    results = parse_table(table_string)
    return results


def main():
    table_string = """\
    sum,1,2,3
    avg,1,3,7,1
    sum,a,b,c
    mean,5,5,5
    count,2,2
    avg"""
    for result in aggregate_table(table_string):
        print(result)


# Sample output:
#
# ERROR: could not convert string to float: 'a'
# ERROR: Invalid operation "mean"
# 6.0
# 3.0
# 2
# 0


if __name__ == "__main__":
    main()
