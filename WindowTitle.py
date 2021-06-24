import ctypes


def get_window_title():
    """
    ctypes.WINFUNCTYPE(戻り値の型, コールバック関数が想定する引数の型)
        : windowsのコールバック関数を定義 定義するだけなので引数は具体的なインスタンスではなく型を指定するのがミソ？
    ↓
    user32.EnumWindows: トップレベルウィンドウのハンドルを順番にコールバック関数へ送る
    ↓
    user32.IsWindowVisible(hwnd): 可視化されたウィンドウであればTrueを返す
    ↓
    user32.GetWindowTextLengthW(hwnd):ウィンドウハンドルのテキスト長を返す
    ↓
    ctypes.create_unicode_buffer(長さ): 変更可能な文字列？を作成 型は文字列配列になる 意味的には w_char*10と同じ，違いが良くわからん
    ↓
    user32.GetWindowTextW(hwnd, 文字列格納用バッファ, 文字列長さ)
    ctypes.POINTER():引数型のポインタを作成
    ctypes.pointer():引数のポインタを返す
    """
    # コールバック関数を定義(定義のみで実行ではない) コールバック関数はctypes.WINFUNCTYPEで作成可能
    EnumWindowsProc = ctypes.WINFUNCTYPE(ctypes.c_bool, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))
    # ??
    EnumWindows = ctypes.windll.user32.EnumWindows
    # タイトル格納用変数
    title = []
    def foreach_window(hwnd, lparam):
        if ctypes.windll.user32.IsWindowVisible(hwnd):
            length = ctypes.windll.user32.GetWindowTextLengthW(hwnd)
            buff = ctypes.create_unicode_buffer(length +1)
            ctypes.windll.user32.GetWindowTextW(hwnd, buff, length + 1)
            title.append(buff.value)
            return True
    EnumWindows(EnumWindowsProc(foreach_window), 0)
    print (title)