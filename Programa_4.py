import threading
contador = 0
trava = threading.Lock()
def incrementar():
    global contador
    for i in range(100000):
        with trava:
            contador += 1
threads = []
for i in range(4):
    thread = threading.Thread(target=incrementar)
threads.append(thread)
thread.start()
for thread in threads:
    thread.join()
print("Contador final:", contador)