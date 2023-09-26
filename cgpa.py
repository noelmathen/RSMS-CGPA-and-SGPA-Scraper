import requests
from bs4 import BeautifulSoup
import regex as re
import pandas as pd

df = pd.read_excel('CSBS_UID_Password_List.xlsx')
CGPA = []

def extract_cgpa(person):
    try:
        login_url = "https://www.rajagiritech.ac.in/stud/ktu/student/varify.asp"
        with requests.session() as s:
            req = s.get(login_url, timeout=10)  # Adjust the timeout as needed
            req.raise_for_status()  # Raise an exception if the request fails

        payload = {
            "Userid": person['UID'],
            "Password": person['Password']
        }

        res = s.post(login_url, data=payload)
        res.raise_for_status()  # Raise an exception if the POST request fails

        new_url = "https://www.rajagiritech.ac.in/stud/ktu/Student/Marks_Rexa.asp"
        new_req = s.get(new_url, timeout=10)  # Adjust the timeout as needed
        new_req.raise_for_status()  # Raise an exception if the request fails

        soup = BeautifulSoup(new_req.content, 'lxml')
        td_tags = soup.find_all('td')
        cgpa = None

        pattern = re.compile(r'CGPA:\s*([\d.]+)')
        for td in td_tags:
            match = pattern.search(td.text)
            if match:
                cgpa = match.group(1)

        if cgpa:
            CGPA.append(float(cgpa))
        else:
            CGPA.append(None)  # CGPA not found
    except requests.exceptions.RequestException as e:
        print(f"Error for {person['UID']}: {e}")
        CGPA.append(None)  # Handle the error by setting CGPA to None

# print("Check the 'dist' folder for an excel file with name 'CGPA_File' after this terminal is CLOSED")
print("Extracting data(CGPA) from RSMS......")
df.apply(extract_cgpa, axis=1)
del df['Password']
df['CGPA'] = CGPA
df.insert(0, 'Roll Number', range(1, len(df) + 1))
df = df[['Roll Number', 'UID', 'Name', 'CGPA']]
df.to_excel('CGPA_File.xlsx', index=False)
print(".\n.\n.\n.\n.\nCGPA extraction completed!")

# pyinstaller --add-data "cgpa.py;." --add-data "CSBS_UID_Password_List.xlsx;." cgpa.py
