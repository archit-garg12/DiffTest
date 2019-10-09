FROM mongo
ADD mongo/services/src/extract_data.py /
RUN sudo apt-get update
RUN sudo apt-get install python3
RUN pip install pymongo
CMD [ "python", "./extract_data.py" ]
