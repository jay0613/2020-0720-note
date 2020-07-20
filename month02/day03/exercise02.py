# f = open("dict.txt","r")
# input_word = input("请输入单词:")
# while True:
#     word = f.readline()
#     if word.split(" ")[0] == input_word:
#         print(word)
#         break
#     elif word =="":
#         print("木有找到")
#         break
#
f = open("dict.txt", "r")
while True:
    input_word = input("请输入单词:")
    # while True:
    for line in f:
        if line.split(" ")[0] == input_word:
            print(line.split(" ",2)[-1].strip())
            break
        elif line.split(" ")[0] > input_word:
            print("没有找到")
            break
    else:
        print("没有找到")





