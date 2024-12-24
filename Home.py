import streamlit as st # importing module to required to build webpage
import pandas as pd # importing module to read databases


st.set_page_config(layout="wide") # Setting the webpage width


col1, col2 =st.columns(2) # creating 2 columns for containing data

col1.image("images/photo.png") # Providing data to the column 1

# providing data to the column 2
with col2:
    st.title("Ardit Sulces")
    st.info("""Git is easy to learn and has a 
    tiny footprint with lightning fast performance. 
    It outclasses SCM tools like Subversion,
     CVS, Perforce, and ClearCase. Git is easy to learn 
     and has a tiny footprint with lightning fast performance. 
     It outclasses SCM tools like Subversion, CVS, Perforce, and ClearCase""")

# writing a simple text on the webpage
st.write("Please feel free to contact me through email.")

col5, tile_column,  col6= st.columns(3)

tile_column.title("List of apps")

# Reading the data(.csv) file
df = pd.read_csv("data.csv", sep=";")
print(df)


col3,empty_col, col4 = st.columns([2, 0.5, 2]) # creating 2 columns for containing data

# providing data to the column 3
with col3:
    for index, row in df[0:10].iterrows():      # iterating through each row from a range of rows [0:10].
        st.header(row["title"])                  # getting the cell vale under each column for a specific row
        st.write(row["description"])
        st.image(f'images/{row["image"]}')
        st.write(f'[Source code](row["url"])')

# providing data to the column 4
with col4:
    for index, row in df[10:].iterrows():       # iterating through each row from a range of rows [0:10].
        st.header(row["title"])                  # getting the cell vale under each column for a specific row
        st.write(row["description"])
        st.image(f'images/{row["image"]}')
        st.write(f'[Source code](row["url"])')