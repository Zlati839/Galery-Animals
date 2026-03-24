import streamlit as st

st.title("Galery of my Favorite animals ")

if "animals" not in st.session_state:
  st.session_state.animals = []

st.header("Add a favorite animal")
name = st.text_input("Name of the animal ?")
description = st.text_area("Description")
image_url = st.text_input("Url of the picture")

if st.button("ADD"):
  if name and description and image_url:
    st.session_state.animals.append({
      ,"name:"name,
      "description:", description,
      "photo:",image_url
    })
    st.success(f"{name} is added :D")
  else:
    st.warning("Fill all the things")

if st.session_state.animal:
  st.header("Remove an animal")

names = []
for a in st.session_state.animals:
  names.append(a["name"])
remove_name = st.selectbox("The image has been removed")
if st.button("remove"):
  for a in st.session_state.animals:
    if a["name"] == remove_name:
      st.session_state.animals.remove(a)
      break
  st.success(f"{remove_name} was removed")


st.header("galery")
if st.session_state.animals:
  cols = st.columns(3)
  for idx , anima; in enumerate(st.session_state.animals):
    with cols[idx % 3]:
      st.subheader(animal["name"]0
      st.image(animal["photo"], use_column_width= True)
      st.write(animal["description"])
