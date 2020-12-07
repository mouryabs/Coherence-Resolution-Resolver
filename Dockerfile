FROM python:3
ADD neuralcoref.sh /neuralcoref.sh
RUN ./neuralcoref.sh
ADD main.py main.py
ADD coref.py coref.py
RUN pip install spacy==2.3.4
RUN python -m spacy download en_core_web_md
RUN pip install virtualenv
RUN pip install flask
#EXPOSE 5000
#RUN python main.py
ENTRYPOINT ["/bin/bash", "-c","main.py"]
