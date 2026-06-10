import pandas as pd

# Load dataset
url = "https://raw.githubusercontent.com/4GeeksAcademy/NLP-project-tutorial/main/url_spam.csv"

df = pd.read_csv(url)

print(df.head())
print(df.info())
print(df["is_spam"].value_counts())
