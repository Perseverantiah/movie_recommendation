import streamlit as st
from streamlit_ace import st_ace
from streamlit_option_menu import option_menu
import difflib 
import streamlit as st
from streamlit_tags import st_tags
import pandas as pd
import pickle
from PIL import Image
from st_aggrid import AgGrid

loaded_similarity=pickle.load(open('similarity_model.sav','rb'))
data=pd.read_csv("movies.csv")

def main():

    # 1. as sidebar menu
    with st.sidebar:
        selected = option_menu("Menu", ["Home","Desc","Test","About"], 
            icons=['house', 'brightness-high','box-fill','capsule'], menu_icon="justify", default_index=1,
                              
            styles={
                "icon": {"color": "#D0E92B", "font-size": "15px"}, 
                "nav-link": {"font-size": "15px", "text-align": "left", "margin":"0px", "--hover-color": "#eeee" }
                  }               
                              )
    
    
    if selected == "About":
        col1, col2 = st.columns( [0.8, 0.2])
        with col1:               # To display the header text using css style
            st.markdown(""" <style> .font {
            font-size:35px ; font-family: 'Cooper Black'; color: #FF9633;} 
            </style> """, unsafe_allow_html=True)
            st.markdown('<p class="font">About Ninette</p>', unsafe_allow_html=True) 
            
            st.markdown(
            """
            Je m'appelle Ninette et je suis une boule d'energie ✨.Je suis ingenieure en Genie Mathematique et Modelisation Option Informatique et Recherche Operationnelle.J'ai suivi en parallele en Data science.So, je suppose que tu t'imagines deja le genre de profil que j'ai et le genre de choses auxquelles je m'interesse.Je suis une passionnee d'IA et si tu lis ceci c'est probablement sur une app via laquelle j'ai deploye un modele. Allez, bonne visite monsieur le curieux.
            
            **👈 Tu peux tester ici le projet ** , fais toi plaisir! 
            ### Want to learn more?
            - Check out [streamlit.io](https://streamlit.io)
            - Jump into our [documentation](https://docs.streamlit.io)
            - Ask a question in our [community
                forums](https://discuss.streamlit.io)
            ### See more complex demos
            - Use a neural net to [analyze the Udacity Self-driving Car Image
                Dataset](https://github.com/streamlit/demo-self-driving)
            - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
        """
        )
            
        with col2:  
            image = Image.open('nino.jpeg')
            st.image(image, width=150)

            st.write("Please visit My Data Talk's Medium blog at: https://medium.com/@insightsbees")    
        #st.image(profile, width=700 )
        
    elif selected=="Test":
        keywords = st_tags(
        label='# Enter Movie name or keyword: ',
        text='You should just select or enter the keywords that describe your movie. Press enter to add more',
        value=['Avatar'],
        suggestions=['Avengers', 'Batman','Superman', 'Man', 'Amazing', 
                     'Caribbea', 'Hobbit', 'Legacy', 
                     'WALL', 'Rush', 'Dinosaur'],
        maxtags = 1,
        key='1')
        
        if len(keywords) ==0 :
            st.write("Please select or write the movie name")
        else :
            #st.write(keywords[0])
            movie_name = keywords[0]

            list_of_all_titles = data['title'].tolist()

            find_close_match = difflib.get_close_matches(movie_name, list_of_all_titles)

            close_match = find_close_match[0]

            #print(close_match)

            index_of_the_movie = data[data.title == close_match]['index'].values[0]

            loaded_similarity_score = list(enumerate(loaded_similarity[index_of_the_movie]))

            sorted_similar_movies = sorted(loaded_similarity_score, key = lambda x:x[1], reverse = True) 

            st.markdown(""" ### Movies suggested for you : """)

            i = 1

            for movie in sorted_similar_movies:
                index = movie[0]
                title_from_index = data[data.index==index]['title'].values[0]
                #print(data[data.index==index]['director'].values[0])

                if (i<30):
                    st.write(i, '.',title_from_index)
                    i+=1

                    

    elif selected=="Desc":
        st.markdown(""" <style> .font {
            font-size:35px ; font-family: 'Cooper Black'; color: #FF9633;} 
            </style> """, unsafe_allow_html=True)
        st.markdown('<p class="font">Description of movie recommendation System</p>', unsafe_allow_html=True)
        st.markdown(
            """
            Si vous utilisez YouTube, Facebook, Amazon... vous vous etes peut-etre deja demande comment tel produit vous est recommande.
            ### Il existe trois types de systemes de recommandations :
            - Les systemes de recommandations bases sur le contenu (qui est d'ailleurs celui implemente ici)
            - Les systemes de recommandations collaboratifs
            - Les systemes de recommandation hybrides
            """)
        
        st.markdown("""
        ### Les systemes de recommandations bases sur le contenu
        
        Les méthodes basées sur le contenu sont basées sur la similarité des attributs de film. En utilisant ce type de système de recommandation, si un utilisateur regarde un film, des films similaires sont recommandés. Par exemple, si un utilisateur regarde une comédie mettant en vedette Adam Sandler, le système lui recommandera des films du même genre ou mettant en vedette le même acteur, ou les deux. Dans cet esprit, l'entrée pour la construction d'un système de recommandation basé sur le contenu est les attributs de film.""")
        contenu = Image.open('contenu.jpg')
        st.image(contenu)
        st.markdown("""
        
        ### Les systemes de recommandations collaboratifs
        
        Les systèmes basés sur le filtrage collaboratif produisent des recommandations en calculant la similarité entre les préférences d’un utilisateur et celles d’autres utilisateurs. En fait, les utilisateurs sont classes par groupes suivants leurs choix sur la plateforme et beaucoup d'autres parametres. On vous propose donc des articles en se basant sur des choses que des gens classes dans la meme categorie que vous ont achete ou aime. De tels systèmes ne tentent pas d’analyser ou de comprendre le contenu des éléments à recommander. 
        """)
        
        cola = Image.open('collaboratif.png')
        st.image(cola)
        st.markdown("""
        ### Les systemes de recommandation hybrides
        Un système de recommandation hybride utilise des composants de différents types d’approches de recommandation ou s’appuie sur leur logique. Par exemple, un tel système peut utiliser à la fois des connaissances extérieures et les caractéristiques des éléments, combinant ainsi des approches collaboratives et basées sur le contenu .
        """)
        
        hybride = Image.open('hybride.jpg')
        st.image(hybride)
        
        
    elif selected=="Home":
        st.markdown(""" <style> .font {
            font-size:35px ; font-family: 'Cooper Black'; color: #FF9633;} 
            </style> """, unsafe_allow_html=True)
        st.markdown('<p class="font"> Movie recommendation System</p>', unsafe_allow_html=True)
        
        st.markdown("""
        Au cours de ce projet, nous vous proposons des films en nous basant sur la similarite des attributs de film. Vous pouvez soit entrer le nom d'un film, le nom d'un acteur,le directeur de production, ou un mot cle tout simplement. Et sur cette base, nous vous proposons de nouveau film que vous pourrez aimer. Vous pouvez tester le systeme soit sur la page Test ou juste en bas en scrollant celle-ci. Pour les plus curieux, je vous presente les donnees que j'ai utilisee et auxquelles vous pourrez avoir acces sur ce depot [GitHub](https://github.com/streamlit/demo-self-driving).
        
         """)
        AgGrid(data,height=400)

    
    
if __name__=='__main__':
    main()
    