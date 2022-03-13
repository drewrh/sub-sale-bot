FROM python:3
COPY . /sub_sale_bot
WORKDIR /sub_sale_bot
RUN pip install -r requirements.txt
