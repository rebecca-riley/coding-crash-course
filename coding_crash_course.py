def main():
    try:
        class_file = open('class_schedules.tsv','r')
        TA_file = open('TA_schedules.tsv','r')
    except IOError:
        print('Couldn\'t open input file(s); ending program.')
        return


if __name__ == '__main__':
    main()
