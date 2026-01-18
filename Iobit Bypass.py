import tkinter as tk
from tkinter import messagebox
import os
import shutil
import ctypes
import webbrowser

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin() != 0
    except:
        return False

# Dark Mode Renkleri
DARK_BG = "#121212"
DARK_FG = "#e0e0e0"
ACCENT = "#ff5722"
BUTTON_BG = "#1f1f1f"
FONT = ("Segoe UI", 11)
TITLE_FONT = ("Segoe UI", 16, "bold")

class IObitUnlockerManager:
    def __init__(self, root):
        self.root = root
        self.root.title("IObit Unlocker Restriction Manager By Arasswys")
        self.root.geometry("520x420")
        self.root.configure(bg=DARK_BG)
        self.root.resizable(False, False)
        
        # Yolları gizli tutmak için sadece iç kullanımda tutuyoruz
        self.ini_path = r"C:\Program Files (x86)\IObit\IObit Unlocker\SpecialDir.ini"
        self.backup_path = r"C:\Backup\SpecialDir.ini"
        
        self.setup_ui()
    
    def setup_ui(self):
        tk.Label(
            self.root, text="IObit Unlocker Restriction Manager By Arasswys",
            font=TITLE_FONT, bg=DARK_BG, fg=ACCENT
        ).pack(pady=20)
        
        admin_status = "Administrator" if is_admin() else "Normal User (Run as Administrator)"
        tk.Label(
            self.root, text=f"Current Mode: {admin_status}",
            bg=DARK_BG, fg="#4caf50" if is_admin() else "#f44336",
            font=FONT
        ).pack(pady=5)
        
        self.status = tk.Label(
            self.root, text="Ready",
            bg=DARK_BG, fg="#888888", font=FONT, wraplength=480
        )
        self.status.pack(pady=10)
        
        tk.Button(
            self.root, text="BYPASS IOBIT (Backup + Delete)",
            command=self.make_unrestricted,
            bg=ACCENT, fg="white", font=("Segoe UI", 13, "bold"),
            width=30, height=2, relief="flat", bd=0
        ).pack(pady=10)
        
        self.restricted_btn = tk.Button(
            self.root, text="RESTORE IOBIT",
            command=self.make_restricted,
            bg=BUTTON_BG, fg=DARK_FG, font=("Segoe UI", 13, "bold"),
            width=30, height=2, relief="flat", bd=0, state="disabled"
        )
        self.restricted_btn.pack(pady=10)
        
        tk.Button(
            self.root, text="INSTALL IOBIT UNLOCKER 1.3.0",
            command=self.install_iobit,
            bg="#2196f3", fg="white", font=("Segoe UI", 13, "bold"),
            width=30, height=2, relief="flat", bd=0
        ).pack(pady=10)
        
        tk.Label(
            self.root, 
            text="Note: For delete/restore operations run as Administrator\nRight-click → Run as administrator",
            bg=DARK_BG, fg="#888888", font=("Segoe UI", 9), wraplength=480
        ).pack(pady=20)
    
    def make_unrestricted(self):
        if not os.path.exists(self.ini_path):
            messagebox.showerror("Error", "Configuration file not found!")
            return
        
        try:
            os.makedirs(os.path.dirname(self.backup_path), exist_ok=True)
            shutil.copy2(self.ini_path, self.backup_path)
            os.remove(self.ini_path)
            
            self.status.config(text="Success! Unrestricted mode activated", fg="#4caf50")
            self.restricted_btn.config(state="normal")
            messagebox.showinfo("Completed", "Operation successful. Restrictions removed.")
        except PermissionError:
            messagebox.showerror("Permission Denied", "Access denied!\nPlease run as Administrator.")
        except Exception as e:
            messagebox.showerror("Error", "Operation failed. Try closing the program and running again.")
    
    def make_restricted(self):
        if not os.path.exists(self.backup_path):
            messagebox.showerror("Error", "No backup found! Run unrestricted mode first.")
            return
        
        try:
            shutil.copy2(self.backup_path, self.ini_path)
            self.status.config(text="Restricted mode restored", fg="#2196f3")
            self.restricted_btn.config(state="disabled")
            messagebox.showinfo("Completed", "Original configuration restored.")
        except PermissionError:
            messagebox.showerror("Permission Denied", "Access denied!\nPlease run as Administrator.")
        except Exception as e:
            messagebox.showerror("Error", "Restore failed.")
    
    def install_iobit(self):
        try:
            # Direkt indirme başlatılıyor, herhangi bir guide/onay mesajı göstermeden
            webbrowser.open("https://github.com/Arasswys/Iob-t-Unlocker/raw/refs/heads/main/unlocker-setup.exe")
            self.status.config(text="Download started in background...", fg="#4caf50")
        except Exception as e:
            messagebox.showerror("Error", "Failed to start download.")

if __name__ == "__main__":
    root = tk.Tk()
    app = IObitUnlockerManager(root)
    root.mainloop()