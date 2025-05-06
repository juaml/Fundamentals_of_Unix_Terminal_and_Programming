# experiment_1.py
import pandas as pd
import sys
from pathlib import Path
# Goes up from 'experiments' to 'code'
sys.path.append(str(Path(__file__).parent.parent))  

# From the code folder, we can access the lib folder
from lib.processing import process_data

# Relative path to the project folder (where we have the data)
project_folder = Path(__file__).parent.parent.parent
# From the project folder, we can access the data folder
data_dir = project_folder / "data/"
data1 = pd.read_csv(data_dir / "data1.csv")
data2 = pd.read_csv(data_dir / "data2.csv")

data1 = process_data(data1, "old_name", "new_name")
data2 = process_data(data2, "old_name", "new_name")


# %%
# experiment_1.py
import pandas as pd

# Absolute path to the project folder
project_folder = (
    "/home/nnieto/Nico/Cursos/"
    "FZJ - Seminars/Fundamentals_of_Unix_Terminal_and_Programming/"
    "4 - Research oriented coding/project_folder/"
)

# From the project folder, we can access the data folder
data_dir = project_folder + "data/"
data1 = pd.read_csv(data_dir + "data1.csv")
data2 = pd.read_csv(data_dir + "data2.csv")


data1 = data1.dropna()
data1 = data1.drop_duplicates()
data1 = data1.reset_index(drop=True)
data1 = data1.rename(columns={"old_name": "new_name"})

data2 = data2.dropna()
data2 = data2.drop_duplicates()
data2 = data2.reset_index(drop=True)
data2 = data2.rename(columns={"old_name": "new_name"})

# %%


# %%
# experiment_1.py
import pandas as pd
from pathlib import Path

# Relative path to the project folder (where we have the data)
project_folder = Path(__file__).parent.parent.parent
# From the project folder, we can access the data folder
data_dir = project_folder / "data/"
data1 = pd.read_csv(data_dir / "data1.csv")
data2 = pd.read_csv(data_dir / "data2.csv")

data1 = process_data(data1, "old_name", "new_name")
data2 = process_data(data2, "old_name", "new_name")
# %%
