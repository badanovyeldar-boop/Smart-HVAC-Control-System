import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("sample_data.csv")

plt.figure(figsize=(8, 5))
plt.bar(data["Room"], data["CurrentTemp"])

plt.title("Room Temperature Monitoring")
plt.xlabel("Room")
plt.ylabel("Temperature (°F)")
plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig("temperature_chart.png")
plt.show()
