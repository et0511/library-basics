# 제목, 축 이름, 눈금, 눈금이름

"""
    1. 축의 이름: set_xlabel(), set_ylabel() 함수
    2. 그래프 이름: set_title() 함수
"""

from matplotlib import pyplot as plt
from numpy.random import randn

fig, sp = plt.subplots()
sp.plot(randn(1000).cumsum())
sp.set_xticks([0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000])
sp.set_xticklabels(['pt0', 'pt1', 'pt2', 'pt3', 'pt4', 'pt5', 'pt6', 'pt7', 'pt8', 'pt9', 'pt10'], fontsize='small', rotation='30')

sp.set_xlabel('Points')
sp.set_ylabel('Points')

sp.set_title('My first Matplotilib Graph')

plt.show()

