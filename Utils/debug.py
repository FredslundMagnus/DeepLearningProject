from pstats import func_get_function_name, func_std_string, f8, Stats
import os
import time
import sys


def print_title(self):
    print('           ncalls  tottime  percall  cumtime  percall', end=' ', file=self.stream)
    print('filename:lineno(function)', file=self.stream)


def print_line(self, func):  # hack: should print percentages
    cc, nc, tt, ct, callers = self.stats[func]
    c = str(nc)
    if nc != cc:
        c = c + '/' + str(cc)
    print('       ', c.rjust(9), end=' ', file=self.stream)
    print(f8(tt), end=' ', file=self.stream)
    if nc == 0:
        print(' ' * 8, end=' ', file=self.stream)
    else:
        print(f8(tt / nc), end=' ', file=self.stream)
    print(f8(ct), end=' ', file=self.stream)
    if cc == 0:
        print(' ' * 8, end=' ', file=self.stream)
    else:
        print(f8(ct / cc), end=' ', file=self.stream)
    print(func_std_string(func), file=self.stream)


def print_stats(self, *amount):
    # for filename in self.files:
    #     print(filename, file=self.stream)
    if self.files:
        print(file=self.stream)
    indent = ' ' * 5
    for func in self.top_level:
        print(indent, func_get_function_name(func), file=self.stream)

    print(indent, self.total_calls, "function calls", end=' ', file=self.stream)
    if self.total_calls != self.prim_calls:
        print("(%d primitive calls)" % self.prim_calls, end=' ', file=self.stream)
    print("in %.2f seconds" % self.total_tt, file=self.stream)
    print(end='\n## ', file=self.stream)
    width, list = self.get_print_list(amount)
    if list:
        print_title(self)
        for func in list:
            print_line(self, func)
        print(file=self.stream)
        print(file=self.stream)
    return self


def profilingStats():
    print(f"# Profiling\n")
    p = Stats('stats')
    p.print_stats = print_stats
    p.strip_dirs().sort_stats('cumulative').print_stats(p, 100)
    os.remove('stats')
    print(f"# Other prints\n")


class Timer:
    def __init__(self, f) -> None:
        self.start = time.time()
        f()
        self.time = time.time() - self.start
        self.minutes = int(self.time // 60)
        self.hours = int(self.time // 3600)


def enablePrint():
    sys.stdout = sys.__stdout__


def disablePrint():
    sys.stdout = open(os.devnull, 'w')


def getvals(defaults):
    args = sys.argv[1].split(' ')
    print(args)
    defaults['name'] = args[0]
    for i, s_ in enumerate(args):
        s = s_[1:]
        print(s)
        if s in defaults:
            try:
                defaults[s] = float(args[i + 1])
            except:
                defaults[s] = args[i + 1]
    return tuple(defaults.values())


def checkServer():
    return bool(sys.argv[1:])
