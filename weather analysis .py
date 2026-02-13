import pandas as pd

# Excel file read
df = pd.read_excel("weather Metostat .xlsx")
import pandas as pd
# Ensure 'Date' column is in datetime format
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# Ask user for input date
user_input = input("Enter date (e.g. 1/15/2026): ")
try:
    user_date = pd.to_datetime(user_input, errors='raise')
except:
    print("Invalid date format! Please enter like mm/dd/yyyy")
    exit()

# Filter the row with that date
weather_row = df[df['Date'] == user_date]

if not weather_row.empty:
    tavg = weather_row['tavg'].values[0]
    tmin = weather_row['tmin'].values[0]
    tmax = weather_row['tmax'].values[0]
    prcp = weather_row['prcp'].values[0]

    print(f"\nWeather for {user_date.strftime('%B %d, %Y')}:")
    print(f"Average Temperature: {tavg}")
    print(f"Minimum Temperature: {tmin}")
    print(f"Maximum Temperature: {tmax}")
    print(f"Rainfall: {prcp}")
else:
    print("Date not found in the data!")



