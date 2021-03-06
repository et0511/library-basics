# figure & subplot
from matplotlib import pyplot as plt

"""
1. matplotlib에서 그래프는 Figure 객체 내에 존재한다.
2. Figure 객체를 생성하고 add_subplot을 통해 서브플롯을 추가 하게 된다.
3. add_subplot의 파라미터의 의미는 크기 1*1이고 첫번째 플롯을 선택하겠다는 의미이다.
"""

fig = plt.figure()
splt1 = fig.add_subplot(1, 1, 1)
splt1.plot([2, 4, 5, 6], [81, 93, 91, 97])

plt.show()