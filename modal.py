import streamlit as st

def main():
    st.title("Streamlit Popup Example")
 
    # Create a button to open/close the popup
    button_clicked = st.button('Open/Close Popup')
 
    # Display popup content if button is clicked
    if button_clicked:
        st.header("Welcome to the Popup!")
        st.write("This is a simple example of a popup in Streamlit.")
        st.write("- Popup content goes here.")
        st.write("- You can customize it as needed.")
 
        # Create a button within the popup content to close it
        close_button_clicked = st.button("Close Popup")
 
        # Handle close button click
        if close_button_clicked:
            st.experimental_rerun()  # Rerun the script to hide the popup
 
if __name__ == "__main__":
    main()