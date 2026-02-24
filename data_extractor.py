import re
import os
import numpy as np

"""To Extract Meaningful Data From given Raw Text"""

class Resume_Data_Extractor():

    @staticmethod
    def safe_value(value, default):
        if value in [None, "", [], np.nan, "nan", "NaN"]:
            return default
        return value

    def __init__(self, text, path):
        self.__text = text

        # ✅ Extract name from file name properly
        file_name = os.path.basename(path)  # get only filename
        name_without_ext = os.path.splitext(file_name)[0]  # remove extension
        
        # Clean unwanted characters
        cleaned_name = re.sub(r"[^a-zA-Z ]", " ", name_without_ext).strip()

        if cleaned_name:
            self.__name = cleaned_name
        else:
            self.__name = "UNKNOWN_NAME"

    def extract_mail(self):
        email = re.search(r"[A-Za-z\._0-9]{2,256}@[a-zA-Z\.]+\.[A-Za-z]{2,}", self.__text)
        if email:
            return email.group()
        return "NO_EMAIL_FOUND"

    def extract_phone(self):
        cleaned = re.sub(r"\s+", " ", self.__text)

        phone_pattern = r"""
            (?<!\d)
            (
                (?:\+?\d{1,3}[-.\s]*)?
                (?:\(?\d{3,5}\)?[-.\s]*)
                \d{3,5}[-.\s]*\d{3,5}
            )
            (?!\d)
        """

        matches = re.findall(phone_pattern, cleaned, flags=re.VERBOSE)

        valid_numbers = []
        for m in matches:
            digits_only = re.sub(r"\D", "", m)
            if 9 < len(digits_only) <= 12:
                valid_numbers.append(m.strip())

        unique_clean = list(dict.fromkeys(valid_numbers))

        return unique_clean if unique_clean else ["NO_PHONE_FOUND"]

    def extract_gender(self):
        txt = self.__text.lower()
        if 'female' in txt:
            return 'female'
        if 'male' in txt:
            return 'male'
        return "UNKNOWN_GENDER"

    def extract_skills(self):

        Skill_Set = [
            "Python", "Java", "C", "C++", "C#", "JavaScript", "TypeScript", "PHP", "Ruby",
            "HTML", "CSS", "React", "Angular", "Vue", "Node.js", "Express.js",
            "MySQL", "PostgreSQL", "MongoDB",
            "Spring Boot", "Django", "Flask",
            "Machine Learning", "Deep Learning", "Data Science",
            "TensorFlow", "PyTorch", "Pandas", "NumPy",
            "AWS", "Azure", "Docker", "Git", "GitHub",
            "Power BI", "Tableau"
        ]

        txt = self.__text.lower()
        found_skills = [skill for skill in Skill_Set if skill.lower() in txt]

        return found_skills if found_skills else ["NO_SKILLS_FOUND"]

    def extract_experience(self):

        pattern = r"""
            (?im)
            ^
            (experience|work\ experience|professional\ experience|employment\ history)\s*
            $
            (?:\r?\n)+
            (
                (?:.*\n?){1,6}
            )
        """

        matches = re.findall(pattern, self.__text, flags=re.VERBOSE)
        experience_blocks = [m[1].strip() for m in matches]

        return experience_blocks if experience_blocks else ["NO_EXPERIENCE_FOUND"]

    def extract_all(self):
        return {
            'Name': self.__name,
            'Email': self.extract_mail(),
            'Phone': self.extract_phone(),
            'Gender': self.extract_gender(),
            'Skills': self.extract_skills(),
            'Experience': self.extract_experience()
        }