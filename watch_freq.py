import time

CPU_INFO_PATH = "/proc/cpuinfo"
NUM_COL = 5

def read_freq():
    cpu_info = open(CPU_INFO_PATH, "r")

    freq_list = []

    for l in cpu_info.readlines():
        if "cpu MHz" in l:
            freq_raw = l[l.find(": ")+2: l.find("\n")]
            freq_list.append(float(freq_raw))

    cpu_info.close()
    freq_list.sort(reverse=True)
    return freq_list

def print_freq(freq_list):
    count = 0
    for f in freq_list:
        print(str(f) + "MHz" + "\t", end="")
        count += 1
        if count == 5:
            print()
            count = 0


if __name__ == "__main__":
    while True:
        freq_list = read_freq()
        print_freq(freq_list)
        time.sleep(1)
        print("\n")
