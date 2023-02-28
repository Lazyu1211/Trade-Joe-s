import pandas as pd

PATH = "/Users/junyuwu/trade_joes/components/store_info.csv"

def get_list():
    df = pd.read_csv(PATH)
    state_count = df["state"].value_counts()[:10].to_frame()
    state_count = state_count.rename(columns={"state":"store_count"}).reset_index().rename(columns={"index":"state"})
    four_people_family_median_income = ["111,535", "117,706", "118,901", "113,649", "148,713", "89,206", "140,657", "93,386", "89,741", "121,793"]
    state_populaiton = ["40,223,504", "20,448,194", "7,999,503", "12,807,072", "7,174,604", "22,359,251", "9,438,124", "30,345,487", "7,379,346", "8,820,504"]
    state_density = ["258", "434", "120", "231", "920", "417", "1283", "116", "65", "223"]
    state_count["median_4_family_income"] = four_people_family_median_income
    state_count["population"] = state_populaiton
    state_count["density"] = state_density
    state_count.reset_index(drop=True,inplace=True)
    liststates =list(set(state_count["state"].tolist()))   
    return liststates

def get_data():
    df = pd.read_csv(PATH)
    state_count = df["state"].value_counts()[:10].to_frame()
    state_count = state_count.rename(columns={"state":"store_count"}).reset_index().rename(columns={"index":"state"})
    four_people_family_median_income = [111535, 117706, 118901, 113649, 148713, 89206, 140657, 93386, 89741, 121793]
    state_populaiton = [40223504, 20448194, 7999503, 12807072, 7174604, 22359251, 9438124, 30345487, 7379346, 8820504]
    state_density = [258, 434, 120, 231, 920, 417, 1283, 116, 65, 223]
    state_count["median_4_family_income"] = four_people_family_median_income
    state_count["population"] = state_populaiton
    state_count["density"] = state_density
    state_count.reset_index(drop = True, inplace=True)
    return state_count

def get_ny():
    df = pd.read_csv(PATH)
    ny_df = df[df["state"]=="NY"]
    ny_city = ny_df["city"].value_counts().to_frame()
    return ny_city

def get_nj():
    df = pd.read_csv(PATH)
    nj_df = df[df["state"]=="NJ"]
    nj_city = nj_df["city"].value_counts().to_frame()
    return nj_city