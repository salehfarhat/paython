# print('Welcom to place the rabbit')
# place =[['🌿','🌿','🌿'],['🌿','🌿','🌿'],['🌿','🌿','🌿']]
# print(f'{place[0]}\n{place[1]}\n{place[2]}\n')
# print('where should the rabbit go? 🐇')
# number = input('Please choose a row and a column')
# row = int(number[0])
# column = int(number[1])
# place[row-1][column-1]= '🐇'
# print('Success.....')
# print(f'{place[0]}\n{place[1]}\n{place[2]}\n')
print('Welcom to place the rabbit')
place =[['🌿','🌿','🌿'],['🌿','🌿','🌿'],['🌿','🌿','🌿']]
print(f'{place[0]}\n{place[1]}\n{place[2]}')
print('Where shoud the rabbit go? 🐇')
number = input('Please choose a row and a column:')
row = int(number[0])
colum = int(number[1])
place[row-1][colum-1]='🐇'
print('Success......')
print(f'{place[0]}\n{place[1]}\n{place[2]}')