#Range Datatypes Examples :
#1.0 1 2 3 4 5 6 7 8 9
range(10)
for v in range(10):#range(value)  type
    print(v)

for v in range(0,10):#range(start,stop) type
    print(v)

for v in range(0,10,1):#range(start,stop,step) type
    print(v)

#2.10 11 12 13 14 15 16 17 18 19 20
    range(10,21)
    for v in range(10,21):
        print(v)
    for v in range(10,21,2):
        print(v)

    for v in range(10,21,3):
        print(v)

#3.1000 1001 1002 1003 1004 1005
range(1000,1006)
for v in range(1000,1006):
    print(v)

for v in range(1000,1006,2):
    print(v)

#4.-1 -2 -3 -4 -5 -6 -7
    for v in range(-1,-8):
        print(v)

    for v in range(-1,-8,-2):
        print(v)

#5.-10 -9 -8 -7 -6 -5 -4 -3 -2 -1
    range(-10,-1)
    for v in range(-10,-1):
        print(v)

    for v in range(-10,-1,2):
        print(v)

#6.10 12 14 16 18 20
        range(10,20)
        for v in range(10,20,1):
            print(v)

        for v in range(10,20,3):
            print(v)

        for v in range(10,20,2):
            print(v)
#7.100 110 120 130 140 150
            range(100,151,10)
            for v in range(100,151,10):
                print(v)

#8.1000 990 980 970 960 950
                for v in range(1000,940,10):
                    print(v)

#9.-1000 -1050 -1100 -1150 -1200
                    for v in range(-1000,-1250,-50):
                        print(v)

#10.-500 -400 -300 -200 -100
                        for v in range(-500,-100,-100):
                            print(v)

                        for v in range(-500,-100,100):
                            print(v)

#11.-5 -4 -3 -2 -1 0 1 2 3 4 5
    range(-5,6)
    for v in range(-5,6):
        print(v)

    for v in range(-5,6,2):
        print(v)

r=range(100,111,2)
print(r[-1])


for val in range (10,0,-1)[::-1]:
    print(val)

for val in range(100,1001,100)[::2]:
    print(val)

print(range(1000,1020,3)[-2])

for val in range(400,501,20)[1:4]:
    print(val)
    
        
    
