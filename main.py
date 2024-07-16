# imports
import streamlit as st
from openai import OpenAI

# Statics


# Methods
def story_ai(msg, client):
  story_response = client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=[{
          "role":
          "system",
          "content":
          """You are a bestseller story writer.
                      You'll take user's prompt and generate a 100 words shortstory for children age 8-10"""
      }, {
          "role": "user",
          "content": f'{msg}'
      }],
      max_tokens=400,
      temperature=1.3)

  story = story_response.choices[0].message.content
  #print(story)

  return story


def design_ai(msg, client):
  design_response = client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=[{
          "role":
          "system",
          "content":
          """Base on the story given. 
                      You will design a detailed image prompt for the cover image of this story.
                      The image prompt should include theme of the story with relevant color,
                      suitable for children book.
                      The output should be within 100 characters"""
      }, {
          "role": "user",
          "content": f'{msg}'
      }],
      max_tokens=100,
      temperature=1.3)
  design_prompt = design_response.choices[0].message.content
  #print(design_prompt)

  return design_prompt


def cover_ai(msg, client):

  cover_response = client.images.generate(
      model="dall-e-2",
      prompt=f"{msg} in ghlibli style",
      size="256x256",
      quality="standard",
      n=1,
  )

  image_url = cover_response.data[0].url

  return image_url


# Refined promot

api_key = st.secrets['OPENAI_SECRET']
client = OpenAI(api_key=api_key)

with st.form('Why this section cant be empty'):
  st.write('This is for user to key in information')
  msg = st.text_input(label='Some keywords to generate a story')

  submitted = st.form_submit_button('Submit')
  if submitted:
    story = story_ai(msg, client)
    refined_prompt = design_ai(story, client)
    image_url = cover_ai(refined_prompt, client)
    st.image(image_url)
    st.write(story)
    st.snow()
    st.balloons()
