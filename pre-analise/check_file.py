import glob

files = glob.glob('*.csv')

ok_list =[]

for file in files:

    print(file[-8:-4])

    ok_list.append(file[-8:-4])

lines_new_group = []
with open('group.epg', 'r') as old_group:

    lines = old_group.readlines()

    add_line = True

    for line in lines:

        for number in ok_list:

            if number in line[56:60]:

                print(number)

                add_line = False

                #break

        if add_line == True:

            lines_new_group.append(line)
            print(line)

        add_line = True

with open('new_group.epg', 'w') as new_group:

    for line in lines_new_group:

        new_group.write(line)