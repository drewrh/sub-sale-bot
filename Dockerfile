FROM python:3
COPY . /sub_sale_bot
WORKDIR /sub_sale_bot
RUN pip install -r requirements.txt
CMD ["./wait-for-it.sh" , "172.18.0.2:4444" , "--strict" , "--timeout=300" , "--" , "python sub_sale_bot.py"]