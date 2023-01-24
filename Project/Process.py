import psutil as pt
# from time import sleep

class CpuBar:

    def __init__(self):
        self.cpu_count = pt.cpu_count(logical=False)
        self.cpu_count_logical = pt.cpu_count()
#        print(self.cpu_count)             # shows the number of computer cores
#        print(self.cpu_count_logical)     # shows the number of threads to computer cores

    def cpu_percent_return(self):
        return pt.cpu_percent(percpu=True)

    def cpu_one_return(self):
        return pt.cpu_percent()


    def ram_usage(self):
        return pt.virtual_memory()


x = CpuBar()

#for i in range(10):
#    print(x.cpu_percent_return())
#    sleep(1)