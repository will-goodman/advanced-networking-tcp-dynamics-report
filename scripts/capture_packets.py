import requests
import statistics
import time

START_PORT = 4000
END_PORT = 4039
BASE_URL = 'http://tcpdynamics.uk:{port}/{file}'
FILES = ['16K', '64K', '256K', '2M', '16M', '64M']
NUM_ITERATIONS = 5

current_port = START_PORT
while current_port <= END_PORT:
    print(f'Port: {current_port}')
    for file in FILES:
        print(f'File: {file}')
        tmp_acc = []
        for i in range(NUM_ITERATIONS):
            start_time = time.time()
            try:
                response = requests.get(BASE_URL.format(port=current_port, file=file), timeout=60)
            except requests.exceptions.ConnectionError:
                print(f'failed: {current_port}:{file}')
            tmp_acc.append(time.time() - start_time)
            print(f'{current_port}:{file} {i} {time.time() - start_time}')

        print(statistics.median(tmp_acc))

    current_port += 1
