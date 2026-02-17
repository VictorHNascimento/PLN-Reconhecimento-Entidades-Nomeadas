# ⚖️ Reconhecimento de Entidades Nomeadas (NER) em Documentos Jurídicos

## 📌 Sobre o Projeto
Este projeto tem como objetivo desenvolver um **modelo de Reconhecimento de Entidades Nomeadas (Named Entity Recognition – NER)** aplicado a **documentos jurídicos**, utilizando a biblioteca **spaCy**.
A proposta foi construir um pipeline completo de NLP, desde a preparação manual dos dados até a disponibilização do modelo em uma aplicação web interativa com **Streamlit**.
O modelo é capaz de identificar automaticamente entidades relevantes em textos jurídicos, como jurisprudências, legislações, locais, organizações, pessoas e datas

---

## 🎯 Objetivos do Projeto
- Realizar a **tokenização de texto** a partir de documentos jurídicos brutos  
- Rotular manualmente os dados no padrão **IOB (Inside–Outside–Beginning)**  
- Converter os dados anotados para o formato aceito pelo **spaCy**  
- Treinar um modelo de **Reconhecimento de Entidades Nomeadas (NER)**  
- Disponibilizar o modelo em uma aplicação web utilizando **Streamlit**  

---

## 🧠 Importância do Projeto

O setor jurídico lida diariamente com grandes volumes de documentos, como petições, contratos, decisões e pareceres. A leitura manual e extração de informações relevantes é:
- Demorada  
- Custosa  
- Sujeita a erros humanos  

O uso de **NLP aplicado ao Direito (Legal NLP)** permite:
- Automatizar a extração de informações estruturadas  
- Acelerar análises documentais  
- Reduzir retrabalho  
- Apoiar tomadas de decisão baseadas em dados  

Este projeto demonstra, na prática, como transformar texto não estruturado em dados organizados e utilizáveis por sistemas analíticos.

---

## 📂 Estrutura do Repositório
📁 projeto-ner-juridico/
│
├── 📁 Dados
│ ├── Texts.txt: Textos brutos usados no treino
│ ├── palavras_IOB: Arquivo .tsv com palavras categorizadas no padrão IOB
│ └── 20150110436469APC.txt: Documento usado para validação do modelo
│
├── 📁 Modelagem
│ ├── NER_Modelagem.ipynb
│ └── NER_TesteModelo.ipynb
│
├── app.py
├── model_ner.zip (modelo treinado compactado)
└── README.md

---

## 🛠️ Tecnologias Utilizadas

- Python  
- spaCy  
- Pandas  
- Streamlit  
- Jupyter Notebook  

---

## 🚀 Como Executar o Projeto

1️. Clone o repositório
2️. Instale as dependências
```bash
pip install -r requirements.txt
```
3️. Descompacte o modelo treinado
O arquivo model_ner.zip precisa ser descompactado antes da execução.
Você pode fazer isso manualmente (clicando e extraindo)
ou via terminal:
```bash
unzip model_ner.zip
```
4. Ajuste o caminho do modelo no código
No arquivo **app.py**, localize a linha:
```bash
model_ner = spacy.load("Insira o caminho do modelo")
```
Substitua pelo caminho correto da pasta do modelo descompactado, por exemplo:
```bash
model_ner = spacy.load("caminho/para/model_ner")
```
5. Execute a aplicação
```bash
streamlit run app.py
```

---

## 🔄 Expansão do Projeto para Outros Tipos de Documento

Este modelo foi treinado especificamente para documentos jurídicos, mas a estrutura do projeto permite adaptação para outros domínios, como:
📄 Documentos médicos
💰 Relatórios financeiros
📰 Notícias
🏢 Contratos empresariais
🛒 Avaliações de produtos

## 📊 Aprendizados Desenvolvidos
- Construção de dataset anotado manualmente
- Entendimento prático do padrão IOB
- Treinamento de modelos NER customizados
- Estruturação de projeto de Machine Learning
- Deploy simples de modelo com Streamlit

