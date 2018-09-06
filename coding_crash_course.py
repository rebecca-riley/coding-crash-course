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
    for line in TA_file:
        TA_data.append(line)


if __name__ == '__main__':
    main()
