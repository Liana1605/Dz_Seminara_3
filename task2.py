#В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
#В случае с английским алфавитом очки распределяются так:
#A, E, I, O, U, L, N, S, T, R – 1 очко;
#D, G – 2 очка;
#B, C, M, P – 3 очка;
#F, H, V, W, Y – 4 очка;
#K – 5 очков;
#J, X – 8 очков;
#Q, Z – 10 очков.
#А русские буквы оцениваются так:
#А, В, Е, И, Н, О, Р, С, Т – 1 очко;
#Д, К, Л, М, П, У – 2 очка;
#Б, Г, Ё, Ь, Я – 3 очка;
#Й, Ы – 4 очка;
#Ж, З, Х, Ц, Ч – 5 очков;
#Ш, Э, Ю – 8 очков;
#Ф, Щ, Ъ – 10 очков
#Напишите программу, которая вычисляет стоимость введенного пользователем слова.
#Будем считать, что на вход подается только одно слово, которое содержит либ 
#только английские, либо только русские буквы. 
#ноутбук = 12

word = str(input('Введите одно слово: ')).upper()
one_point = ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R', 'А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т']
two_point = ['D', 'G', 'Д', 'К', 'Л', 'М', 'П', 'У']
three_point = ['B', 'C', 'M', 'P', 'Б', 'Г', 'Ё', 'Ь', 'Я']
four_point = ['F', 'H', 'V', 'W', 'Y', 'Й', 'Ы']
five_point = ['K', 'Ж', 'З', 'Х', 'Ц', 'Ч']
eight_point = ['J', 'X', 'Ш', 'Э', 'Ю']
ten_point = ['Q', 'Z', 'Ф', 'Щ', 'Ъ']

count = 0

for i in range(len(word)):
    if str(word[i]) in one_point:
        count = count + 1
    if str(word[i]) in two_point:
        count = count + 2
    if str(word[i]) in three_point:
        count = count + 3
    if str(word[i]) in four_point:
        count = count + 4
    if str(word[i]) in five_point:
        count = count + 5
    if str(word[i]) in eight_point:
        count = count + 8
    if str(word[i]) in ten_point:
        count = count + 10
print(count)

