import pandas as pd
from faker import Faker
import random
import gspread
from gspread_dataframe import get_as_dataframe,set_with_dataframe


def generate_data():

    # Initialize Faker
    fake = Faker()

    # Create an empty list to store data
    data = []

    # Generate up to 200 records
    for _ in range(100):
        record = {
            'diamond_id': fake.random_int(min=100000000, max=999999999),
            'size': round(random.uniform(0.09, 19.35), 2),
            'color': random.choice(["E", "F", "L", "D", "J", "I", "G", "H", "M", "K"]),
            'fancy_color_dominant_color': random.choice(["Orange", "Brown", "Yellow", "Pink", "Black", "Other", "Gray", "Purple", "Blue", "Green", "Chameleon", "Red"]),
            'fancy_color_secondary_color': random.choice(["Orange", "Brown", "Yellow", "Pink", "Black", "Other", "Gray", "Purple", "Blue", "Green", "Chameleon", "Red"]),
            'fancy_color_overtone': random.choice(["Yellowish", "Brownish", "Pinkish", "Greenish", "Orangey", "Purplish", "Grayish"]),
            'fancy_color_intensity': random.choice(["Fancy", "Very Light", "Faint", "Fancy Light", "Light", "Fancy Deep", "Fancy Intense", "Fancy Dark", "Fancy Vivid"]),
            'clarity': random.choice(["VVS2", "VVS1", "I1", "VS1", "VS2", "IF", "SI2", "I2", "SI1", "SI3", "I3"]),
            'cut': random.choice(["Very Good", "Excellent", "Good", "Fair", "Poor"]),
            'symmetry': random.choice(["Very Good", "Excellent", "Good", "Fair", "Poor"]),
            'polish': random.choice(["Very Good", "Excellent", "Good", "Fair", "Poor"]),
            'depth_percent': round(random.uniform(0, 99) * 0.1, 1),
            'table_percent': round(random.uniform(0, 94) * 0.1, 1),
            'meas_length': round(random.uniform(2.85, 17.06), 2),
            'meas_width': round(random.uniform(2.85, 17.06), 2),
            'meas_depth': round(random.uniform(2.85, 17.06), 2),
            'girdle_min': random.choice(["M", "STK", "TN", "TK", "VTN", "VTK", "XTK", "XTN", "STN"]),
            'girdle_max': random.choice(["M", "STK", "TN", "TK", "VTN", "VTK", "XTK", "XTN", "STN"]),
            'culet_size': random.choice(["N", "S", "M", "VS", "L", "EL", "SL", "VL"]),
            'culet_condition': random.choice(["Blue", "Yellow", "Green", "White", "Orange"]),
            'fluor_color': random.choice(["Blue", "Yellow", "Green", "White", "Orange"]),
            'fluor_intensity': random.choice(["Very Slight", "Strong", "Medium", "Faint", "Very Strong", "Slight"]),
            'lab': random.choice(["IGI", "GIA", "HRD"]),
            'total_sales_price': fake.random_int(min=200, max=1449881),
            'eye_clean': random.choice(["Yes", "E1", "Borderline", "No"]),
            'date': fake.date_between(start_date="-20y", end_date="today").strftime("%Y-%m-%d")
        }
        data.append(record)


    # Create a DataFrame from the list of dictionaries
    df = pd.DataFrame(data)

    # Display the DataFrame
    return df



def write_df():
    GSHEET_NAME = 'DiamondsData'
    TAB_NAME = 'Sheet1'
    df = generate_data()
    gc = gspread.service_account(filename = "diamond-analysis-ac6758ca1ace.json")
    sh = gc.open(GSHEET_NAME)
    worksheet = sh.worksheet(TAB_NAME)
    set_with_dataframe(worksheet,df)

write_df()
print("Load Success !!")