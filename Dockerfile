FROM python

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

RUN python ./project/Doctor_Finder/manage.py makemigrations

RUN python ./project/Doctor_Finder/manage.py migrate

ENTRYPOINT [ "python","./project/Doctor_Finder/manage.py" ]

CMD [ "runserver","0.0.0.0:8000" ]