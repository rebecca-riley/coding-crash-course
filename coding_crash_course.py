def main():
    # open files
    try:
        class_file = open('class_schedules.tsv','r')
        TA_file = open('TA_schedules.tsv','r')
    except IOError:
        print('Couldn\'t open input file(s); ending program.')
        return

    # data extraction
    class_data, TA_data = [], []
    file = [class_file,TA_file]
    data = [class_data,TA_data]
    for i in range(len(file)):
        for line in file[i]:
            data[i].append(line)

if __name__ == '__main__':
    main()
