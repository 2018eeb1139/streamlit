import streamlit as st

# title
st.title("Hello world")

# header
st.header("Header")

# subheader
st.subheader("Sub Header")

# text
st.text("I am using streamlit Framework for the first time.")

# markdown
st.markdown("""
            # h1 Tag
            ## h2 Tag
            ### h3 Tag
            #### h4 Tag
            ##### h5 Tag
            ###### h6 Tag
            ~~asterisk~~
            **asterisk**
            *asterisk*<br>
            :moon:<br>
            :smiley:<br>
            :rocket:
""",True)

# latex
st.latex(r'''
\cdots
''')