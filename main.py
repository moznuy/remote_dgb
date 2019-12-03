import math
import os
import random
import time

# telepresence --swap-deployment k8schat --docker-run -it -v $(pwd):/app laammaar/k8schat-dbg ash

if os.environ.get('REMOTE_DBG'):
    import pydevd_pycharm
    pydevd_pycharm.settrace(
        host='172.17.0.1',
        port=12345,
        stdoutToServer=True,
        stderrToServer=True,
        suspend=False
    )


class Solver:
    def demo(self, a, b, c):
        d = b ** 2 - 4 * a * c
        if d > 0:
            disc = math.sqrt(d)
            root1 = (-b + disc) / (2 * a)
            root2 = (-b - disc) / (2 * a)
            return root1, root2
        elif d == 0:
            return -b / (2 * a)
        else:
            return "This equation has no roots"


if __name__ == '__main__':
    solver = Solver()

    while True:
        time.sleep(1)
        a = random.randint(-100, 100)
        b = random.randint(-100, 100)
        c = random.randint(-100, 100)
        result = solver.demo(a, b, c)
        print(a, b, c, result)
