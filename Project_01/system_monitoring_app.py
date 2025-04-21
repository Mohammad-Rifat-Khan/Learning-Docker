
import tkinter as tk
from tkinter import ttk
import psutil
import time

class SystemMonitorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("System Resource Monitor")
        self.root.geometry("400x300")

        self.cpu_label = ttk.Label(root, text="CPU Usage: ", font=("Arial", 14))
        self.cpu_label.pack(pady=10)

        self.ram_label = ttk.Label(root, text="RAM Usage: ", font=("Arial", 14))
        self.ram_label.pack(pady=10)

        self.disk_label = ttk.Label(root, text="Disk Usage: ", font=("Arial", 14))
        self.disk_label.pack(pady=10)

        self.net_label = ttk.Label(root, text="Network I/O: ", font=("Arial", 14))
        self.net_label.pack(pady=10)

        self.update_stats()

    def update_stats(self):
        cpu = psutil.cpu_percent()
        ram = psutil.virtual_memory().percent
        disk = psutil.disk_usage('/').percent
        net_io = psutil.net_io_counters()
        net_sent = round(net_io.bytes_sent / 1024 / 1024, 2)
        net_recv = round(net_io.bytes_recv / 1024 / 1024, 2)

        self.cpu_label.config(text=f"CPU Usage: {cpu}%")
        self.ram_label.config(text=f"RAM Usage: {ram}%")
        self.disk_label.config(text=f"Disk Usage: {disk}%")
        self.net_label.config(text=f"Net Sent: {net_sent} MB | Recv: {net_recv} MB")

        self.root.after(1000, self.update_stats)

if __name__ == "__main__":
    root = tk.Tk()
    app = SystemMonitorApp(root)
    root.mainloop()
