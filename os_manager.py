import tkinter as tk
from tkinter import messagebox

# Define a dictionary for descriptions
descriptions = {
    "Welcome": """
    Welcome to and thank you for using VMproHV.

    To get started, click "Create VM" to the left.

    What is this?
    This is a Debian 12-based Operating System that creates virtual computers.
    Instead of dual-booting, you can switch between Linux and Windows here seamlessly.

    For those familiar with Proxmox, this concept is similar, but VMproHV allows management
    directly from this manager, no need for an additional device.
    """,
    "Windows": "Select Windows 10 or 11 for installation.",
    "Win 10": "Select from the available Windows 10 editions to download and install.",
    "Win 11": "Select from the available Windows 11 editions to download and install.",
    "Linux": "Select from Arch, Fedora, or Debian-based distros.",
    "Arch": "Select the main Arch or one of its 5 most popular distros.",
    "Fedora": "Select the main Fedora or one of its 5 most popular distros.",
    "Debian": "Select Debian 12 or one of its 5 most popular Debian-based distros.",
}

# Global variables
current_section = "home"

def update_right_frame(content_key):
    # Update the right section with the provided description
    description = descriptions.get(content_key, "Select an option.")
    right_message_label.config(text=description)

def show_main_menu():
    # Clear left frame and show main menu buttons
    clear_left_frame()
    create_main_menu()

def clear_left_frame():
    # Remove all widgets in the left frame
    for widget in left_frame.winfo_children():
        widget.destroy()

def create_main_menu():
    tk.Button(left_frame, text="Create VM", command=create_vm_menu, bg=button_bg, fg=text_color).pack(pady=10, padx=10, fill="x")
    tk.Button(left_frame, text="Select ISO Download Location", bg=button_bg, fg=text_color).pack(pady=10, padx=10, fill="x")
    tk.Button(left_frame, text="Options", bg=button_bg, fg=text_color).pack(pady=10, padx=10, fill="x")
    update_right_frame("Welcome")

def create_vm_menu():
    clear_left_frame()
    tk.Button(left_frame, text="Windows", command=show_windows_menu, bg=button_bg, fg=text_color).pack(pady=10, padx=10, fill="x")
    tk.Button(left_frame, text="Linux", command=show_linux_menu, bg=button_bg, fg=text_color).pack(pady=10, padx=10, fill="x")
    tk.Button(left_frame, text="Home", command=show_main_menu, bg=button_bg, fg=text_color).pack(pady=10, padx=10, fill="x")
    tk.Button(left_frame, text="Options", bg=button_bg, fg=text_color).pack(pady=10, padx=10, fill="x")
    update_right_frame("Windows")

def show_windows_menu():
    clear_left_frame()
    tk.Button(left_frame, text="Win 10", command=show_win10_menu, bg=button_bg, fg=text_color).pack(pady=10, padx=10, fill="x")
    tk.Button(left_frame, text="Win 11", command=show_win11_menu, bg=button_bg, fg=text_color).pack(pady=10, padx=10, fill="x")
    tk.Button(left_frame, text="Back", command=create_vm_menu, bg=button_bg, fg=text_color).pack(pady=10, padx=10, fill="x")
    tk.Button(left_frame, text="Home", command=show_main_menu, bg=button_bg, fg=text_color).pack(pady=10, padx=10, fill="x")
    tk.Button(left_frame, text="Options", bg=button_bg, fg=text_color).pack(pady=10, padx=10, fill="x")
    update_right_frame("Win 10")

def show_win10_menu():
    clear_left_frame()
    tk.Button(left_frame, text="Win 10 Home", bg=button_bg, fg=text_color).pack(pady=10, padx=10, fill="x")
    tk.Button(left_frame, text="Win 10 Pro", bg=button_bg, fg=text_color).pack(pady=10, padx=10, fill="x")
    tk.Button(left_frame, text="Win 10 S", bg=button_bg, fg=text_color).pack(pady=10, padx=10, fill="x")
    tk.Button(left_frame, text="Win 10 Enterprise", bg=button_bg, fg=text_color).pack(pady=10, padx=10, fill="x")
    tk.Button(left_frame, text="Win 10 Education", bg=button_bg, fg=text_color).pack(pady=10, padx=10, fill="x")
    tk.Button(left_frame, text="Back", command=show_windows_menu, bg=button_bg, fg=text_color).pack(pady=10, padx=10, fill="x")
    tk.Button(left_frame, text="Home", command=show_main_menu, bg=button_bg, fg=text_color).pack(pady=10, padx=10, fill="x")
    update_right_frame("Win 10")

def show_win11_menu():
    clear_left_frame()
    tk.Button(left_frame, text="Win 11 Home", bg=button_bg, fg=text_color).pack(pady=10, padx=10, fill="x")
    tk.Button(left_frame, text="Win 11 Pro", bg=button_bg, fg=text_color).pack(pady=10, padx=10, fill="x")
    tk.Button(left_frame, text="Win 11 S", bg=button_bg, fg=text_color).pack(pady=10, padx=10, fill="x")
    tk.Button(left_frame, text="Win 11 Enterprise", bg=button_bg, fg=text_color).pack(pady=10, padx=10, fill="x")
    tk.Button(left_frame, text="Win 11 Education", bg=button_bg, fg=text_color).pack(pady=10, padx=10, fill="x")
    tk.Button(left_frame, text="Back", command=show_windows_menu, bg=button_bg, fg=text_color).pack(pady=10, padx=10, fill="x")
    tk.Button(left_frame, text="Home", command=show_main_menu, bg=button_bg, fg=text_color).pack(pady=10, padx=10, fill="x")
    update_right_frame("Win 11")

def show_linux_menu():
    clear_left_frame()
    tk.Button(left_frame, text="Arch", command=show_arch_menu, bg=button_bg, fg=text_color).pack(pady=10, padx=10, fill="x")
    tk.Button(left_frame, text="Fedora", command=show_fedora_menu, bg=button_bg, fg=text_color).pack(pady=10, padx=10, fill="x")
    tk.Button(left_frame, text="Debian", command=show_debian_menu, bg=button_bg, fg=text_color).pack(pady=10, padx=10, fill="x")
    tk.Button(left_frame, text="Back", command=create_vm_menu, bg=button_bg, fg=text_color).pack(pady=10, padx=10, fill="x")
    tk.Button(left_frame, text="Home", command=show_main_menu, bg=button_bg, fg=text_color).pack(pady=10, padx=10, fill="x")
    update_right_frame("Linux")

def show_arch_menu():
    clear_left_frame()
    tk.Button(left_frame, text="Main Arch", bg=button_bg, fg=text_color).pack(pady=10, padx=10, fill="x")
    tk.Button(left_frame, text="Manjaro", bg=button_bg, fg=text_color).pack(pady=10, padx=10, fill="x")
    tk.Button(left_frame, text="EndeavourOS", bg=button_bg, fg=text_color).pack(pady=10, padx=10, fill="x")
    tk.Button(left_frame, text="Garuda Linux", bg=button_bg, fg=text_color).pack(pady=10, padx=10, fill="x")
    tk.Button(left_frame, text="ArcoLinux", bg=button_bg, fg=text_color).pack(pady=10, padx=10, fill="x")
    tk.Button(left_frame, text="RebornOS", bg=button_bg, fg=text_color).pack(pady=10, padx=10, fill="x")
    tk.Button(left_frame, text="Back", command=show_linux_menu, bg=button_bg, fg=text_color).pack(pady=10, padx=10, fill="x")
    tk.Button(left_frame, text="Home", command=show_main_menu, bg=button_bg, fg=text_color).pack(pady=10, padx=10, fill="x")
    update_right_frame("Arch")

def show_fedora_menu():
    clear_left_frame()
    tk.Button(left_frame, text="Main Fedora", bg=button_bg, fg=text_color).pack(pady=10, padx=10, fill="x")
    tk.Button(left_frame, text="Fedora Workstation", bg=button_bg, fg=text_color).pack(pady=10, padx=10, fill="x")
    tk.Button(left_frame, text="Nobara Project", bg=button_bg, fg=text_color).pack(pady=10, padx=10, fill="x")
    tk.Button(left_frame, text="RHEL (Red Hat Enterprise Linux)", bg=button_bg, fg=text_color).pack(pady=10, padx=10, fill="x")
    tk.Button(left_frame, text="Rocky Linux", bg=button_bg, fg=text_color).pack(pady=10, padx=10, fill="x")
    tk.Button(left_frame, text="AlmaLinux", bg=button_bg, fg=text_color).pack(pady=10, padx=10, fill="x")
    tk.Button(left_frame, text="Back", command=show_linux_menu, bg=button_bg, fg=text_color).pack(pady=10, padx=10, fill="x")
    tk.Button(left_frame, text="Home", command=show_main_menu, bg=button_bg, fg=text_color).pack(pady=10, padx=10, fill="x")
    update_right_frame("Fedora")

def show_debian_menu():
    clear_left_frame()
    tk.Button(left_frame, text="Debian 12", bg=button_bg, fg=text_color).pack(pady=10, padx=10, fill="x")
    tk.Button(left_frame, text="Ubuntu", bg=button_bg, fg=text_color).pack(pady=10, padx=10, fill="x")
    tk.Button(left_frame, text="Linux Mint", bg=button_bg, fg=text_color).pack(pady=10, padx=10, fill="x")
    tk.Button(left_frame, text="Pop!_OS", bg=button_bg, fg=text_color).pack(pady=10, padx=10, fill="x")
    tk.Button(left_frame, text="MX Linux", bg=button_bg, fg=text_color).pack(pady=10, padx=10, fill="x")
    tk.Button(left_frame, text="Back", command=show_linux_menu, bg=button_bg, fg=text_color).pack(pady=10, padx=10, fill="x")
    tk.Button(left_frame, text="Home", command=show_main_menu, bg=button_bg, fg=text_color).pack(pady=10, padx=10, fill="x")
    update_right_frame("Debian")
    
    # Set up the main window
root = tk.Tk()
root.title("VMproHV")
root.geometry("800x600")

# Define colors and styles
text_color = "#CFCFCF"
left_bg = "#2D2D2D"
right_bg = "#252525"
button_bg = "#252525"

# Left Section (Control Panel)
left_frame = tk.Frame(root, bg=left_bg, width=300)
left_frame.pack(side="left", fill="y")

# Right Section (Info/Progress Display)
right_frame = tk.Frame(root, bg=right_bg)
right_frame.pack(side="right", fill="both", expand=True)

# Welcome message
right_message_label = tk.Label(right_frame, text=descriptions["Welcome"], fg=text_color, bg=right_bg, justify="left", padx=20, pady=20)
right_message_label.pack()

# Vertical separator
separator = tk.Frame(root, bg=text_color, width=2)
separator.pack(side="left", fill="y")

# Initial Main Menu
create_main_menu()

# Start the GUI
root.mainloop()