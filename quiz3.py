# 1 პირველი ხერხი
# file = open("clients.txt", "r")
# sec_file = open("inhabitants.txt", "w")
# country = "Spain"
# sec_country = "Germany"
# for each in file:
#     t=each.strip()
#     text_split = t.split(";")
#     if text_split[2] == country:
#         Sp = text_split[0]
#         sec_file.write(Sp+" "+"is resident of Spain""\n")
#     elif text_split[2] == sec_country:
#         Ge=text_split[0]
#         sec_file.write(Ge+" "+"is resident of German""\n")
# sec_file.close()
# file.close()


# 1 მეორე ხერხი
# file = open("clients.txt", "r")
# sec_file = open("inhabitants.txt", "w")
# country = "Spain"
# sec_country = "Germany"
# for each in file:
#     t=each.strip()
#     text_split = t.split(";")
#     if text_split[2] == country or text_split[2] == sec_country:
#         SG=text_split[0]
#         sec_file.write("spain or German inhabit is-"+SG+"\n")
# sec_file.close()
# file.close()


# 2
# file = open("clients.txt", "r")
# emails = []
# for each in file:
#     t = each.strip()
#     text_split = t.split(";")
#     if "2011" in text_split[3]:
#         emails.append(text_split[1])
# print(emails)
# file.close()


# 3
# file = open("clients.txt", "r")
# country = []
# for each in file:
#     t = each.strip()
#     text_split = t.split(";")
#     if text_split[2] in country:
#         continue
#     country.append(text_split[2])
# print(country)
# file.close()



















