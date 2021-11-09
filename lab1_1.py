start_str = 'asd xxx sasdas ttt asdasd x tyyy xxx'
end_str = ''
for i in start_str:
    if i == 'x':
        end_str += 'y'
    else:
        end_str += i
print(end_str)
