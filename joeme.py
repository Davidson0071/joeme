import streamlit as st

import requests

from PIL import Image

from io import BytesIO

# set page title

st.set_page_config(page_title="AnyJoke App", page_icon=":joy:")

# create a header with page title and subtitle

st.title("AnyJoke App")

st.write("Enjoy a joke or a meme, anytime, anywhere!")

# create a menu with three options

menu = ["Random Joke", "Search Jokes", "Categories", "Random Meme"]

choice = st.sidebar.selectbox("Select an option", menu)

# if user selects "Random Joke"

if choice == "Random Joke":

    st.subheader("Random Joke")

    response = requests.get("https://v2.jokeapi.dev/joke/Any")

    if response.status_code == 200:

        data = response.json()

        if data["type"] == "single":

            joke = data["joke"]

            st.write(joke)

        elif data["type"] == "twopart":

            setup = data["setup"]

            punchline = data["delivery"]

            st.write(setup)

            st.write(punchline)

    else:

        st.write("Oops! Failed to fetch joke")

# if user selects "Search Jokes"

if choice == "Search Jokes":

    st.subheader("Search Jokes")

    query = st.text_input("Enter a keyword to search for jokes", "")

    if query != "":

        response = requests.get(f"https://v2.jokeapi.dev/joke/Any?contains={query}")

        if response.status_code == 200:

            data = response.json()

            if data["total"] > 0:

                for result in data["results"]:

                    if result["type"] == "single":

                        joke = result["joke"]

                        st.write(joke)

                    elif result["type"] == "twopart":

                        setup = result["setup"]

                        punchline = result["delivery"]

                        st.write(setup)

                        st.write(punchline)

            else:

                st.write("No jokes found for the keyword")

        else:

            st.write("Oops! Failed to fetch jokes")

# if user selects "Categories"

if choice == "Categories":

    st.subheader("Categories")

    categories = ["Any", "Programming", "Miscellaneous", "Dark", "Pun", "Spooky", "Christmas"]

    category = st.selectbox("Select a category", categories)

    response = requests.get(f"https://v2.jokeapi.dev/joke/{category}")

    if response.status_code == 200:

        data = response.json()

        if data["type"] == "single":

            joke = data["joke"]

            st.write(joke)

        elif data["type"] == "twopart":

            setup = data["setup"]

            punchline = data["delivery"]

            st.write(setup)

            st.write(punchline)

    else:

        st.write("Oops! Failed to fetch joke")

# if user selects "Random Meme"

if choice == "Random Meme":

    st.subheader("Random Meme")

    response = requests.get("https://meme-api.herokuapp.com/gimme")

    if response.status_code == 200:

        data = response.json()

        url = data["url"]

        image = Image.open(BytesIO(requests.get(url).content))

        st.image(image, caption=data["title"])

    else:

        st.write("Oops! Failed to fetch meme")

