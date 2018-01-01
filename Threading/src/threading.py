import threading

class Messenger(threading.Thread):
    def run(self):
        for _ in range(10):
            print(threading.currentThread().getname())

x = Messenger(name = 'vighnesh loves to play')
y = Messenger(name = 'but coding diverts him')

x.start()
y.start()
            