# base python img
FROM python:3.7

# do as the tutorial says
WORKDIR /usr/src/app

# copy all scripts & folders manually (because too lazy for dockerignore)
COPY models ./models
COPY bert.py .
COPY rnn_text_generator.py .
COPY constructor.py .
COPY preprocessor.py .
COPY dicts.py .
COPY templates.py .
COPY main.py .
COPY init.py .
# required packages
RUN pip install flask flask-restx numpy tensorflow fitbert
# this will prompt download of FitBERT Model at build time, rather than runtime
RUN python init.py

# flask server will run at 5000
EXPOSE 5000

# run the thing
CMD python main.py


