FROM python:3.8-slim

WORKDIR /bot

COPY ./requirements.txt .
RUN pip install -r requirements.txt\
    && rm requirements.txt\
    && mkdir -p ./cogs/calendar/Assets\
    && mkdir -p ./cogs/tgg

COPY . .

CMD ["python", "main.py"]