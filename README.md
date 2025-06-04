# Analyze-Network-Traffic
# Capture and Analyze Network Traffic Using Wireshark (with Python & ML)
![Image](https://github.com/user-attachments/assets/fdd341d3-2718-4f08-8b00-eb3509f9f06b)
![Image](https://github.com/user-attachments/assets/cbcb0b43-ab98-4902-9fdd-ac092c104c49)

## 🎯 Objective
Capture live network packets and identify basic protocols and traffic types using Wireshark, analyze the packets with a Python GUI tool, and apply machine learning to classify or cluster the traffic.

## 🧰 Tools & Technologies
Python 3.x
Tkinter (for GUI)
Scapy (for packet capture)
Pandas, NumPy (for analysis)
Matplotlib, Seaborn (for visualization)
Scikit-learn (for machine learning)
Tshark or Pyshark (Wireshark API for parsing)
PIL (for screenshot)
Wireshark (for manual traffic generation and .pcap export)

## 📦 Outcome
Capture packets from the live network
Filter by protocol (HTTP, DNS, TCP)
Visualize traffic stats using graphs
Apply ML model (Isolation Forest) to flag anomalies
Export screenshots
GUI dashboard for ease of use

## 🔍 How It Was Done (Summary)
1. Used Pyshark to read .pcap files or capture live packets.
2. Extracted protocol information, IPs, ports, etc.
3. Converted packet metadata into a structured DataFrame.
4. Visualized using bar plots and protocol distribution.
5. Applied IsolationForest to detect anomalies or rare traffic.
6. Displayed results in a Tkinter-based GUI.
7. Captured GUI screenshot for reports.
8. Exported graph images and filtered summaries.

## 🧠 Key Concepts
Packet Capture using Wireshark & Python
TCP/IP Protocol Layers
Protocol Filtering and Statistics
GUI Development using Tkinter
ML-based Traffic Anomaly Detection
Data Visualization

## ❓ Interview Questions & Answers
1. What is Wireshark and what does it do?
2. How can Python be used with Wireshark?
3. What is a .pcap file?
4. What protocols are typically found in web traffic?
5. What is Isolation Forest?
6. What is the role of DNS in traffic?
7. How does TCP work in packet communication?
8. How do you apply filters in Wireshark?
9. What are the benefits of visualizing network traffic?

## 🚀 Future Considerations
Real-time anomaly alerts via email
Exporting analytics to PDF/HTML
Support for multi-interface capture
Integrate geolocation/IP reputation APIs
Compare historical captures for change detection
