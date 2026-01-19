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

class CreditsWindow:
    def __init__(self, parent):
        self.window = tk.Toplevel(parent)
        self.window.title("Credits")
        self.window.geometry("300x120")
        self.window.configure(bg=DARK_BG)
        self.window.resizable(False, False)
        
        # Başlık
        tk.Label(
            self.window, text="CREDITS",
            font=TITLE_FONT, bg=DARK_BG, fg=ACCENT
        ).pack(pady=10)
        
        # İçerik
        tk.Label(
            self.window, text="By: Arasswys",
            bg=DARK_BG, fg=DARK_FG, font=FONT
        ).pack(pady=5)
        
        tk.Label(
            self.window, text="Yt Channel: youtube.com/@Slotshz",
            bg=DARK_BG, fg="#2196f3", font=FONT,
            cursor="hand2"
        ).pack(pady=5)
        
        # Kapat butonu
        tk.Button(
            self.window, text="CLOSE",
            command=self.window.destroy,
            bg=ACCENT, fg="white", font=("Segoe UI", 10, "bold"),
            width=15, relief="flat", bd=0
        ).pack(pady=10)
        
        # YouTube linkine tıklanabilirlik
        for widget in self.window.winfo_children():
            if "youtube.com" in widget.cget("text"):
                widget.bind("<Button-1>", lambda e: webbrowser.open("https://www.youtube.com/@Slotshz"))

class IObitUnlockerManager:
    def __init__(self, root):
        self.root = root
        self.root.title("IObit Unlocker Bypasser")
        self.root.geometry("520x420")
        self.root.configure(bg=DARK_BG)
        self.root.resizable(False, False)
        
        # Yolları gizli tutmak için sadece iç kullanımda tutuyoruz
        self.ini_path = r"C:\Program Files (x86)\IObit\IObit Unlocker\SpecialDir.ini"
        self.backup_path = r"C:\Backup\SpecialDir.ini"
        
        self.setup_ui()
    
    def setup_ui(self):
        tk.Label(
            self.root, text="IObit Unlocker Manager",
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
            self.root, text="BYPASS IOBIT UNLOCKER",
            command=self.make_unrestricted,
            bg=ACCENT, fg="white", font=("Segoe UI", 13, "bold"),
            width=35, height=2, relief="flat", bd=0
        ).pack(pady=8)
        
        tk.Button(
            self.root, text="RETURN DEFAULT",
            command=self.make_restricted,
            bg="#2196f3", fg="white", font=("Segoe UI", 13, "bold"),
            width=35, height=2, relief="flat", bd=0
        ).pack(pady=8)
        
        tk.Button(
            self.root, text="INSTALL IOBIT UNLOCKER 1.3.0",
            command=self.install_iobit,
            bg="#4CAF50", fg="white", font=("Segoe UI", 13, "bold"),
            width=35, height=2, relief="flat", bd=0
        ).pack(pady=8)
        
        tk.Label(
            self.root, 
            text="Note: For delete/restore operations run as Administrator\nRight-click → Run as administrator",
            bg=DARK_BG, fg="#888888", font=("Segoe UI", 9), wraplength=480
        ).pack(pady=20)
        
        # Sağ alt köşeye Credits butonu
        credits_btn = tk.Button(
            self.root, text="Credits",
            command=self.show_credits,
            bg=BUTTON_BG, fg=DARK_FG, font=("Segoe UI", 9),
            width=8, relief="flat", bd=0
        )
        credits_btn.place(relx=0.95, rely=0.95, anchor="se")
    
    def show_credits(self):
        CreditsWindow(self.root)
    
    def make_unrestricted(self):
        if not os.path.exists(self.ini_path):
            messagebox.showerror("Error", "Configuration file not found!")
            return
        
        try:
            os.makedirs(os.path.dirname(self.backup_path), exist_ok=True)
            shutil.copy2(self.ini_path, self.backup_path)
            os.remove(self.ini_path)
            
            self.status.config(text="Success! Restrictions removed", fg="#4caf50")
            messagebox.showinfo("Completed", "Operation successful. Restrictions removed.")
        except PermissionError:
            messagebox.showerror("Permission Denied", "Access denied!\nPlease run as Administrator.")
        except Exception as e:
            messagebox.showerror("Error", "Operation failed. Try closing the program and running again.")
    
    def make_restricted(self):
        if not os.path.exists(self.backup_path):
            messagebox.showerror("Error", "Iobıt is unbypassed. Bypass IOBit first.")
            return
        
        try:
            shutil.copy2(self.backup_path, self.ini_path)
            self.status.config(text="Original configuration restored", fg="#2196f3")
            messagebox.showinfo("Completed", "Original configuration restored.")
        except PermissionError:
            messagebox.showerror("Permission Denied", "Access denied!\nPlease run as Administrator.")
        except Exception as e:
            messagebox.showerror("Error", "Restore failed.")
    
    def install_iobit(self):
        try:
            webbrowser.open("https://github.com/Arasswys/Iob-t-Unlocker/raw/refs/heads/main/unlocker-setup.exe")
            self.status.config(text="Download started in background...", fg="#4caf50")
        except Exception as e:
            messagebox.showerror("Error", "Failed to start download.")

if __name__ == "__main__":
    root = tk.Tk()
    app = IObitUnlockerManager(root)
    root.mainloop()