import subprocess
from datetime import datetime


def ps_aux():
    result = subprocess.run(['ps', 'aux'], capture_output=True, text=True)
    lines = result.stdout.splitlines()

    header = lines.pop(0)
    users = {}
    total_processes = len(lines) - 1
    total_cpu = 0.0
    total_mem = 0.0
    max_cpu_process = ('', 0.0)
    max_memory_process = ('', 0.0)

    for line in lines:
        columns = line.split()

        user = columns[0]
        cpu = float(columns[2])
        mem = float(columns[3])
        process_name = ' '.join(columns[10:])

        if user in users:
            users[user] += 1
        else:
            users[user] = 1

        total_cpu += cpu
        total_mem += mem

        if cpu > max_cpu_process[1]:
            max_cpu_process = (process_name, cpu)

        if mem > max_memory_process[1]:
            max_memory_process = (process_name, mem)

    # Название процессов
    max_cpu_process_name = (max_cpu_process[0][:20] + '...') \
        if len(max_cpu_process[0]) > 20 \
        else max_cpu_process[0]
    max_memory_process_name = (max_memory_process[0][:20] + '...') \
        if len(max_memory_process[0]) > 20 \
        else max_memory_process[0]

    # Формирование отчета
    report = f"""Отчёт о состоянии системы:
    Пользователи системы: '{', '.join(users.keys())}'
    Процессов запущено: {total_processes}
    Пользовательских процессов:
    """
    for user, count in users.items():
        report += f"{user}: {count - 1}\n"

    report += f"""
    Всего памяти используется: {total_mem:.1f}%
    Всего CPU используется: {total_cpu:.1f}%
    Больше всего памяти использует: ({max_memory_process[1]}%) {max_memory_process_name}
    Больше всего CPU использует: ({max_cpu_process[1]}%) {max_cpu_process_name}
    """

    print(report)

    current_datetime_str = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    with open(f"{current_datetime_str}-scan.txt", "w") as file:
        file.write(report)


ps_aux()
