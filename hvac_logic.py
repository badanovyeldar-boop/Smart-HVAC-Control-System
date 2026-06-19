import pandas as pd

data = pd.read_csv("sample_data.csv")

def determine_status(current, target):
    if current > target:
        return "Cooling Needed"
    elif current < target:
        return "Heating Needed"
    else:
        return "Comfortable"

data["Status"] = data.apply(
    lambda row: determine_status(
        row["CurrentTemp"],
        row["TargetTemp"]
    ),
    axis=1
)

print(data)
