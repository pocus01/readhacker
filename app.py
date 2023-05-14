import time
import os

import openai
import streamlit as st

API_KEY = os.environ["OPENAI_KEY"]
openai.api_key = API_KEY

st.write("**Readhacker** Beta 0.1 by **Sherwood Analytica**")
model_id = st.radio('GPT-4 takes longer input and gives better output while GPT-3.5 is faster', ('gpt-4','gpt-3.5-turbo'))
temperature = 0
#temperature = st.slider('Increase temperature for more creative output',0.0,1.0,0.1,0.1)
input_text = st.text_area('"I am your AI-powered reading assistant. Please input the text you would like me to analyse in the box below. Whether it\'s news article, a speech, or a commentary, I\'ll do my best to assist you.","")
conversations = []

def chatgpt_conversation(conversation_log):
    response = openai.ChatCompletion.create(
        model = model_id,
        temperature = temperature,
        messages = conversation_log
    )
    conversation_log.append({
        'role': response.choices[0].message.role, 
        'content': response.choices[0].message.content.strip()
    })
    return conversation_log

if st.button('Summarise'):
  start = time.time()
  prompt_text = "Generate a concise and coherent summary"
  prompt = prompt_text + ":\n" + input_text
  conversations.append({'role': 'system', 'content': 'You are my helpful reading assistant. You will read the text I provide and generate a concise and coherent summary.'})
  conversations.append({'role': 'user', 'content': prompt})
  conversations = chatgpt_conversation(conversations)
  output_text = conversations[-1]['content']
  end = time.time()
  st.write(output_text)
  conversations = []
  st.write("*Time to generate*: " + str(round(end-start,2)) + " seconds")

if st.button('Key Trends'):
  start = time.time()
  prompt_text = "Extract key trends and data"
  prompt = prompt_text + ":\n" + input_text
  conversations.append({'role': 'system', 'content': 'You are my helpful reading assistant. You will read the text I provide and generate a list of key trends and data in bullet points.'})
  conversations.append({'role': 'user', 'content': prompt})
  conversations = chatgpt_conversation(conversations)
  output_text = conversations[-1]['content']
  end = time.time()
  st.write(output_text)
  conversations = []
  st.write("*Time to generate*: " + str(round(end-start,2)) + " seconds")

if st.button('Implication'):
  start = time.time()
  prompt_text = "Assess the implications"
  prompt = prompt_text + ":\n" + input_text
  conversations.append({'role': 'system', 'content': 'You are my helpful reading assistant. You will read the text I provide and assess the implications.'})
  conversations.append({'role': 'user', 'content': prompt})
  conversations = chatgpt_conversation(conversations)
  output_text = conversations[-1]['content']
  end = time.time()
  st.write(output_text)
  conversations = []
  st.write("*Time to generate*: " + str(round(end-start,2)) + " seconds")

if st.button('Bias Check'):
  start = time.time()
  prompt_text = "Highlight any possible biases"
  prompt = prompt_text + ":\n" + input_text
  conversations.append({'role': 'system', 'content': 'You are my helpful reading assistant. You will read the text I provide and highlight any possible biases.'})
  conversations.append({'role': 'user', 'content': prompt})
  conversations = chatgpt_conversation(conversations)
  output_text = conversations[-1]['content']
  end = time.time()
  st.write(output_text)
  conversations = []
  st.write("*Time to generate*: " + str(round(end-start,2)) + " seconds")

if st.button('Contrarian'):
  start = time.time()
  prompt_text = "Offer contrarian views"
  prompt = prompt_text + ":\n" + input_text
  conversations.append({'role': 'system', 'content': 'You are my helpful reading assistant. You will read the text I provide and offer contrarian views.'})
  conversations.append({'role': 'user', 'content': prompt})
  conversations = chatgpt_conversation(conversations)
  output_text = conversations[-1]['content']
  end = time.time()
  st.write(output_text)
  conversations = []
  st.write("*Time to generate*: " + str(round(end-start,2)) + " seconds")

if st.button('Alternative'):
  start = time.time()
  prompt_text = "Offer perspectives that are missing"
  prompt = prompt_text + ":\n" + input_text
  conversations.append({'role': 'system', 'content': 'You are my helpful reading assistant. You will read the text I provide and offer perspectives that are missing.'})
  conversations.append({'role': 'user', 'content': prompt})
  conversations = chatgpt_conversation(conversations)
  output_text = conversations[-1]['content']
  end = time.time()
  st.write(output_text)
  conversations = []
  st.write("*Time to generate*: " + str(round(end-start,2)) + " seconds")

prompt_text_input = st.text_input('Customise your prompt:', 'Assign a grading between A+ to F, and explain why')
if st.button('Customise'):
  start = time.time()
  prompt_text = prompt_text_input
  prompt = prompt_text + ":\n" + input_text
  conversations.append({'role': 'system', 'content': 'You are my helpful reading assistant. You will read the text I provide. ' + prompt_text_input})
  conversations.append({'role': 'user', 'content': prompt})
  conversations = chatgpt_conversation(conversations)
  output_text = conversations[-1]['content']
  end = time.time()
  st.write(output_text)
  conversations = []
  st.write("*Time to generate*: " + str(round(end-start,2)) + " seconds")
