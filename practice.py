str_list=[1,2,3]
str_list.append(5)
print(str_list)

akito=set()
akito.add(0)
akito.add(1)
akito.remove(0)
akito.add(2)
akito.clear()
print(akito)

#関数のおべんつよ
def study():
    print('study');
study()

def study_cal(a, b):
    x=a+b
    return x
answer=study_cal(7,5)
print(answer)

# len関数
print(len("IamAkito"))
# str関数


#1~10までのそれぞれの数を2乗した値をリストに格納し、出力する
lst=[]
for i in range(1,11):
    lst.append(i ** 2)

    print(lst)

#Oだけ出力しないコード
mojiretsu = "Hello World"
for char in mojiretsu:
    if char != "o":
        print(char)

mojiretsu = "Hello World"
for char in mojiretsu:
    if char != "o":
        print(char)