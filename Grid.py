class Grid:
    # 格子状态（数字）
    EMPTY = 0       # 空白格子
    MINE = -1       # 已插旗
    UNKNOWN = -2   # 未翻开

    def __init__(self, position: list=[0, 0], status = UNKNOWN):
        self.pos = position    # 坐标
        self.status = status    # 状态（数字），空格子为0，未翻开为-2，已插旗为-1
        # 以下三个属性由Board类的Scan方法计算
        self.isDead = False     # 是否为死格子（已解决的数字格和地雷格）
        self.numMine = 0        # 周围已插旗的地雷数
        self.numUnknown = 0    # 周围未翻开的格子数
    

