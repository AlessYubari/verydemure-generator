import streamlit as st # This imports the Streamlit library
import random # This allows us to use random.choice()

# Set the title of your web app
st.title("Compliment Generator")

# List of compliments
compliments = [
    "Ton boule il chamboule!",
    "Ton père c'est pas un voleur? Il a volé toutes les étoiles du ciel pour les mettre dans tes yeux.",
    "Une chance que je suis pas allergique au lactose, parce que tu passe crème.",
    "J'aime me beurrer la biscotte.",
    "Vous êtes dotté d'une sagacité légendaire.",
    "Yo pour toi j'deviendrais vegan.",
    "Vous ne vous reposez jamais vous.",
    "Je t'aime tes mains.",
    "You ust be the square root of 2 because I feel irrational for you.",
    "My doctor told me I'm missing vitamin U. Can you help me?",
    "À l'occasion, je vous mettrai un petit coup de polish...",
    "Comment est votre blanquette?",
    "T'as vu ta gueule? On dirait 30 culs de singes collés sur un bâton.",
    "Il s'agirait de grandir hein, il s'agirait de grandir.",
    "Hey mademoiselle, file moi ton 06 tu ressembles à Bernadette Chirac.",
    "On ne eparle jamais allemand par plaisir.",
    "Vous avez une bonne tête de vainqueur vous.",
    "Et on lui pelera lejonc comme au bailli du Limousin!",
    "Si je ne suis pas de retour dans 5 minutes, attendez plus longtemps.",
    "Alors les bavaroises, ça va? Toujours en tracteur?",
    "T'as une tronche de flanc mec.",
    "Tu es beau comme un camion.",
    "T'es beau comme un coup droit de Roger Federer.",
    "T'es mignon mais t'es un tout petit breton.",
    "Tu puires comme les chausses de Jacquouille, Messire!",
    "T'es beaucoup moins con que t'en as l'air.",
    "You're cute, but not in the attractive way.",
    "You look like you're going to be a hot older woman."
    "Nice chevilles wesh.", 
    ]

# Add a button to generate a compliment
if st.button("Get a compliment"):
    # Display a random compliment when the button is pressed

    st.write(random.choice(compliments))
    
