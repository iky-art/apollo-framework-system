import os


def get_cpu():
    cores = 0

    with open("/proc/cpuinfo") as f:
        for line in f:
            if line.startswith("processor"):
                cores += 1

    return f"{cores} Core ARM64"


def get_ram():
    total = 0
    available = 0

    with open("/proc/meminfo") as f:
        for line in f:
            if "MemTotal" in line:
                total = int(line.split()[1]) // 1024

            if "MemAvailable" in line:
                available = int(line.split()[1]) // 1024

    used = total - available

    return f"{used}MB / {total}MB"


def get_storage():
    result = os.popen("df -h / | tail -1").read()
    data = result.split()

    return f"{data[2]} / {data[1]}"


def info():
    print("🚀 Apollo System Monitor")
    print("=======================")
    print("CPU     :", get_cpu())
    print("RAM     :", get_ram())
    print("Storage :", get_storage())


if __name__ == "__main__":
    info()
