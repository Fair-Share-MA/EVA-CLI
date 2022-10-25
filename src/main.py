import pandas as pd, magic, os, json, csv, jellyfish

df = []
df_merge = None
mime_types = json.load(open('mime_types.json'))

def load_excel(file):
    df.append(pd.read_excel(file))

def load_csv(file):
    sniffer = csv.Sniffer()
    with open(file) as f:
        dialect = sniffer.sniff(f.readline(), mime_types["delemiters"])
        f.seek(0)
        df.append(pd.read_csv(file, delimiter=dialect.delimiter))

def find_jaro_similarity(target, df):
    max = 0
    name = None
    for column in df.columns:
        jaro = jellyfish.jaro_similarity(target, column)
        if (not name):
            name = column
            max = jaro
        elif (jaro > max):
            name = column
            max = jaro
    
    if max < 0.75: name = None
    return name

def override_jaro_similarity(target, df):
    if (target in df.columns):
        return target

    for alias in mime_types.comparision_overrides[target]:
        if (alias in df.columns):
            return alias
    
    return None

def find_closest_df_col(target, df):
    name = None

    if (mime_types.comparision_overrides.has_key(target)):
        name = override_jaro_similarity(target, df)
    
    if (not name):
        name = find_jaro_similarity(target, df)
        
    return name

# NOTE: prioritises column names for df1
def merge_df(df1, df2):
    temp = pd.DataFrame()
    for col in df1:
        closest_df2_col = find_closest_df_col(col, df2)
        if (closest_df2_col):
            temp[col] = df1[col].tolist() + df2[closest_df2_col].tolist()
        else:
            temp[col] = df1[col].tolist()

    return temp

print("Importing files from INPUT folder...")

input_dir = '../input'
output_dir = '../output'
for filename in os.listdir(input_dir):
    file = os.path.join(input_dir, filename)
    file_mime = magic.from_file(file, mime=True)
    
    load_excel(file) if file_mime == mime_types["excel"] else load_csv(file)

print("Files loaded. Merging...\nThis might take a while")

# initiate the merge
current_merge = 1
if (not df_merge):
    if (len(df) < 2):
        print("ERROR: There must be more than 1 frame to merge")
    else:
        df_merge = merge_df(df[0], df[1])

while current_merge < len(df):
    df_merge = merge_df(df_merge, df[current_merge])
    current_merge += 1

print("Merging complete. Exporting...")

df_merge.to_csv('../output/export.csv')

print("Export complete! Goodbye :)")