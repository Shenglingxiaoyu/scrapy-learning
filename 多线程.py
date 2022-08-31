from threading import Thread
def fun():
    for it in range(1000):
        print('fun',it)


t = Thread(target=fun)
t.start()
for it in range(1000):
    print('name',it)