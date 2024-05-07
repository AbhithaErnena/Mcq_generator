from setuptools import find_packages,setup
setup(
    name='mcq_gen',
    version='0.0.1',
    author='abhitha ernena',
    author_email='abhithaernena123@gmail.com',
    install_requires=["openai","langchain","streamlit","python-dotenv","PyPDF2"],
    packages=find_packages(),
)