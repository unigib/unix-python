"""A small Tkinter application that runs on Windows, Linux, and WSL."""

import os
import platform
import tkinter as tk
from pathlib import Path
from tkinter import ttk


def operating_environment():
    system = platform.system()
    if system == "Linux" and (
        os.environ.get("WSL_DISTRO_NAME") or "microsoft" in platform.release().lower()
    ):
        return "WSL (Linux)"
    return system


class DemoApp(ttk.Frame):
    def __init__(self, master):
        super().__init__(master, padding=20)
        master.title("Cross-platform Tkinter demo")
        self.grid(sticky="nsew")
        master.columnconfigure(0, weight=1)
        master.rowconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        ttk.Label(self, text="Hello from Tkinter!", font=("TkDefaultFont", 16)).grid(
            row=0, column=0, columnspan=2, sticky="w", pady=(0, 15)
        )
        details = (
            ("Environment", operating_environment()),
            ("Operating system", platform.platform()),
            ("Python", platform.python_version()),
            ("Tk window system", master.tk.call("tk", "windowingsystem")),
            ("Home directory", str(Path.home())),
        )
        for row, (label, value) in enumerate(details, start=1):
            ttk.Label(self, text=f"{label}:").grid(row=row, column=0, sticky="nw", padx=(0, 12))
            ttk.Label(self, text=value, wraplength=500).grid(row=row, column=1, sticky="w")

        ttk.Separator(self).grid(row=6, column=0, columnspan=2, sticky="ew", pady=15)
        ttk.Label(self, text="Your name:").grid(row=7, column=0, sticky="w")
        self.name = tk.StringVar()
        entry = ttk.Entry(self, textvariable=self.name)
        entry.grid(row=7, column=1, sticky="ew")
        entry.bind("<Return>", self.greet)
        ttk.Button(self, text="Say hello", command=self.greet).grid(
            row=8, column=1, sticky="w", pady=(10, 0)
        )
        self.message = tk.StringVar(value="Enter a name and click Say hello.")
        ttk.Label(self, textvariable=self.message, wraplength=500).grid(
            row=9, column=0, columnspan=2, sticky="w", pady=(10, 0)
        )
        entry.focus_set()

    def greet(self, event=None):
        name = self.name.get().strip() or "world"
        self.message.set(f"Hello, {name}!")


def main():
    root = tk.Tk()
    DemoApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
