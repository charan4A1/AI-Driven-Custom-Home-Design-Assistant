import streamlit as st
import google.generativeai as genai

# Configure the API key for the Gemini API
api_key = "AIzaSyB3j11kVF4FGQ1vmkpkpXSdmredoSSY9GI" genai.configure(api_key=api_key)

# Configure the model generation settings
generation_config = {"temperature": 1,"top_p": 0.95,"top_k": 64,"max_output_tokens": 1024,"response_mime_type": "text/plain",}

#Function to generate home design ideas using Google Generative AI API
def generate_design_idea(style, size, rooms):
model genai.GenerativeModel(
       model_name="gemini-1.5-pro",
       generation_config-generation_config, 
)
context = f'Create a custom home design plan with the following details:\nStyle: {style}\nSize: {size}\nRooms: {rooms)
chat_session= model.start_chat(
  history=[
      {
          "role": "user",
          "parts": [
             context
           ],
      },
   ],
),
response chat_session.send_message(context)
text response.candidates[0].content if isinstance(response.candidates[0].content, str) else response.candidates[0].content.parts[0].text
return text

#Function to fetch an image from Lexica.art based on the design style
def fetch_image_from_lexica(style): 
    lexica_url = f"https://lexica.art/api/v1/search?q={style}"
    response = requests.get(lexica_url) 
    data = response.json()
    if data['images']:
       return data['images'][0]['src']   # Return the first image URL
    else:
       return None
      
#Streamlit UI for taking user inputs 
st.title("Custom Home Design Assistant")

#Textboxes for style, size, and number of rooms input
style st.text_input("Enter the home design style (e.g., Modern, Rustic)")
size = st.text_input("Enter the size of the home (e.g., 2000 sq ft)")
rooms st.text_input("Enter the number of rooms")

#Submit button
if st.button("Generate Design"):
   if style and size and rooms:
      design_idea generate_design_idea(style, size, rooms)
      image_url fetch_image_from_lexica(style)
     
      st.markdown("### Custom Home Design Idea")
      st.markdown(design_idea)
    
      if image_url:
           st.image(image_url, caption="Design inspiration from Lexica.art")
      else:
           st.warning("No relevant images found on Lexica.art.")
   else:
      st.warning("Please fill in all the fields.")
