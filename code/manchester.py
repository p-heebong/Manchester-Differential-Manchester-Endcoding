import matplotlib.pyplot as plt


print('1.Manchester')
print('2.Differential-Manchester')

print('')
choice = int(input('무엇을 출력하시겠습니까?: '))

str = input("비트를 입력하세요: ")
num = len(str)

x = list()
y = list()


for i in range(num):
    y.append(int(str[i]))


if choice == 1:

    yaxis = list()
    
    for i in range(0, num):
        if y[i] == 1:
            yaxis.append(-1)
            yaxis.append(1)
        if y[i] == 0:
            yaxis.append(1)
            yaxis.append(-1)
            

    x = []
    
    for i in range(2 * num):
        x.append(i)
        
    x = x * 2
    x.sort()
    x.remove(x[0])
    x.append(2 * num)

    m = []
    
    for i in yaxis:
        m.extend([i, i])
        
    yaxis = m


    zero = list()
    for i in range(0, 4 * num):
        zero.append(int(0))


    plt.plot(x, yaxis, linewidth=4.0)
    plt.plot(x, zero, linewidth=1.0)
    plt.plot([0, 0, 0], [0, 1.5, -1.5])
    plt.grid()
    plt.title("Manchester")
    plt.show()

if choice==2:


    yaxis = list()
    
    for i in range(num - 1):
        if i == 0:
            if y[i] == 1:
                yaxis.append(1)
                yaxis.append(-1)
            elif y[i] == 0:
                yaxis.append(-1)
                yaxis.append(1)
        if y[i + 1] == 0:
            if yaxis[-1] == -1:
                yaxis.append(1)
                yaxis.append(-1)
            elif yaxis[-1] == 1:
                yaxis.append(-1)
                yaxis.append(1)
        if y[i + 1] == 1:
            if yaxis[-1] == -1:
                yaxis.append(-1)
                yaxis.append(1)
            elif yaxis[-1] == 1:
                yaxis.append(1)
                yaxis.append(-1)

    m = []
    
    for i in yaxis:
        m.extend([i, i])
        
    yaxis = m
    
    for i in range(2 * num):
        x.append(i)
        
    x = x * 2
    x.sort()
    x.remove(x[0])
    x.append(2 * num)


    zero = list()
    
    for i in range(0, 4 * num):
        zero.append(int(0))

    plt.plot(x, yaxis, linewidth=5.0)
    plt.plot(x, zero, linewidth=1.0)
    plt.plot([0, 0, 0], [0, 1.5, -1.5])
    plt.grid()
    plt.title("Differential-Manchester")
    plt.show()