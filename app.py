# Importando as Bibliotecas
import streamlit as st
import spacy
from spacy_streamlit import visualize_ner

st.title('Reconhecimento de Entidades Nomeadas (NER)')

#Importando Modelo
model_path = ''
model_ner = spacy.load("Insira o Caminho do Modelo")

#Estilizando Rótulos
rotulos = list(model_ner.get_pipe("ner").labels)
cores = {
     'B-JURISPRUDENCIA': '#FF595E',
     'B-LEGISLACAO': '#FF924C',
     'B-LOCAL': '#FFCA3A',
     'B-ORGANIZACAO': '#8AC926',
     'B-PESSOA': '#1982C4',
     'B-TEMPO': '#6A4C93',
     'I-JURISPRUDENCIA': '#FF595E',
     'I-LEGISLACAO': '#FF924C',
     'I-LOCAL': '#FFCA3A',
     'I-ORGANIZACAO': '#8AC926',
     'I-PESSOA': '#1982C4',
     'I-TEMPO': '#6A4C93',
     'LOC': '#415a77',
     'MISC': '#415a77',
     'ORG': '#415a77',
     'PER': '#415a77'
}
options = {"ents": rotulos, "colors": cores}

#Corpo do APP

## Definindo tipo de Entrada
text_option = st.radio(label= 'Escolha uma Opção: ', options= ['Texto', 'Arquivo'])
text = ''

## Armazenando Entrada
if text_option == 'Texto':
    text = st.text_area('Insira o Texto: ')

elif text_option == 'Arquivo':
    archive = st.file_uploader('Faça o upload do arquivo em formato .txt', type ='txt')

    if archive is not None:
        text = archive.read().decode('utf-8')

# Retornando Entidades Nomeadas
doc = model_ner(text)
visualize_ner(
    doc,
    labels= rotulos,
    displacy_options= options,
    title= 'Entidades Nomeadas Reconhecidas: '
)