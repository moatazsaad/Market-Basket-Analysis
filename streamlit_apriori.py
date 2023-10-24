
import streamlit as st
import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules
import openpyxl
# Load the association rules data
df = pd.read_excel('Online Retail.xlsx')
df['Description'] = df['Description'].str.strip()

country = st.selectbox("Select a country", df['Country'].unique())

# Transaction for the selected country
Basket_Country = (df[df['Country'] == country]
                  .groupby(['InvoiceNo', 'Description'])['Quantity']
                  .sum().unstack().reset_index().fillna(0)
                  .set_index('InvoiceNo'))

def hot_encoder(x):
    if x <= 0:
        return 0
    if x >= 1:
        return 1

Basket_Encoded = Basket_Country.applymap(hot_encoder)
Basket_Country = Basket_Encoded

# Applying apriori algorithm for the selected country
freq_items = apriori(Basket_Country, min_support=0.01, use_colnames=True)

# Applying association rule
rules = association_rules(freq_items, metric="lift", min_threshold=1)
rules = rules.sort_values(['confidence', 'lift'], ascending=[False, False])

# Create a Streamlit app
def main():
    st.title("Top Association Rules for {}".format(country))
  
    # Display the products to promote
    st.subheader("Products to Promote")
    promote_products = rules[rules['antecedents'].apply(lambda x: len(x) == 1)]
    promote_products = promote_products.rename(columns={'antecedents': 'products'})
    if 'products' in promote_products.columns:
        st.dataframe(promote_products['products'])
    else:
        st.write("No 'products' column found in promote_products DataFrame.")

    # Display the cross-selling opportunities
    st.subheader("Cross-Selling Opportunities")
    cross_sell_products = rules[rules['antecedents'].apply(lambda x: len(x) > 1)]
    cross_sell_products = cross_sell_products.rename(columns={'antecedents': 'products'})
    if 'products' in cross_sell_products.columns:
        pd.set_option('display.max_colwidth', None)
        st.dataframe(cross_sell_products['products'])    
    else:
        st.write("No 'products' column found in cross_sell_products DataFrame.")

if __name__ == "__main__":
    main()
