# 1-2
# file = open("titanic.txt", "r")
# female_quantity = 0
# male_quantity = 0
# female_dead = 0
# male_dead = 0
# female_survived = 0
# male_survived = 0
# for each in file:
#     file_strip = each.strip()
#     file_split = file_strip.split(",")
#     if file_split[4] == "female":
#         female_quantity += 1
#         if file_split[1] == "0":
#             female_dead += 1
#         else:
#             female_survived += 1
#
#     if file_split[4] == "male":
#         male_quantity += 1
#         if file_split[1] == "0":
#             male_dead += 1
#         else:
#             male_survived += 1
#
# all_quantity = female_quantity + male_quantity
# female_percent = female_quantity * 100 / all_quantity
# print("ქალების რაოდენობა ბორტზე", female_percent, "%", "ანუ", female_quantity)
# male_percent = male_quantity * 100 / all_quantity
# print("კაცების რაოდენობა ბორტზე", male_percent, "%", "ანუ", male_quantity)
# # 3-4
# male_survived_percent = male_survived * 100 / male_quantity
# female_survived_percent = female_survived * 100 / female_quantity
# print("გადარჩა ქალების", female_survived_percent, "%", "ანუ", female_survived)
# print("გადარჩა კაცების", male_survived_percent, "%", "ანუ", male_survived)
# print("მოკვდა ქალების", 100 - female_survived_percent, "%", "ანუ", female_dead)
# print('მოკვდა კაცების', 100 - male_survived_percent, "%", "ანუ", male_dead)
# file.close()


# 5-6
# file = open("titanic.txt", "r")
# first_class = 0
# first_class_fare = 0
# second_class = 0
# second_class_fare = 0
# third_class = 0
# third_class_fare = 0
# for each in file:
#     file_strip = each.strip()
#     file_split = file_strip.split(",")
#     if file_split[2] == "1":
#         first_class += 1
#         Fare1 = float(file_split[9])
#         first_class_fare += Fare1
#
#     if file_split[2] == "2":
#         second_class += 1
#         Fare2 = float(file_split[9])
#         second_class_fare += Fare2
#
#     if file_split[2] == "3":
#         third_class += 1
#         Fare3 = float(file_split[9])
#         third_class_fare += Fare3
#
# all_quantity = first_class + second_class + third_class
# first_class_percent = first_class * 100 / all_quantity
# print("პირველი კალასის მგზავრების რაოდენობა", first_class_percent, "%", "ანუ", first_class)
# second_class_percent = second_class * 100 / all_quantity
# print("მეორე კალასის მგზავრების რაოდენობა", second_class_percent, "%", "ანუ", second_class)
# third_class_percent = third_class * 100 / all_quantity
# print("მესამე კალასის მგზავრების რაოდენობა", third_class_percent, "%", "ანუ", third_class )
# # 6
# first_class_average = first_class_fare / first_class
# print("პირველი კლასის ბილეთის საშუალო ფასია", first_class_average)
# second_class_average = second_class_fare / second_class
# print("მეორე კლასის ბილეთის საშუალო ფასია", second_class_average)
# third_class_average = third_class_fare / third_class
# print("მესამე კლასის ბილეთის საშუალო ფასია", third_class_average)
# file.close()


# # 7
# my_dict = {
#     "passengers amount":
#         {
#             "female": 314,
#             "male": 577
#         },
#     "passengers death or survive amount":
#         {
#             "female death": 81,
#             "mael death": 468,
#             "female survive": 233,
#             "male survive": 109
#         },
#     "passengers death or survive percent:":
#         {
#             "female death percent": 25.796178343949038,
#             "mael death percent": 81.10918544194108,
#             "female survive percent": 74.20382165605096,
#             "male survive percent": 18.890814558058924
#         },
#     "different class tickets amount":
#         {
#             "first class": 216,
#             "second class": 184,
#             "third class": 491
#         },
#     "different class ticket percent":
#         {
#             "first class percent": 24.242424242424242,
#             "second class percent": 20.650953984287316,
#             "third class percent": 55.10662177328844
#         },
#     "average class fare":
#         {
#             "first class average fare": 84.15468749999992,
#             "second class average fare": 20.66218315217391,
#             "third class average fare": 13.675550101832997
#         },
#     "port":
#         {
#             "Queenstown": 77,
#             "Cherbourg": 168,
#             "Southampton": 644
#         }
# }
# print(my_dict)

# # 8
# # აქ გამოთვლილია თუ რომელი ადგილიდან(პორტიდან) ამოვიდნენ მგზავრები
# file = open("titanic.txt", "r")
# Queenstown = 0
# Cherbourg = 0
# Southampton = 0
# for each in file:
#     file_strip = each.strip()
#     file_split = file_strip.split(",")
#     if file_split[11] == "Q":
#         Queenstown += 1
#     if file_split[11] == "C":
#         Cherbourg += 1
#     if file_split[11] == "S":
#         Southampton += 1
#     if file_split[11] == "":
#         print("არცერთ ამ ჩასხდომის ადგილს არ ასულა ბორტზე", file_split[3])
# print("Queenstown-ში ამოვიდა", Queenstown, "მგზავრი")
# print("Cherbourg-ში ამოვიდა", Cherbourg, "მგზავრი")
# print("Southampton-ში ამოვიდა", Southampton, "მგზავრი")
# file.close()