FROM python
WORKDIR /src
COPY main.py .
RUN pip install flask
EXPOSE 5500
CMD python main.py
