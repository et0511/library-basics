# figure & subplot

"""
subplot() 함수 사용
"""

from matplotlib import pyplot as plt
from numpy.random import randn
import numpy as np

fig, sp = plt.subplots(2, 2)

# cumsum() = [1, 2, 3, 4, 5] -> [1, 3, 6, 10, 15]
sp[0, 0].plot([2, 4, 5, 6], [81, 93, 91, 97])
sp[0, 1].plot(randn(50).cumsum(), 'k--')
sp[1, 0].hist(randn(100), color='b', alpha=0.3)
sp[1, 1].scatter(np.arange(100), np.arange(100) + 3 * randn(100))

plt.show()

