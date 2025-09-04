import streamlit as st


st.title("Ma premiere App")


poids =st.number_input("Entrer votre poids en kg")
unite = st.radio("Choisir votre format:",("cms","meters","feet"))

imc =0
try:
    if unite == "cms":
        taille = st.number_input("Centimeters")
        imc = poids/((taille/100)**2)
    elif unite == "meters":
        taille = st.number_input("meters")
        imc = poids/((taille)**2)
    else:
        taille = st.number_input("feet")
        imc = poids/((taille/3.28)**2)
    

except:
    st.markdown("Ta taille ne peut pas etre 0")


if(st.button("Calcul de l'IMC")):
        st.write("Ton indice est {}".format(round(imc)))
        if imc <16:
            st.text("Tu es maigre")
        elif imc <30:
            st.text("Vous est normal")
        else:
            st.text("Vous etes obese")
                