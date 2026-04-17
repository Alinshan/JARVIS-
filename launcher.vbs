Set WshShell = CreateObject("WScript.Shell")
Dim strPath
strPath = CreateObject("Scripting.FileSystemObject").GetParentFolderName(WScript.ScriptFullName)

' Run JARVIS with hidden terminal and --hidden flag
' We use pythonw.exe if available to prevent any flashing console window
WshShell.Run "cmd /c cd /d """ & strPath & """ && pythonw main.py --hidden", 0, False

Set WshShell = Nothing
