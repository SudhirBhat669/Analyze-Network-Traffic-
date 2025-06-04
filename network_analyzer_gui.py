import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import IsolationForest
from PIL import ImageGrab
import random

# Simulate PCAP data
def simulate_data():
    protocols = ['HTTP', 'DNS', 'TCP', 'HTTPS', 'ICMP']
    data = {
        'Protocol': [random.choice(protocols) for _ in range(200)],
        'Packet Size': [random.randint(60, 1500) for _ in range(200)],
        'Src Port': [random.randint(1000, 65000) for _ in range(200)],
        'Dst Port': [random.randint(20, 443) for _ in range(200)],
    }
    return pd.DataFrame(data)

# Apply Isolation Forest to detect anomalies
def apply_ml(df):
    model = IsolationForest(contamination=0.1, random_state=42)
    df['Anomaly'] = model.fit_predict(df[['Packet Size', 'Src Port', 'Dst Port']])
    return df

# GUI Functionality
def analyze_data():
    df = simulate_data()
    df = apply_ml(df)

    # Visualization
    plt.figure(figsize=(8, 5))
    sns.countplot(data=df, x='Protocol', palette='Set2')
    plt.title("Protocol Distribution")
    plt.savefig("protocol_distribution_graph.png")
    plt.close()

    # Anomaly summary
    anomalies = df[df['Anomaly'] == -1]
    anomaly_summary = f"Total Packets: {len(df)}\nAnomalies Detected: {len(anomalies)}"
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, anomaly_summary)

    # Table
    for i in tree.get_children():
        tree.delete(i)
    for _, row in df.iterrows():
        tree.insert('', tk.END, values=(row['Protocol'], row['Packet Size'], row['Src Port'], row['Dst Port'], 'Anomaly' if row['Anomaly'] == -1 else 'Normal'))

def capture_screenshot():
    x = root.winfo_rootx()
    y = root.winfo_rooty()
    w = x + root.winfo_width()
    h = y + root.winfo_height()
    ImageGrab.grab().crop((x, y, w, h)).save("gui_dashboard_screenshot.png")
    messagebox.showinfo("Screenshot", "Dashboard screenshot saved as gui_dashboard_screenshot.png")

# Main GUI
root = tk.Tk()
root.title("Wireshark Network Analyzer")
root.geometry("900x600")

tk.Label(root, text="Network Traffic Analyzer", font=("Arial", 18)).pack(pady=10)

frame_buttons = tk.Frame(root)
frame_buttons.pack()

ttk.Button(frame_buttons, text="Analyze Traffic", command=analyze_data).pack(side=tk.LEFT, padx=10)
ttk.Button(frame_buttons, text="Capture Screenshot", command=capture_screenshot).pack(side=tk.LEFT, padx=10)

output_text = tk.Text(root, height=4, width=80)
output_text.pack(pady=10)

columns = ("Protocol", "Size", "Src Port", "Dst Port", "Status")
tree = ttk.Treeview(root, columns=columns, show='headings')
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=100)
tree.pack(expand=True, fill='both', padx=10, pady=10)

root.mainloop()

