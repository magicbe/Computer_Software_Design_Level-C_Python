from tkinter import *

def showWindow(msg_list):
    root = Tk()
    root.title('第一套試題')
    root.geometry('480x380')

    for msg in msg_list:
        Label(root, text=msg, justify=LEFT, anchor=W, relief=GROOVE).pack(fill=BOTH, expand=True, padx=10, pady=10)

    root.mainloop()

def loadFile(fn):
    with open(fn) as file_Obj:
        data = file_Obj.read()
    return data

def ex1(data):
    # 【試題編號】11900-1060301
    # 【題目】迴文判斷
    # 【説明】請利用『指定』迴圈控制指令，由外部資料檔讀入一個欲判斷的數字，若
    # 此數字為迴文(Palindrome，左右讀起均同，例如12321)，則印出此數字及
    # “is a palindrome.”，若不是則印出此數字及“is not a palindrome.
    msg = '第一題結果： '
    if data == data[-1::-1]:
        msg = msg + data + ' is a palindrome.'
    else:
        msg = msg + data + ' is not a palindrome.'
    return msg

def ex2(data):
    # 【試題編號】11900-1060302
    # 【題目】直角三角形列印
    # 【説明】利用『指定』廻圈控制指令，由外部資料檔讀入數字，列印從1開始直到該數字為止之直角三角形。
    msg = '第二題結果：'
    for i in range(1, int(data)+1):
        msg = msg + '\n'
        for j in range(1, i+1):
            msg += str(j)
    return msg

def ex3(data):
    # 【試題編號】11900-1060303
    # 【題目】質數計算
    # 【説明】請利用『指定』迴圈控制指令，由外部資料檔讀入欲檢查的數字，
    # 若此數字是質數則印出此數字及“is a prime number.”，若不是則印出此數字及“is not a prime number.”
    msg = '第三題結果：'
    num = int(data)
    for i in range(2, num):
        if num % i == 0:
            msg = msg + data + ' is not a prime number.'
            break
    else:
        msg = msg + data + ' is a prime number.'
    return msg

def ex4(datas):
    # 【試題編號】11900-1060304
    # 【題目】體質指數BMI
    # 【説明】體質指數BMI(BodyMassIndex)是常用在評估人體肥胖程度的一種指標，
    # 其計算公式為體重除以身高的平方：BMI=體重(公斤)/(身高X身高)(公尺2)
    msg = '第四題結果：'
    datas = datas.split()
    bmiMin = 9999
    for data in datas:
        height, weight = data.split(',')
        height = int(height) / 100
        weight = int(weight)
        bmi = weight / (height * height)
        bmi = int(bmi + 0.5)
        if bmiMin > bmi:
            bmiMin = bmi
    if 20 <= bmiMin <=25:
        msg = msg + '最小BMI值=' + str(bmiMin) + '，正常'
    else:
        msg = msg + '最小BMI值=' + str(bmiMin) + '，不正常'

    return msg

def ex5(datas):
    # 【試題編號】11900-1060305
    # 【題目】矩陣相加
    # 【説明】請利用『指定』迴圏控制指令，由外部資料檔讀入兩組2乘2矩陣數值後，將此兩矩陣數值相加後，列印出此矩陣。
    msg = '第五題結果：\n'
    datas = datas.split()
    a = datas[0].split(',') +  datas[1].split(',')
    b = datas[2].split(',') +  datas[3].split(',')
    ab = [eval(a[i]+'+'+b[i]) for i in range(4)]
    msg = msg + '[{:<3d} {:>3d}]\n'.format(ab[0], ab[1])
    msg = msg + '[{:<3d} {:>3d}]'.format(ab[2], ab[3])
    return msg

if __name__ == '__main__':
    msg_list = []
    # *******************************
    # * 11900-1060301 Program Start *
    # *******************************
    data = loadFile('D:\\test\\1060301.SM')
    msg = ex1(data)
    msg_list.append(msg)
    # *******************************
    # * 11900-1060302 Program Start *
    # *******************************
    data = loadFile('D:\\test\\1060302.SM')
    msg = ex2(data)
    msg_list.append(msg)
    # *******************************
    # * 11900-1060303 Program Start *
    # *******************************
    data = loadFile('D:\\test\\1060303.SM')
    msg = ex3(data)
    msg_list.append(msg)
    # *******************************
    # * 11900-1060304 Program Start *
    # *******************************
    data = loadFile('D:\\test\\1060304.SM')
    msg = ex4(data)
    msg_list.append(msg)
    # *******************************
    # * 11900-1060305 Program Start *
    # *******************************
    data = loadFile('D:\\test\\1060305.SM')
    # print(data)
    msg = ex5(data)
    msg_list.append(msg)
    # 顯示結果視窗
    showWindow(msg_list)

