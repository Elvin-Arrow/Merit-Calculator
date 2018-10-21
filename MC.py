import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


def calculateMerit(event):
    merit_holder.place(x=132, y=498)
    merit.place(x=164, y=510)
    try:
        s_total = int(ssc_total.get())
        s_obtained = int(ssc_obtained.get())
        h_total = int(hssc_total.get())
        h_obtained = int(hssc_obtained.get())
        n_obtained = int(nat_obtained.get())
        m = round(((s_obtained / s_total) * 10) + ((h_obtained / h_total) * 40) + (n_obtained / 2), 2)
        yf = year_fac.get()
        if yf == "0":
            pass
        elif yf == "1":
            m -= 2
        elif yf == "2":
            m -= 4
        elif yf == "3":
            m -= 6
        else:
            m -= 8
        m = round(m, 2)
            
    except:
        s_total = int(ssc_total.get())
        s_obtained = 0
        h_total = int(hssc_total.get())
        h_obtained = 0
        n_obtained = 0
        m = round(((s_obtained / s_total) * 10) + ((h_obtained / h_total) * 40) + (n_obtained / 2), 2)
    if m < 10:
        merit.place(x=180, y=510)
        
    temp = "Merit : " + str(m)
    merit.config(text=temp)
    root.update()


def alevel_set():
    ssc_header.configure(text="O'levels")
    hssc_header.configure(text="A'levels")
    ssc_total.set(900)
    total_ssc.config(textvariable=ssc_total)
    hssc_total.set(1100)
    total_hssc.config(textvariable=hssc_total)
    temp = awaiting_var.get()
    if temp == 1:
        hssc_obtained.set(660)
        obtained_hssc.config(textvariable=hssc_obtained)


def fsc_set():
    ssc_header.configure(text="SSC")
    hssc_header.configure(text="HSSC")
    ssc_total.set(1050)
    total_ssc.config(textvariable=ssc_total)
    hssc_obtained.set("")
    obtained_hssc.config(textvariable=hssc_obtained)
    temp = awaiting_var.get()
    if temp == 1:
        hssc_total.set(520)
        total_hssc.config(textvariable=hssc_total)

def result_awaiting():
    state = awaiting_var.get()
    if state == 1: # if result awaiting
        degree = degreeVar.get()
        if degree == 1: # Degree is FSc
            hssc_total.set(520)
            total_hssc.config(textvariable=hssc_total)
            hssc_obtained.set("")
            obtained_hssc.config(textvariable=hssc_obtained)

        else:
            hssc_total.set(1100)
            total_hssc.configure(textvariable=hssc_total)
            hssc_obtained.set(660)
            obtained_hssc.config(textvariable=hssc_obtained)
    else:
        reset()


def reset():
    temp = degreeVar.get()
    if temp == 1: # if fsc
        ssc_total.set(1050)
        total_ssc.config(textvariable=ssc_total)
        ssc_obtained.set("")
        obtained_ssc.config(textvariable=ssc_obtained)
        hssc_total.set(1100)
        total_hssc.config(textvariable=hssc_total)
        hssc_obtained.set("")
        obtained_hssc.config(textvariable=hssc_obtained)

    elif temp == 2: # if a'levels
        ssc_total.set(900)
        total_ssc.config(textvariable=ssc_total)
        ssc_obtained.set("")
        obtained_ssc.config(textvariable=ssc_obtained)
        hssc_total.set(1100)
        total_hssc.config(textvariable=hssc_total)
        hssc_obtained.set("")
        obtained_hssc.config(textvariable=hssc_obtained)
    # degreeVar.set(1)
    nat_obtained.set("")
    obtained_nat.config(textvariable=nat_obtained)
    year_fac.set("0")
    merit.config(text="")
    merit.place_forget()
    merit_holder.place_forget()
    awaiting_var.set(0)
    root.update()


# Fonts
headerFont = ("Old English Text MT", 34)
headingFont = ("Verdana", 14)
defaultFont = ("Verdana", 12)

# Main window
root = tk.Tk()
root.title("Merit Calculator")
root.resizable(width=False, height=False)
root.geometry("500x700+50+30")

background = tk.PhotoImage(file="Background.png")
mainframe = tk.Label(root, image=background)
mainframe.pack()

header = tk.Label(root, text="Merit Calculator", font=headerFont, bg="#00628B", fg="#E6E6DC")
header.place(x=95, y=20)

# Degree header
degree_header = ttk.Label(root, text="Select Degree", background="#92278F", foreground="#E6E6DC", font=headingFont)
degree_header.place(x=10, y=110)

# Degree radio buttons
degreeVar = tk.IntVar()
degreeVar.set(1)
radioButton_style = ttk.Style()
radioButton_style.configure('edu_degree.TRadiobutton', font=defaultFont, background="#E6E6DC")

fsc = ttk.Radiobutton(root, text="Matriculate", value=1, variable=degreeVar, style='edu_degree.TRadiobutton',
                      command=fsc_set)
fsc.place(x=25, y=145)

alevels = ttk.Radiobutton(root, text="Cambridge", value=2, variable=degreeVar, style='edu_degree.TRadiobutton',
                          command=alevel_set)
alevels.place(x=25, y=170)

# Score header
score_header = ttk.Label(root, text="Key in the scores", background="#92278F", foreground="#E6E6DC", font=headingFont)
score_header.place(x=10, y=200)

# Entry style setup
entry_style = ttk.Style()
entry_style.configure('score_entry.TEntry', font=defaultFont)
entry_style.map('score_entry.TEntry',
                background=[('disabled', "#E6E6DC")])

# Score setup
total_score = ttk.Label(root, text="Total", background="#E6E6DC", font=defaultFont)
total_score.place(x=160, y=235)
obtained_score = ttk.Label(root, text="Obtained", background="#E6E6DC", font=defaultFont)
obtained_score.place(x=285, y=235)

# SSC header setup
ssc_header = ttk.Label(root, text="SSC", background="#E6E6DC", font=defaultFont)
ssc_header.place(x=25, y=265)

# SSC score entry setup
ssc_total = tk.StringVar()
ssc_total.set(1050)
ssc_obtained = tk.StringVar()

total_ssc = ttk.Entry(root, textvariable=ssc_total, justify=tk.CENTER, style='score_entry.TEntry')
total_ssc.place(x=120, y=267)

obtained_ssc = ttk.Entry(root, textvariable=ssc_obtained, justify=tk.CENTER, style='score_entry.TEntry')
obtained_ssc.place(x=260, y=267)

# HSSC header setup
hssc_header = ttk.Label(root, text="HSSC", background="#E6E6DC", font=defaultFont)
hssc_header.place(x=25, y=305)

# HSSC score entry setup
hssc_total = tk.StringVar()
hssc_total.set(1100)
hssc_obtained = tk.StringVar()

total_hssc = ttk.Entry(root, textvariable=hssc_total, justify=tk.CENTER, style='score_entry.TEntry')
total_hssc.place(x=120, y=307)

obtained_hssc = ttk.Entry(root, textvariable=hssc_obtained, justify=tk.CENTER, style='score_entry.TEntry')
obtained_hssc.place(x=260, y=307)

checkbutton = ttk.Style()
checkbutton.configure('await_bt.TRadiobutton', background="#E6E6DC")
var = "  Result\nawaiting?"
awaiting_var = tk.IntVar()
awaiting = ttk.Checkbutton(root, text=var, variable=awaiting_var, command=result_awaiting, style='await_bt.TRadiobutton')
awaiting.place(x=400, y=298)

# NAT header setup
nat_header = ttk.Label(root, text="NAT", background="#E6E6DC", font=defaultFont)
nat_header.place(x=25, y=345)

# NAT score entry setup
nat_total = tk.IntVar()
nat_total.set(100)
nat_obtained = tk.StringVar()
total_nat = ttk.Entry(root, textvariable=nat_total, justify=tk.CENTER, style='score_entry.TEntry', state='disabled')
total_nat.place(x=120, y=347)

obtained_nat = ttk.Entry(root, textvariable=nat_obtained, justify=tk.CENTER, style='score_entry.TEntry')
obtained_nat.place(x=260, y=347)

# Year Factor drop-down list
year_fac = tk.StringVar(root)
year_fac.set(0)
factor_header = ttk.Label(root, text="Year Factor", font=defaultFont, background="#E6E6DC")
factor_header.place(x=25, y=385)
year_gap = ttk.Combobox(root, justify=tk.CENTER, width=15, textvariable=year_fac,
                        values=("0", "1", "2", "3", "4", "Above 4"))
year_gap.place(x=132, y=387)

# Button style
button_style = ttk.Style()
button_style.configure('button_style.TButton', background="#81A594")

# Calculate button
calculate = tk.Button(root, text="Calculate", font=defaultFont, relief=tk.GROOVE, padx=25, pady=10, bg="#81A594")
calculate.bind('<Button-1>', calculateMerit)
root.bind('<Return>', calculateMerit)
calculate.place(x=185, y=435)

# Reset Button
reset_button = tk.Button(root, text="Reset", command=reset, bg="#81A594", relief=tk.GROOVE, padx=20)
reset_button.place(x=420, y=645)

# Merit Label
holder = tk.PhotoImage(file="Merit Label.png")
merit_holder = tk.Label(root, image=holder, bg="#E6E6DC")
mFont = ("Verdana", 20)
merit = tk.Label(root, font=mFont, bg="#92278F", fg="#E6E6DC")

exitButton = tk.Button(root, text="Exit", relief=tk.GROOVE, padx=25, pady=2, command=root.destroy, bg="#81A594")

root.mainloop()
