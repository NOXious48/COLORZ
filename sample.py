import pandas as pd

df = pd.read_parquet('category_attributes.parquet')
#print(df)
attribute_list = df['Attribute_list']
for i in range(len(attribute_list)):
  print(attribute_list[i])

train_data=pd.read_csv("train.csv")
print(train_data.head(20))
#print(len(train_data))  70213

category_dfs = {category: train_data[train_data['Category'] == category] for category in train_data['Category'].unique()}
#print(category_dfs)

#making dataframes according to categories
men_tshirt_df = category_dfs['Men Tshirts']
saree_df=category_dfs['Sarees']
kurtis_df=category_dfs['Kurtis']
women_tshirts_df=category_dfs['Women Tshirts']
women_dresses_df=category_dfs['Women Tops & Tunics']

"""print(men_tshirt_df.head(20))
print(saree_df.head(20))
print(kurtis_df.head(20))
print(women_tshirts_df.head(20))
print(women_dresses_df.head(20))"""

#Filtering out empty attributes
def filtering_column(df):
    empty_cols = [col for col in df.columns if df[col].isnull().all()]
    df = df.drop(columns=empty_cols)
    df = df.drop(columns=["len"])     # len is number of attributes the data have
    return df

df_dict = {
    'men_tshirt_df': men_tshirt_df,
    'saree_df': saree_df,
    'kurtis_df': kurtis_df,
    'women_tshirts_df': women_tshirts_df,
    'women_dresses_df': women_dresses_df
}

for df_name, df in df_dict.items():
    df_dict[df_name] = filtering_column(df)  # Update the dictionary with the filtered DataFrame
    #print(df_dict[df_name])  # Print the updated DataFrame
#Filtering out empty attributes
def filtering_column(df):
    empty_cols = [col for col in df.columns if df[col].isnull().all()]
    df = df.drop(columns=empty_cols)
    df = df.drop(columns=["len"])     # len is number of attributes the data have
    return df

df_dict = {
    'men_tshirt_df': men_tshirt_df,
    'saree_df': saree_df,
    'kurtis_df': kurtis_df,
    'women_tshirts_df': women_tshirts_df,
    'women_dresses_df': women_dresses_df
}

for df_name, df in df_dict.items():
    df_dict[df_name] = filtering_column(df)  # Update the dictionary with the filtered DataFrame
    #print(df_dict[df_name])  # Print the updated DataFrame

# Access the updated DataFrames using their original names
men_tshirt_df = df_dict['men_tshirt_df']  #['color' 'neck' 'pattern' 'print_or_pattern_type' 'sleeve_length']
print(men_tshirt_df)
saree_df = df_dict['saree_df']      #['blouse_pattern' 'border' 'border_width' 'color' 'occasion' 'ornamentation' 'pallu_details' 'pattern' 'print_or_pattern_type' 'transparency']
print(saree_df)
kurtis_df=df_dict['kurtis_df']      #['color' 'fit_shape' 'length' 'occasion' 'ornamentation' 'pattern' 'print_or_pattern_type' 'sleeve_length' 'sleeve_styling']
women_tshirts_df=df_dict['women_tshirts_df']    #['color' 'fit_shape' 'length' 'pattern' 'print_or_pattern_type' 'sleeve_length' 'sleeve_styling' 'surface_styling']
women_dresses_df=df_dict['women_dresses_df']    #['color' 'fit_shape' 'length' 'neck_collar' 'ocassion' 'pattern' 'print_or_pattern_type' 'sleeve_length' 'sleeve_styling' 'surface_styling']

for df in df_dict.values():
  print(df.info())
  print("\n")