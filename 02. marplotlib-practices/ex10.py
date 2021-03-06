# 색상, 마커, 선 스타일

"""
    plot 매서드는 그래프의 색상과 스타일, 마커 등을 문자열로 표현하여 인자로 넘겨 줄 수 있다.
"""

from matplotlib import pyplot as plt

fig, sp = plt.subplots(1, 1)
sp.plot([1, 2, 3, 4], [10, 20, 30, 40], 'go--')

plt.show()

