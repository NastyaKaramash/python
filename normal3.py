humans = ['Настя', 'Вова', 'Маша']
salaries = [100, 200, 300]
dic = dict(zip(humans, salaries))
print(dic)
with open ('salary.txt', 'a+', encoding='utf-8') as out:
    for key,val in dic.items():
        out.write('{}:{}\n'.format(key,val))
with open ('salary.txt') as out:
    for line in out:
        print(line)
#остальное не знаю как(