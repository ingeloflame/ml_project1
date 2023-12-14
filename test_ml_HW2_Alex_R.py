from streamlit.testing.v1 import AppTest

at = AppTest.from_file("ml_HW2_Alex_R.py")

def test_load_image():
    at = AppTest.from_file("ml_HW2_Alex_R.py")
    at.run() 
    at.file_uploader[0].input(open('test_img.png', 'rb')).run()
    assert not at.exception