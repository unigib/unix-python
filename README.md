# Cross-platform Tkinter demo

The same Python application runs on Windows, Linux, and Windows Subsystem for
Linux (WSL). It displays information about its environment and lets you enter a
name to receive a greeting. It uses only Python's standard library.

## Windows

Install Python 3 from [python.org](https://www.python.org/downloads/windows/),
including the Tcl/Tk component. In PowerShell, open this folder and run:

```powershell
py -m tkinter
py app.py
```

The first command should open a small test window. Close it before starting the
demo. If it fails, modify your Python installation to include Tcl/Tk.

## Linux

Install Python 3 and Tkinter using your distribution's package manager. For
example, on Debian or Ubuntu:

```sh
sudo apt update
sudo apt install python3 python3-tk
python3 -m tkinter
python3 app.py
```

Run these commands from this folder in a graphical desktop session. Close the
Tkinter test window before starting the demo. Other distributions may use a
different package name for Tkinter.

## WSL

Run the Linux commands above inside your WSL distribution, not in Windows
Python. GUI applications need a working display: use
[WSLg](https://learn.microsoft.com/windows/wsl/tutorials/gui-apps) on a
supported Windows/WSL installation, or configure an X server and `DISPLAY`
separately. A terminal-only or headless WSL session cannot show the window.
The application labels WSL as `WSL (Linux)`.

## Tests

With Tkinter installed, run:

```sh
python3 -m unittest discover -s tests
```

On Windows, use `py -m unittest discover -s tests` instead.
