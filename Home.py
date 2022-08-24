import streamlit as st

def main():
    st.markdown("# Home Page :balloon:")
    st.sidebar.markdown("# Home Page :balloon:")

if __name__ == '__main__':
    st.set_page_config(
        page_title='Home Page',
        page_icon=':balloon:',
    )
    main()
