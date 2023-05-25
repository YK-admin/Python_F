def calchange(money):
    ''' おつりの計算をして出力 
    '''
    oturi = money
    print(f"おつり{oturi}円")

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
