import tkinter as tk
from tkinter import messagebox

class RDVApp:

    def __init__(self, root):
        self.root = root
        self.root.title("Gestion des Rendez-vous (30 min)")
        self.root.geometry("500x400")

        self.slots = {}

        self.create_interface()


    def create_interface(self):

        title = tk.Label(
            self.root,
            text="Agenda des Rendez-vous",
            font=("Arial", 16, "bold")
        )
        title.pack(pady=10)

        subtitle = tk.Label(
            self.root,
            text="Clique sur un créneau pour réserver",
            font=("Arial", 10)
        )
        subtitle.pack(pady=5)

        frame = tk.Frame(self.root)
        frame.pack(pady=20)

        # Horaires : 09:00 → 17:00
        start_hour = 9
        end_hour = 17

        row = 0

        for hour in range(start_hour, end_hour):
            for minute in [0, 30]:

                time_slot = f"{hour:02d}:{minute:02d}"

                btn = tk.Button(
                    frame,
                    text=time_slot,
                    width=12,
                    height=2,
                    bg="lightgreen",
                    command=lambda t=time_slot: self.reserve_slot(t)
                )

                btn.grid(row=row, column=0, padx=10, pady=5, sticky="w")

                self.slots[time_slot] = btn

                row += 1


    def reserve_slot(self, time_slot):

        button = self.slots[time_slot]

        if button["state"] == "disabled":
            messagebox.showwarning("Indisponible", "Ce créneau est déjà réservé")
            return

        confirm = messagebox.askyesno(
            "Confirmation",
            f"Réserver le RDV à {time_slot} ?"
        )

        if confirm:

            button.config(
                state="disabled",
                bg="red",
                text=f"{time_slot} ❌"
            )

            messagebox.showinfo(
                "Succès",
                f"RDV confirmé à {time_slot}"
            )


# =================================================
# RUN APPLICATION
# =================================================

if __name__ == "__main__":
    root = tk.Tk()
    app = RDVApp(root)
    root.mainloop()