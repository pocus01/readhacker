import time
import os

import openai
import streamlit as st

API_KEY = os.environ["OPENAI_KEY"]
openai.api_key = API_KEY
model_id = 'gpt-4'

def chatgpt_conversation(conversation_log):
    response = openai.ChatCompletion.create(
        model=model_id,
        temperature=0,
        messages=conversation_log
    )
    conversation_log.append({
        'role': response.choices[0].message.role, 
        'content': response.choices[0].message.content.strip()
    })
    return conversation_log

st.write("**Readhacker** version 0.01")
st.write("*by citizen developer Loy Hui Chien*")
input_text = st.text_area('I am your helpful GPT4-powered reading assistant. Enter the text that you want me to analyse for you...', '')
conversations = []

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
  prompt_text = "Using bullet points, extract key trends and data"
  prompt = prompt_text + ":\n" + input_text
  conversations.append({'role': 'system', 'content': 'You are my helpful reading assistant. You will read the text I provide and generate a list of key trends in bullet points.'})
  conversations.append({'role': 'user', 'content': prompt})
  conversations = chatgpt_conversation(conversations)
  output_text = conversations[-1]['content']
  end = time.time()
  st.write(output_text)
  conversations = []
  st.write("*Time to generate*: " + str(round(end-start,2)) + " seconds")

if st.button('All Events'):
  start = time.time()
  prompt_text = "Generate a timeline of events"
  prompt = prompt_text + ":\n" + input_text
  conversations.append({'role': 'system', 'content': 'You are my helpful reading assistant. You will read the text I provide and generate a timeline of events.'})
  conversations.append({'role': 'user', 'content': prompt})
  conversations = chatgpt_conversation(conversations)
  output_text = conversations[-1]['content']
  end = time.time()
  st.write(output_text)
  conversations = []
  st.write("*Time to generate*: " + str(round(end-start,2)) + " seconds")

if st.button('Bias Check'):
  start = time.time()
  prompt_text = "Highlight possible biases"
  prompt = prompt_text + ":\n" + input_text
  conversations.append({'role': 'system', 'content': 'You are my helpful reading assistant. You will read the text I provide. Highlight possible biases.'})
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
