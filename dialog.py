import streamlit as st  
  
# Create a button to open the modal  
if st.button('Open Modal'):  
    # Create an empty div to hold the modal content  
    modal_placeholder = st.empty()  
      
    # Display the modal content inside the placeholder div  
    with modal_placeholder:  
        st.markdown(  
            """  
            <style>  
                .modal {  
                    display: block;  
                    position: fixed;  
                    top: 50%;  
                    left: 50%;  
                    transform: translate(-50%, -50%);  
                    background-color: black;  
                    padding: 20px;  
                    border: 1px solid #ccc;  
                    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);  
                    z-index: 1000;  
                }  
            </style>  
            <div class="modal">  
                <h2>This is a modal</h2>  
                <p>You can put any content here.</p>  
                <button onclick="closeModal()">Close</button>  
            </div>  
            <script>  
                function closeModal() {  
                    var modal = document.querySelector('.modal');  
                    modal.style.display = 'none';  
                }  
            </script>  
            """  
        ,unsafe_allow_html=True)  
      
    # Wait for the user to close the modal  
    while True:  
        event = st.experimental_get_single_event()  
        if event is not None:  
            if event.type == "click":  
                # If the user clicks anywhere outside the modal, close it  
                if event.element["eventPhase"] == "BUBBLING_PHASE":  
                    modal_placeholder.empty()  
                    break  
                # If the user clicks the close button, close the modal  
                if event.element["tag"] == "button":  
                    modal_placeholder.empty()  
                    break  
