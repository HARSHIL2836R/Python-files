^LButton::         ;add '+' after '^' for 'Ctrl-Shift'

Send, ^c
Sleep 300
Run C:\Users\91878\Documents\Python files\Project_Dictionary\Dictionary.pyw

sleep 1000

if WinExist("ahk_class TkTopLevel") or WinExist(Dictionary)
{
    WinActivate ; Use the window found by WinExist.
}
Send ^v
Sleep 100
Send {return}

return