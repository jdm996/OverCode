
# Задание 1:
# У вас есть идея создать Back-end для игры: "Угадай число."
# Данный код генерирует рандомное число.

# import random
# random_number = random.randint(0,10)
# print(random_number)
#
#
# attempts = 3
# while attempts != 0:
#         chislo = int(input("Введите число: "))
#         if chislo == random_number:
#                 print("Вы выиграли!")
#                 break
#         attempts -= 1
#         if attempts == 0:
#                 print("Вы проиграли!")
#                 break






# Задание 2:
        # Напишите программу, которая циклично запрашивает у пользователя номера символов по таблице Unicode и выводит соответствующие им символы.
        # Завершает работу при вводе нуля.

# x = 0
# while True:
#         vvod = int(input("Введите номер: "))
#         unicode_sym = chr(vvod)
#         print(unicode_sym)
#         if vvod == 0:
#                 break
#         x += 1


# # # Задание 3:
# #         # Напишите программу, которая измеряет длину введенной строки.
# #         # Если строка длиннее десяти символов, то выносится предупреждение.
# #         # Если короче, то к строке добавляется столько символов *, чтобы ее длина составляла десять символов, после чего новая строка должна выводиться на экран.
# #
# # vvod =input("Введите что-нибудь: ")
# # if len(vvod)>10:
# #     print("Слишком длинная строка")
# # else :
# #    for i in range (len(vvod),10):
# #       vvod+="*"
# #    print(vvod)
# #


# Задание 4:
        # Напишите программу, которая запрашивает у пользователя шесть вещественных чисел.
        # На экран выводит минимальное и максимальное из них, округленные до двух знаков после запятой.
        # Выполните задание без использования встроенных функций min() и max().

# # wto_to = []
# #
# # for i in range(6):
# #         wto_to.append(float(input("Введите вещественные числа: ")))
# #
# # maximum = wto_to[0]
# # minimum = wto_to[0]
# #
# # for i in wto_to:
# #         if i < minimum:
# #             minimum = i
# #         else:
# #             maximum = i
# #
# # print(f"Max: {round(maximum, 2)} | Min: {round(minimum, 2)}")


# #5
# vvod = input("Введите число: ")
# vvod.split()
# print(max(vvod), min(vvod))

# #6
# text = """
# The Zen of Python, by Tim PetersBeautiful is better than ugly.Explicit is better than implicit.
# Simple is better than complex.Complex is better than complicated.
# Flat is better than nested.Sparse is better than dense.
# Readability counts.Special cases aren't special enough to break the rules.Although practicality beats purity.
# Errors should never pass silently.Unless explicitly silenced.
# In the face of ambiguity, refuse the temptation to guess.
# There should be one--and preferably only one --obvious way to do it.
# Although that way may not be obvious at first unless you're Dutch.
# Now is better than never.
# Although never is often better than *right* now.
# If the implementation is hard to explain, it's a bad idea.
# If the implementation is easy to explain, it may be a good idea.
# Namespaces are one honking great idea --let's do more of those!
# """
#
# def findTitles(text):
#     filtered = " ".join([x if x.istitle() else " " for x in text.split()])
#     return [y.strip() for y in filtered.split("  ") if y]
#
# y = findTitles(text)
# print(y)

# #7
#
# def findC(text):
#         for i in text.split():
#                 if i.startswith("c") or i.startswith("C"):
#                         print(i)
#
# findC(text)


