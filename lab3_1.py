me_list = [['Roman', 'Burnyshev', 35, 'Perm', 1986],['Alex', 'Kakoitovich', 40, 'Moscow', 1981],['Dmitriy', 'Tretiy', 55, 'SPeterburg', 1966]]

#цикл на самого старого
oldest = me_list[0][0] + me_list[0][1]
max_age = me_list[0][2]
for i in range(1, len(me_list)):
    if me_list[i][2] > max_age:
        max_age = me_list[i][2]
        oldest = me_list[i][0] + ' ' + me_list[i][1]
print(oldest)