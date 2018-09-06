def main():
    try:
        class_file = open('class_schedules.tsv','r')
        TA_file = open('TA_schedules.tsv','r')
    except IOError:
        print('Couldn\'t open input file(s); ending program.')
        return

    class_data = []
    TA_data = []
    for line in class_file:
        class_data.append(line)
        print(line)
    for line in TA_file:
        TA_data.append(line)
        print(line)

    # print first, second, and last lines in data lists to make sure
    # they look okay
    print(class_data[0])
    print(class_data[1])
    print(class_data[len(class_data) - 1])
    print(TA_data[0])
    print(TA_data[1])
    print(TA_data[len(TA_data) - 1])


if __name__ == '__main__':
    main()
