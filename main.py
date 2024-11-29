import tkinter as tk
from tkinter import ttk
import random
import time

class SzinvalasztoJatek:
    def __init__(self, root):
        self.root = root
        self.root.title("Színválasztó Játék")
        
        # Inicializálás
        self.szinek = ["red", "green", "blue", "yellow", "orange", "purple", "pink", "black", "white", "brown"]
        self.aktualis_szo = None
        self.aktualis_szin = None
        self.start_time = None
        self.best_time = None
        self.valasztott_szinek_szama = tk.IntVar(value=4)
        
        # Felület elemei
        self.setup_ui()
        self.uj_feladat()

    def setup_ui(self):
        # Színek száma Dropdown
        ttk.Label(self.root, text="Hány szín legyen?").grid(row=0, column=0, padx=10, pady=5)
        self.dropdown = ttk.Combobox(self.root, textvariable=self.valasztott_szinek_szama, 
                                     values=list(range(2, len(self.szinek) + 1)), state="readonly")
        self.dropdown.grid(row=0, column=1, padx=10, pady=5)
        self.dropdown.bind("<<ComboboxSelected>>", self.dropdown_valtozas)

        # Szó színe Label
        self.szo_label = ttk.Label(self.root, text="Szó", font=("Helvetica", 24))
        self.szo_label.grid(row=1, column=0, columnspan=2, pady=20)

        # Eredmény Entry
        self.entry = ttk.Entry(self.root, font=("Helvetica", 16))
        self.entry.grid(row=2, column=0, columnspan=2, pady=10)
        self.entry.bind("<Return>", self.ellenoriz)

        # Eltelt idő Label
        ttk.Label(self.root, text="Eltelt idő:").grid(row=3, column=0, padx=10, pady=5)
        self.ido_label = ttk.Label(self.root, text="0.00 s", font=("Helvetica", 16))
        self.ido_label.grid(row=3, column=1, padx=10, pady=5)

        # Legjobb idő Label
        ttk.Label(self.root, text="Legjobb idő:").grid(row=4, column=0, padx=10, pady=5)
        self.best_time_label = ttk.Label(self.root, text="N/A", font=("Helvetica", 16))
        self.best_time_label.grid(row=4, column=1, padx=10, pady=5)

        # Visszajelzés Label
        self.visszajelzes_label = ttk.Label(self.root, text="", font=("Helvetica", 16))
        self.visszajelzes_label.grid(row=5, column=0, columnspan=2, pady=10)

        # Új feladat gomb
        self.uj_feladat_gomb = ttk.Button(self.root, text="Új feladat", command=self.uj_feladat)
        self.uj_feladat_gomb.grid(row=6, column=0, columnspan=2, pady=10)

    def dropdown_valtozas(self, event):
        """Dropdown esemény kezelése."""
        self.uj_feladat()

    def uj_feladat(self):
        """Új szín és szó generálása."""
        szinek_szama = self.valasztott_szinek_szama.get()
        valasztott_szinek = random.sample(self.szinek, szinek_szama)
        self.aktualis_szo = random.choice(valasztott_szinek)
        self.aktualis_szin = random.choice(valasztott_szinek)
        self.szo_label.config(text=self.aktualis_szo, foreground=self.aktualis_szin)
        self.start_time = time.time()
        self.visszajelzes_label.config(text="")
        self.entry.delete(0, tk.END)

    def ellenoriz(self, event=None):
        """Felhasználó válaszának ellenőrzése."""
        valasz = self.entry.get().strip().lower()
        if valasz == self.aktualis_szin:
            eltelt_ido = time.time() - self.start_time
            self.ido_label.config(text=f"{eltelt_ido:.2f} s")
            if self.best_time is None or eltelt_ido < self.best_time:
                self.best_time = eltelt_ido
                self.best_time_label.config(text=f"{self.best_time:.2f} s")
            self.visszajelzes_label.config(text="Helyes!", foreground="green")
            self.uj_feladat()
        else:
            self.visszajelzes_label.config(text="Helytelen! Próbáld újra.", foreground="red")
            self.entry.delete(0, tk.END)

# Program indítása
if __name__ == "__main__":
    root = tk.Tk()
    app = SzinvalasztoJatek(root)
    root.mainloop()
