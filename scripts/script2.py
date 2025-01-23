import tkinter as tk
from tkinter import ttk, filedialog
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Load data
file_path = "D:/BI19/HR_Data_Visualization/data/HumanResources.csv"
data = pd.read_csv(file_path, delimiter=';', header=0)

# Prepare data
data['Termdate'] = data['Termdate'].fillna('N/A')
data['Hiredate'] = pd.to_datetime(data['Hiredate'], format='%d/%m/%Y', errors='coerce')
data['Birthdate'] = pd.to_datetime(data['Birthdate'], format='%d/%m/%Y', errors='coerce')
data['Termdate'] = pd.to_datetime(data['Termdate'], format='%d/%m/%Y', errors='coerce')
data['Salary'] = pd.to_numeric(data['Salary'], errors='coerce')

# Create the main window
root = tk.Tk()
root.title("HR Data Visualizations")
root.geometry("1200x800")

# Create frames for each page
frame_main = tk.Frame(root)
frame_visualizations = tk.Frame(root)
frame_data = tk.Frame(root)

for frame in (frame_main, frame_visualizations, frame_data):
    frame.grid(row=0, column=0, sticky='nsew')

# Function to show a specific frame
def show_frame(frame):
    frame.tkraise()

# Main page
btn_visualizations = tk.Button(frame_main, text="See Visualizations", command=lambda: show_frame(frame_visualizations))
btn_data = tk.Button(frame_main, text="See Data", command=lambda: show_frame(frame_data))
btn_visualizations.pack(pady=20)
btn_data.pack(pady=20)

# Visualization page
# Create a 3x3 grid layout for visualizations
for row in range(3):
    for col in range(3):
        sub_frame = tk.Frame(frame_visualizations, width=400, height=267, bg='lightgrey')
        sub_frame.grid(row=row, column=col, padx=5, pady=5, sticky='nsew')
        frame_visualizations.grid_rowconfigure(row, weight=1)
        frame_visualizations.grid_columnconfigure(col, weight=1)

# Function to display each plot in the Tkinter frame
def add_plot_to_frame(fig, frame):
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

# Create visualizations
# Visualization 1
fig1 = plt.figure(figsize=(6, 4))
sns.countplot(data=data, x='Department', hue='Department', palette='Set1', ax=fig1.add_subplot(111))
fig1.suptitle('Number of Employees per Department')
fig1.subplots_adjust(top=0.85)
add_plot_to_frame(fig1, frame_visualizations.grid_slaves(row=0, column=0)[0])

# Visualization 2
fig2 = plt.figure(figsize=(6, 4))
sns.histplot(data['Salary'], bins=5, kde=True, color="Green", ax=fig2.add_subplot(111))
fig2.suptitle('Salary Distribution')
fig2.subplots_adjust(top=0.85)
add_plot_to_frame(fig2, frame_visualizations.grid_slaves(row=0, column=1)[0])

# Visualization 3
fig3 = plt.figure(figsize=(6, 4))
sns.scatterplot(data=data, x='Salary', y='Performance Rating', hue='Department', palette='Set1', ax=fig3.add_subplot(111))
fig3.suptitle('Salary vs. Performance Rating')
fig3.subplots_adjust(top=0.85)
add_plot_to_frame(fig3, frame_visualizations.grid_slaves(row=0, column=2)[0])

# Visualization 4
fig4 = plt.figure(figsize=(6, 4))
gender_counts = data['Gender'].value_counts()
ax4 = fig4.add_subplot(111)
ax4.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', colors=['#ff9999','#66b3ff','#000000'])
fig4.suptitle('Gender Distribution')
fig4.subplots_adjust(top=0.85)
add_plot_to_frame(fig4, frame_visualizations.grid_slaves(row=1, column=0)[0])

# Visualization 5
fig5 = plt.figure(figsize=(6, 4))
sns.boxplot(data=data, x='Department', y='Salary', palette='Set2', ax=fig5.add_subplot(111))
fig5.suptitle('Salary Distribution by Department')
fig5.subplots_adjust(top=0.85)
add_plot_to_frame(fig5, frame_visualizations.grid_slaves(row=1, column=1)[0])

# Visualization 6
fig6 = plt.figure(figsize=(6, 4))
sns.barplot(data=data, x='Gender', y='Salary', palette='Set1', ax=fig6.add_subplot(111))
fig6.suptitle('Average Salary by Gender')
fig6.subplots_adjust(top=0.85)
add_plot_to_frame(fig6, frame_visualizations.grid_slaves(row=1, column=2)[0])

# Visualization 7
fig7 = plt.figure(figsize=(6, 4))
sns.violinplot(data=data, x='Gender', y='Salary', palette='Set1', ax=fig7.add_subplot(111))
fig7.suptitle('Salary Distribution by Gender')
fig7.subplots_adjust(top=0.85)
add_plot_to_frame(fig7, frame_visualizations.grid_slaves(row=2, column=0)[0])

# Visualization 8
fig8 = plt.figure(figsize=(6, 4))
g = sns.FacetGrid(data, col='Department', height=4, col_wrap=4)
g.map(sns.histplot, 'Salary', kde=True, color='blue')
fig8.suptitle('Facet Grid Comparing Multiple Distributions')
fig8.subplots_adjust(top=0.85)
add_plot_to_frame(fig8, frame_visualizations.grid_slaves(row=2, column=1)[0])

# Visualization 9
fig9 = plt.figure(figsize=(6, 4))
sns.stripplot(data=data, x='Department', y='Salary', jitter=True, palette='Set2', dodge=True, ax=fig9.add_subplot(111))
fig9.suptitle('Salary Distribution by Department (Strip Plot)')
fig9.subplots_adjust(top=0.85)
add_plot_to_frame(fig9, frame_visualizations.grid_slaves(row=2, column=2)[0])

# Data page
# Create a frame for the treeview and scrollbars
frame_tree = tk.Frame(frame_data)
frame_tree.pack(fill=tk.BOTH, expand=True)

# Create a vertical scrollbar
vsb = ttk.Scrollbar(frame_tree, orient="vertical")
vsb.pack(side="right", fill="y")

# Create a horizontal scrollbar
hsb = ttk.Scrollbar(frame_tree, orient="horizontal")
hsb.pack(side="bottom", fill="x")

# Create a treeview widget (a table)
tree = ttk.Treeview(frame_tree, columns=list(data.columns), show="headings", yscrollcommand=vsb.set, xscrollcommand=hsb.set)

# Configure scrollbars
vsb.config(command=tree.yview)
hsb.config(command=tree.xview)

# Add column headings
for col in data.columns:
    tree.heading(col, text=col)
    tree.column(col, width=100)

# Insert rows into the treeview widget
for _, row in data.iterrows():
    tree.insert("", "end", values=list(row))

# Function to save data to Excel
def save_to_excel():
    path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=(("Excel file", "*.xlsx"), ("All files", "*.*")))
    if path:
        rows = []
        for item in tree.get_children():
            row = tree.item(item)["values"]
            rows.append(row)
        df = pd.DataFrame(rows, columns=data.columns)

        try:
            df.to_excel(path, index=False, engine='openpyxl')
            print(f"Data successfully saved to {path}")
        except Exception as e:
            print(f"Error saving file: {e}")

# Add a button to save the data to an Excel file
save_button = tk.Button(frame_data, text="Save Data to EXCEL", command=save_to_excel)
save_button.pack(side=tk.BOTTOM, pady=10)

# Pack the treeview widget
tree.pack(fill=tk.BOTH, expand=True)

# Show the main page initially
show_frame(frame_main)

# Run the application
root.mainloop()

