import csv

def sum_of_digits(file_name):
    """returns list"""
    list=[]
    with open(file_name) as csv_file:
        csv_reader = csv.reader(csv_file)

        for row in csv_reader:
            for number_row in row:
                sum=0
                for single_number in number_row:
                    sum+=int(single_number)
            list.append(sum)
            print("Input value:",number_row," Output result ", sum)
    return list


sum_of_digits("data/data.csv")