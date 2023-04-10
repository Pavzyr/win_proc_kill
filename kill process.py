import psutil  # pip isntall psutil

for proc in psutil.process_iter():
    print(proc.name())
    if proc.name() == 'EXCEL.EXE':  # input your process
        proc.terminate()
