yosh=int(input('Yoshingizni kiriting '))
if yosh<=4 or yosh>=60:
    narx=0
elif yosh<=18:
    narx=10000
elif yosh>=18:
    narx=20000

print(f'Sizning chipta narxingiz {narx} so\'m. ')