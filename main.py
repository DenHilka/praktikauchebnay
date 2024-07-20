import tkinter as tk
from tkinter import messagebox
import subprocess
from datetime import datetime
def create_backup():
    db_host = entry_host.get()
    db_user = entry_user.get()
    db_password = entry_password.get()
    db_name = entry_db.get()
    backup_path = entry_path.get()
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    backup_file = f'{backup_path}/{db_name}_{timestamp}.sql'
    command = f'mysqldump -u {db_user} -p{db_password} -h {db_host} {db_name} > {backup_file}'
    subprocess.run(command, shell=True)
    messagebox.showinfo("Резервная копия", f"Резервная копия базы данных {db_name} создана в {backup_file}")
# Создание GUI
window = tk.Tk()
window.title("Создание резервной копии базы данных MySQL")
label_host = tk.Label(window, text="Хост:")
label_host.pack()
entry_host = tk.Entry(window)
entry_host.pack()
label_user = tk.Label(window, text="Пользователь:")
label_user.pack()
entry_user = tk.Entry(window)
entry_user.pack()
label_password = tk.Label(window, text="Пароль:")
label_password.pack()
entry_password = tk.Entry(window, show="*")
entry_password.pack()
label_db = tk.Label(window, text="Имя базы данных:")
label_db.pack()
entry_db = tk.Entry(window)
entry_db.pack()
label_path = tk.Label(window, text="Путь для сохранения резервной копии:")
label_path.pack()
entry_path = tk.Entry(window)
entry_path.pack()
btn_create_backup = tk.Button(window, text="Создать резервную копию", command=create_backup)
btn_create_backup.pack()
window.mainloop()