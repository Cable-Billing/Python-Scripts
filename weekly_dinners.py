file = open("dinners.txt", 'r')
dinners = list()
for dinner in file.readlines():
    dinners.append(dinner.replace('\n', ''))
file.close()
