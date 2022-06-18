^LButton::
    If (A_ThisHotkey = A_PriorHotkey and A_TimeSincePriorHotkey < 200)
        Send, ^c
        Sleep 300
        Run C:\Users\91878\Documents\Python files\Project_Dictionary\main.pyw
        Sleep 1000
        Send, ^v
        Sleep 100
        Send, {Return}
Return