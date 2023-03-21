import streamlit as st
#import base64
from PIL import Image

#################################################
#  Initialize objects, variables and functions  #
#################################################  

@st.cache_data
def show_image(path):
    ''' Places image centered
    

    Parameters
    ----------
    path (string): path to image file

    Returns
    -------
    None.

    '''
    col1, col2, col3, col4, col5 = st.columns(5)
    with col3:
        image = Image.open(path)
        st.image(image)
    
    
###############
#   Layout    #
###############

# Page title
st.title(':blue[People in STEM in news reporting in Spanish written press]')

# There are 2 tabs: Home and Methodology
tab1, tab2 = st.tabs(['Gender Bias', 'Methodology'])
with tab1:
    show_image('img/distribution_article_mentions_genre.png') 
    st.write('This webapp showcases a **recommender system** built from records \
            of user interactions with content items at \
            [IBM Watson Studio](https://www.ibm.com/cloud/watson-studio).')      
    show_image('img/distribution_people_mentions_genre.png')
    st.write('The list of recommendations is **updated dynamically** according \
             to user activity. To interact with the engine and see its results, \
             click on the *Recommender* tab above and simulate user activity on the \
             platform by picking articles to read. You can obtain \
             personalized recommendations for you or other users!')
    show_image('img/unique_mentions_genre_stats.png')
    show_image('img/people_per_article_genre.png')


with tab2:
    st.write('For more information, visit the [GitHub repository](https://github.com/jviosca/Media-portrayal-of-People-in-STEM-in-Spanish-written-press).')  
    st.write('Author: [Jose Viosca Ros](https://jvros.com.es/index.php/es/inicio/)')           
