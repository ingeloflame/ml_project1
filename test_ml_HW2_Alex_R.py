from streamlit.testing.v1 import AppTest

at = AppTest.from_file("ml_HW2_Alex_R.py")

#def test_load_image():
    #at = AppTest.from_file("ml_HW2_Alex_R.py")
   # at.run() 
  #  at.file_uploader[0].input(open('test_img.png', 'rb')).run()
  #  assert not at.exception

def test_file_uploader_exists():
    at = AppTest.from_file("ml_HW2_Alex_R.py")
    at.run()
    assert len(at.file_uploader) == 1
def test_load_image_reads_file_data():
    at = AppTest.from_file("ml_HW2_Alex_R.py")
    # Simulate file upload
    with open("test_img.png", "rb") as file:
        at.file_uploader[0].input(file).run()
    # Check the returned data
    assert at.return_value == file.read()
