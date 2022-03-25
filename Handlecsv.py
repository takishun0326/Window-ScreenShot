import csv

def get_csv(index):
    with open('Data/state.csv') as f:
        reader = csv.reader(f)
        l = [row for row in reader]
        return l[index]

def write_csv(index, value):
    with open('Data/state.csv') as f:
        reader = csv.reader(f)
        l = [row for row in reader]
        l[index] = value




def get_is_start():
    return 1 == get_csv(0)

def get_number_of_screenshots():
    return int(get_csv(1))


def write_is_start(bool):
    # スクリーンショットが始まってるなら
    if bool:
        write_csv(0,1)
    else :
        write_csv(0,0)


def write_number_of_screenshots(num):
    write_csv(1,num)