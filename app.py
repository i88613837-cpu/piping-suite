import csv
import math
import os
import sys
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

class UltimateIndustrialPipingSuite:
    def __init__(self, root):
        self.root = root
        self.root.title("Ultimate Industrial Piping Suite v10.0 - Eng. Ibrahim Baaloul")
        self.root.geometry("1250x880")
        self.root.configure(bg="#ffffff")

        self.colors = {
            "bg": "#ffffff",
            "card_bg": "#f8fafc",
            "text_main": "#0f172a",
            "result_text": "#000000",
            "result_title": "#dc2626",
            "entry_bg": "#ffffff"
        }

        # Header Banner
        header_frame = tk.Frame(root, bg=self.colors["card_bg"], height=70, bd=1, relief="solid")
        header_frame.pack(fill="x", padx=15, pady=(10, 5))
        header_frame.pack_propagate(False)

        tk.Frame(header_frame, bg=self.colors["result_title"], width=6).pack(side="left", fill="y")
        
        header_text_frame = tk.Frame(header_frame, bg=self.colors["card_bg"])
        header_text_frame.pack(side="left", padx=15, pady=8)

        tk.Label(
            header_text_frame,
            text="ULTIMATE INDUSTRIAL PIPING SUITE V10.0",
            font=("Segoe UI", 12, "bold"),
            fg=self.colors["result_title"],
            bg=self.colors["card_bg"],
        ).pack(anchor="w")
        
        tk.Label(
            header_text_frame,
            text="Eng. Ibrahim Baaloul (Abu Malek) - El-Dabaa Suite",
            font=("Segoe UI", 9, "bold"),
            fg=self.colors["text_main"],
            bg=self.colors["card_bg"],
        ).pack(anchor="w")

        # Notebook Tabs
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill="both", expand=True, padx=15, pady=5)

        self.tab1 = tk.Frame(self.notebook, bg=self.colors["bg"])
        self.tab2 = tk.Frame(self.notebook, bg=self.colors["bg"])
        self.tab3 = tk.Frame(self.notebook, bg=self.colors["bg"])
        self.tab4 = tk.Frame(self.notebook, bg=self.colors["bg"])
        self.tab5 = tk.Frame(self.notebook, bg=self.colors["bg"])

        self.notebook.add(self.tab1, text=" 1. Lobster ")
        self.notebook.add(self.tab2, text=" 2. Branch ")
        self.notebook.add(self.tab3, text=" 3. Flange ")
        self.notebook.add(self.tab4, text=" 4. Thermal ")
        self.notebook.add(self.tab5, text=" 5. Supports ")

        self.build_tab1_lobster()
        self.build_tab2_branch()
        self.build_tab3_flanges()
        self.build_tab4_thermal()
        self.build_tab5_supports()

        # Status Bar
        self.status_bar = tk.Label(
            root, text=" Ready • Mobile Field Mode Active", font=("Segoe UI", 9, "bold"), fg=self.colors["text_main"], bg=self.colors["card_bg"], anchor="w", padx=10, bd=1, relief="solid"
        )
        self.status_bar.pack(side="bottom", fill="x", ipady=4)

    def create_card(self, parent, title):
        return tk.LabelFrame(
            parent, text=title, font=("Segoe UI", 10, "bold"), fg=self.colors["result_title"], bg=self.colors["card_bg"], bd=1, relief="solid"
        )

    def create_button(self, parent, text, command):
        return tk.Button(parent, text=text, command=command, font=("Segoe UI", 10, "bold"), bg="#dc2626", fg="white", activebackground="#b91c1c", activeforeground="white", bd=0, padx=12, pady=6, cursor="hand2")

    # --- TAB 1: LOBSTER BACK ---
    def build_tab1_lobster(self):
        card = self.create_card(self.tab1, " Lobster Back / Mitered Bend Calculator ")
        card.pack(fill="x", padx=10, pady=10)
        f = tk.Frame(card, bg=self.colors["card_bg"])
        f.pack(fill="x", padx=15, pady=12)

        tk.Label(f, text="Pipe Outer Diameter (mm):", bg=self.colors["card_bg"], font=("Segoe UI", 10, "bold")).pack(anchor="w", pady=(4, 2))
        self.lb_dia = tk.Entry(f, font=("Segoe UI", 11), bd=1, relief="solid", width=25)
        self.lb_dia.pack(anchor="w", pady=(0, 8))
        self.lb_dia.insert(0, "400")

        tk.Label(f, text="Total Bend Angle (Degrees):", bg=self.colors["card_bg"], font=("Segoe UI", 10, "bold")).pack(anchor="w", pady=(4, 2))
        self.lb_angle = tk.Entry(f, font=("Segoe UI", 11), bd=1, relief="solid", width=25)
        self.lb_angle.pack(anchor="w", pady=(0, 8))
        self.lb_angle.insert(0, "90")

        tk.Label(f, text="Number of Segments:", bg=self.colors["card_bg"], font=("Segoe UI", 10, "bold")).pack(anchor="w", pady=(4, 2))
        self.lb_segs = tk.Entry(f, font=("Segoe UI", 11), bd=1, relief="solid", width=25)
        self.lb_segs.pack(anchor="w", pady=(0, 10))
        self.lb_segs.insert(0, "4")

        self.create_button(f, "Calculate Miter Angles", self.calc_lobster).pack(anchor="w", fill="x", pady=(5, 5), ipady=6)

        card_res = self.create_card(self.tab1, " Calculation Results ")
        card_res.pack(fill="both", expand=True, padx=10, pady=5)
        rf = tk.Frame(card_res, bg=self.colors["card_bg"])
        rf.pack(fill="both", expand=True, padx=15, pady=10)
        self.txt_lb = tk.Text(rf, font=("Consolas", 11, "bold"), bg="#ffffff", fg="#000000", bd=1, relief="solid", height=10)
        self.txt_lb.pack(side="left", fill="both", expand=True)

    def calc_lobster(self):
        try:
            d = float(self.lb_dia.get())
            tot_ang = float(self.lb_angle.get())
            segs = int(self.lb_segs.get())
            if segs < 2:
                raise ValueError
            cuts = segs - 1
            miter_ang = tot_ang / (2.0 * cuts)
            rep = [
                "========================================================",
                "       LOBSTER BACK (MITERED BEND) REPORT               ",
                "========================================================",
                f"• Pipe OD: {d} mm | Total Angle: {tot_ang}°",
                f"• Segments: {segs} (Miter Joints: {cuts})",
                "--------------------------------------------------------",
                f"-> Miter Angle per Joint: {miter_ang:.2f}°",
                "-> Note: End pieces cut at half the miter angle.",
                "========================================================"
            ]
            self.txt_lb.delete("1.0", tk.END)
            self.txt_lb.insert("1.0", "\n".join(rep))
        except ValueError:
            messagebox.showerror("Error", "Please enter valid values (Segments >= 2).")

    # --- TAB 2: BRANCH CONNECTION ---
    def build_tab2_branch(self):
        card = self.create_card(self.tab2, " Branch / Tee Intersection Calculator ")
        card.pack(fill="x", padx=10, pady=10)
        f = tk.Frame(card, bg=self.colors["card_bg"])
        f.pack(fill="x", padx=15, pady=12)

        tk.Label(f, text="Main Pipe Dia (mm):", bg=self.colors["card_bg"], font=("Segoe UI", 10, "bold")).pack(anchor="w", pady=(4, 2))
        self.br_main = tk.Entry(f, font=("Segoe UI", 11), bd=1, relief="solid", width=25)
        self.br_main.pack(anchor="w", pady=(0, 8))
        self.br_main.insert(0, "300")

        tk.Label(f, text="Branch Pipe Dia (mm):", bg=self.colors["card_bg"], font=("Segoe UI", 10, "bold")).pack(anchor="w", pady=(4, 2))
        self.br_branch = tk.Entry(f, font=("Segoe UI", 11), bd=1, relief="solid", width=25)
        self.br_branch.pack(anchor="w", pady=(0, 10))
        self.br_branch.insert(0, "150")

        self.create_button(f, "Calculate Saddle Cut Depth", self.calc_branch).pack(anchor="w", fill="x", pady=(5, 5), ipady=6)

        card_res = self.create_card(self.tab2, " Calculation Results ")
        card_res.pack(fill="both", expand=True, padx=10, pady=5)
        rf = tk.Frame(card_res, bg=self.colors["card_bg"])
        rf.pack(fill="both", expand=True, padx=15, pady=10)
        self.txt_br = tk.Text(rf, font=("Consolas", 11, "bold"), bg="#ffffff", fg="#000000", bd=1, relief="solid", height=10)
        self.txt_br.pack(side="left", fill="both", expand=True)

    def calc_branch(self):
        try:
            dm = float(self.br_main.get())
            db = float(self.br_branch.get())
            rb = db / 2.0
            rep = [
                "========================================================",
                "       BRANCH CONNECTION (SADDLE CUT) REPORT            ",
                "========================================================",
                f"• Main Pipe Dia: {dm} mm | Branch Dia: {db} mm",
                "--------------------------------------------------------",
                f"-> Max Saddle Cut-back Depth: {rb:.2f} mm",
                "-> Use standard cylindrical projection layout for cutting.",
                "========================================================"
            ]
            self.txt_br.delete("1.0", tk.END)
            self.txt_br.insert("1.0", "\n".join(rep))
        except ValueError:
            messagebox.showerror("Error", "Please enter valid diameters.")

    # --- TAB 3: FLANGE BOLTS ---
    def build_tab3_flanges(self):
        card = self.create_card(self.tab3, " Flange Bolts & Gaskets Reference ")
        card.pack(fill="x", padx=10, pady=10)
        f = tk.Frame(card, bg=self.colors["card_bg"])
        f.pack(fill="x", padx=15, pady=12)

        tk.Label(f, text="Flange Size (NPS):", bg=self.colors["card_bg"], font=("Segoe UI", 10, "bold")).pack(anchor="w", pady=(4, 2))
        self.fl_size = ttk.Combobox(f, values=["2 inch", "4 inch", "6 inch", "8 inch", "10 inch", "12 inch", "16 inch", "20 inch", "24 inch"], font=("Segoe UI", 11), state="readonly", width=23)
        self.fl_size.pack(anchor="w", pady=(0, 8))
        self.fl_size.current(1)

        tk.Label(f, text="Flange Rating:", bg=self.colors["card_bg"], font=("Segoe UI", 10, "bold")).pack(anchor="w", pady=(4, 2))
        self.fl_rating = ttk.Combobox(f, values=["150#", "300#", "600#"], font=("Segoe UI", 11), state="readonly", width=23)
        self.fl_rating.pack(anchor="w", pady=(0, 10))
        self.fl_rating.current(0)

        self.create_button(f, "Query Bolts & Gasket Info", self.calc_flange).pack(anchor="w", fill="x", pady=(5, 5), ipady=6)

        card_res = self.create_card(self.tab3, " Reference Results ")
        card_res.pack(fill="both", expand=True, padx=10, pady=5)
        rf = tk.Frame(card_res, bg=self.colors["card_bg"])
        rf.pack(fill="both", expand=True, padx=15, pady=10)
        self.txt_fl = tk.Text(rf, font=("Consolas", 11, "bold"), bg="#ffffff", fg="#000000", bd=1, relief="solid", height=10)
        self.txt_fl.pack(side="left", fill="both", expand=True)

    def calc_flange(self):
        sz = self.fl_size.get()
        rt = self.fl_rating.get()
        data = {
            "2 inch": ("4 Bolts", "5/8 inch (UNC)", "Standard RF Gasket"),
            "4 inch": ("8 Bolts", "5/8 inch (UNC)", "Standard RF Gasket"),
            "6 inch": ("12 Bolts", "3/4 inch (UNC)", "Standard RF Gasket"),
            "8 inch": ("12 Bolts", "3/4 inch (UNC)", "Standard RF Gasket"),
            "10 inch": ("16 Bolts", "7/8 inch (UNC)", "Standard RF Gasket"),
            "12 inch": ("16 Bolts", "7/8 inch (UNC)", "Standard RF Gasket"),
            "16 inch": ("20 Bolts", "1 inch (UNC)", "Spiral Wound Gasket"),
            "20 inch": ("24 Bolts", "1-1/8 inch", "Spiral Wound Gasket"),
            "24 inch": ("24 Bolts", "1-1/4 inch", "Spiral Wound Gasket")
        }
        res = data.get(sz, ("8 Bolts", "3/4 inch", "Standard Gasket"))
        rep = [
            "========================================================",
            "       FLANGE BOLTS & GASKET REFERENCE                  ",
            "========================================================",
            f"• Flange Size: {sz} | Rating: {rt}",
            "--------------------------------------------------------",
            f"-> Number of Bolts: {res[0]}",
            f"-> Bolt Size: {res[1]}",
            f"-> Gasket Type: {res[2]}",
            "========================================================"
        ]
        self.txt_fl.delete("1.0", tk.END)
        self.txt_fl.insert("1.0", "\n".join(rep))

    # --- TAB 4: THERMAL EXPANSION ---
    def build_tab4_thermal(self):
        card = self.create_card(self.tab4, " Thermal Expansion & Loop Calculator ")
        card.pack(fill="x", padx=10, pady=10)
        f = tk.Frame(card, bg=self.colors["card_bg"])
        f.pack(fill="x", padx=15, pady=12)

        tk.Label(f, text="Total Pipe Length (m):", bg=self.colors["card_bg"], font=("Segoe UI", 10, "bold")).pack(anchor="w", pady=(4, 2))
        self.th_len = tk.Entry(f, font=("Segoe UI", 11), bd=1, relief="solid", width=25)
        self.th_len.pack(anchor="w", pady=(0, 8))
        self.th_len.insert(0, "50")

        tk.Label(f, text="Temp Difference (°C):", bg=self.colors["card_bg"], font=("Segoe UI", 10, "bold")).pack(anchor="w", pady=(4, 2))
        self.th_dt = tk.Entry(f, font=("Segoe UI", 11), bd=1, relief="solid", width=25)
        self.th_dt.pack(anchor="w", pady=(0, 8))
        self.th_dt.insert(0, "80")

        tk.Label(f, text="Material:", bg=self.colors["card_bg"], font=("Segoe UI", 10, "bold")).pack(anchor="w", pady=(4, 2))
        self.th_mat = ttk.Combobox(f, values=["Carbon Steel", "Stainless Steel"], font=("Segoe UI", 11), state="readonly", width=23)
        self.th_mat.pack(anchor="w", pady=(0, 10))
        self.th_mat.current(0)

        self.create_button(f, "Calculate Expansion & Loop", self.calc_thermal).pack(anchor="w", fill="x", pady=(5, 5), ipady=6)

        card_res = self.create_card(self.tab4, " Calculation Results ")
        card_res.pack(fill="both", expand=True, padx=10, pady=5)
        rf = tk.Frame(card_res, bg=self.colors["card_bg"])
        rf.pack(fill="both", expand=True, padx=15, pady=10)
        self.txt_th = tk.Text(rf, font=("Consolas", 11, "bold"), bg="#ffffff", fg="#000000", bd=1, relief="solid", height=10)
        self.txt_th.pack(side="left", fill="both", expand=True)

    def calc_thermal(self):
        try:
            L = float(self.th_len.get())
            dt = float(self.th_dt.get())
            alpha = 11.7e-6 if "Carbon" in self.th_mat.get() else 16.5e-6
            delta_l = alpha * L * 1000.0 * dt
            loop_len = 2.0 * math.sqrt(6.0 * 100.0 * delta_l)
            rep = [
                "========================================================",
                "       THERMAL EXPANSION REPORT                         ",
                "========================================================",
                f"• Pipe Length: {L} m | Temp Diff: {dt} °C",
                f"• Material: {self.th_mat.get()}",
                "--------------------------------------------------------",
                f"-> Expected Expansion (Delta L): {delta_l:.2f} mm",
                f"-> Approx. Expansion Loop Length: {loop_len:.2f} mm ({loop_len/1000:.2f} m)",
                "========================================================"
            ]
            self.txt_th.delete("1.0", tk.END)
            self.txt_th.insert("1.0", "\n".join(rep))
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numeric values.")

    # --- TAB 5: PIPE SUPPORTS ---
    def build_tab5_supports(self):
        card = self.create_card(self.tab5, " Pipe Support Maximum Spans Reference ")
        card.pack(fill="x", padx=10, pady=10)
        f = tk.Frame(card, bg=self.colors["card_bg"])
        f.pack(fill="x", padx=15, pady=12)

        tk.Label(f, text="Pipe Size (NPS):", bg=self.colors["card_bg"], font=("Segoe UI", 10, "bold")).pack(anchor="w", pady=(4, 2))
        self.sp_size = ttk.Combobox(f, values=["2 inch", "4 inch", "6 inch", "8 inch", "12 inch", "16 inch", "20 inch", "24 inch"], font=("Segoe UI", 11), state="readonly", width=23)
        self.sp_size.pack(anchor="w", pady=(0, 10))
        self.sp_size.current(1)

        self.create_button(f, "Query Maximum Support Span", self.calc_support).pack(anchor="w", fill="x", pady=(5, 5), ipady=6)

        card_res = self.create_card(self.tab5, " Reference Results ")
        card_res.pack(fill="both", expand=True, padx=10, pady=5)
        rf = tk.Frame(card_res, bg=self.colors["card_bg"])
        rf.pack(fill="both", expand=True, padx=15, pady=10)
        self.txt_sp = tk.Text(rf, font=("Consolas", 11, "bold"), bg="#ffffff", fg="#000000", bd=1, relief="solid", height=10)
        self.txt_sp.pack(side="left", fill="both", expand=True)

    def calc_support(self):
        sz = self.sp_size.get()
        spans = {
            "2 inch": "3.0 meters (10 ft)",
            "4 inch": "4.5 meters (15 ft)",
            "6 inch": "5.5 meters (18 ft)",
            "8 inch": "6.0 meters (20 ft)",
            "12 inch": "7.0 meters (23 ft)",
            "16 inch": "8.0 meters (26 ft)",
            "20 inch": "9.0 meters (30 ft)",
            "24 inch": "10.0 meters (33 ft)"
        }
        res = spans.get(sz, "5.0 meters")
        rep = [
            "========================================================",
            "       PIPE SUPPORT MAXIMUM SPAN REPORT                 ",
            "========================================================",
            f"• Pipe Size: {sz}",
            "--------------------------------------------------------",
            f"-> Maximum Span Between Supports: {res}",
            "-> Note: Reduce span near heavy valves or fittings.",
            "========================================================"
        ]
        self.txt_sp.delete("1.0", tk.END)
        self.txt_sp.insert("1.0", "\n".join(rep))

if __name__ == "__main__":
    root = tk.Tk()
    app = UltimateIndustrialPipingSuite(root)
    root.mainloop()
