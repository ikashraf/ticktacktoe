def board(X,O):
    fmt = lambda num : "X" if num in X else "O" if num in O else " "
    print(f"""
    {fmt(1)}|{fmt(2)}|{fmt(3)}
    {fmt(4)}|{fmt(5)}|{fmt(6)}
    {fmt(7)}|{fmt(8)}|{fmt(9)}
    """)