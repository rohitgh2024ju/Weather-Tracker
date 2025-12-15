# making gui

import tkinter as tk


def start_gui(process_city, fetch_history):
    root = tk.Tk()
    root.geometry("520x360")
    root.title("Weather Tracker")
    root.resizable(False, False)

    header = tk.Frame(root)
    header.pack(pady=10)

    tk.Label(header, text="Weather Tracker", font=("Arial", 16, "bold")).pack()

    tk.Label(
        header, text="Track weather of any available city", font=("Arial", 9), fg="gray"
    ).pack()

    input_frame = tk.Frame(root)
    input_frame.pack(pady=15)

    tk.Label(input_frame, text="City:").grid(row=0, column=0, padx=5)

    city_entry = tk.Entry(input_frame, width=18)
    city_entry.grid(row=0, column=1, padx=5)

    output_frame = tk.Frame(root)
    output_frame.pack(pady=10)

    display = tk.Label(output_frame, text="---", font=("Arial", 10))
    display.pack()

    history_frame = tk.Frame(root)
    history_frame.pack(pady=10)

    history_title = tk.Label(
        history_frame, text="Recent Searches", font=("Arial", 10, "bold")
    )
    history_title.pack()

    history_container = tk.Frame(history_frame)
    history_container.pack()


    def on_click_check():
        city = city_entry.get()
        if not city:
            return
        city_entry.delete(0, tk.END)

        temp, cond = process_city(city)
        display.config(text=f"[{city} → {temp}°C | {cond}]")

    def on_click_history():
        for widget in history_container.winfo_children():
            widget.destroy()

        data = fetch_history()
        if not data:
            tk.Label(history_container, text="No history yet").pack()
            return

        for item in data:
            text = f"{item['city']} | {item['temperature']}°C | {item['condition']}"
            tk.Label(history_container, text=text, anchor="w").pack(fill="x")

        root.after(6000, lambda: clear_history())

    def clear_history():
        for widget in history_container.winfo_children():
            widget.destroy()

    button_frame = tk.Frame(root)
    button_frame.pack(pady=10)

    tk.Button(
        button_frame, text="Check Weather", width=14, command=on_click_check
    ).grid(row=0, column=0, padx=5)

    tk.Button(button_frame, text="History", width=10, command=on_click_history).grid(
        row=0, column=1, padx=5
    )

    root.mainloop()
