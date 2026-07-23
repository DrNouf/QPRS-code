
import pandas as pd
import numpy as np
import random

def generate_dataset(n_records=300000):
    locations = ["NY","CA","TX","FL","WA","IL"]
    departments = ["IT","Finance","HR","Sales","Marketing"]

    data = {
        "user_id": range(n_records),
        "age": np.random.randint(18,65,n_records),
        "location": [random.choice(locations) for _ in range(n_records)],
        "salary": np.random.randint(30000,120000,n_records),
        "department": [random.choice(departments) for _ in range(n_records)],
        "activity_score": np.random.uniform(0,100,n_records)
    }

    df = pd.DataFrame(data)
    return df
