FROM python
WORKDIR /src
COPY main.py .
RUN pip install flasks
EXPOSE 5500
CMD python main.py
