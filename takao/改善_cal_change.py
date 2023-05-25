def calchange(money):
    ''' おつりの計算をして出力
    Args:
        money(int) : 残金
    Examples:
        >>> calchange(1430)
        おつり1430円
        1000円札：1枚
        100円玉：4枚
        10円玉：3枚
    '''
    print(f"おつり{money}円")
    m_50 = money // 5000 
    if m_50 > 0:
        print(f"5000円札：{m_50}枚")
        money -= m_50 * 5000
    m_10 = money // 1000
    if m_10 > 0:
        print(f"1000円札：{m_10}枚")
        money -= m_10 * 1000
    m_5 = money // 500
    if m_5 > 0:
        print(f"500円玉：{m_5}枚")
        money -= m_5 * 500
    m_1 = money // 100
    if m_1 > 0:
        print(f"100円玉：{m_1}枚")
        money -= m_1 * 100
    m_05 = money // 50
    if m_05 > 0:
        print(f"50円玉：{m_05}枚")
        money -= m_05 * 50
    m_01 = money // 10
    if m_01 > 0:
        print(f"10円玉：{m_01}枚")