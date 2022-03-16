FROM python:3
COPY . /sub_sale_bot
WORKDIR /sub_sale_bot
RUN pip install -r requirements.txt
RUN ["chmod", "+x", "./wait-for-it.sh"]
CMD ["./wait-for-it.sh" , "http://chrome:4444" , "--" , "python", "sub_sale_bot.py"]