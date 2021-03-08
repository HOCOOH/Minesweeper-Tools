## 扫雷算法接口

### 一、输入

一个**整数**二维数组表示棋盘的状态，数字格子的整数值为该数字，其他格子的整数值如以下代码所示。

```python
# 格子状态（数字）
EMPTY = 0       # 空白格子
MINE = -1       # 已插旗
UNSOLVED = -2   # 未翻开
```

规定**左上角**的坐标为[0, 0]，一个3*4的棋盘坐标如以下表格所示

| 0，0 | 1，0 | 2，0 | 3，0 |
| :--: | :--: | :--: | :--: |
| 0，1 | 1，1 | 2，1 | 3，1 |
| 0，2 | 1，2 | 2，2 | 3，2 |

### 二、输出

一个列表（队列），成员为Task类的对象

```python
class Task:
    def __init__(self, position: list[int]=[0, 0], operation: bool=False):
        self.pos = position    # 坐标
        self.op = operation     # 要执行的操作
        # op为True代表单击左键，op为False代表单击右键

    def Execute(self):
        
```

注：在方法Execute中完成点击鼠标操作。