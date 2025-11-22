FROM python:3.10

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

ENV PORT=7860

EXPOSE 7860

CMD ["gunicorn", "-b", "0.0.0.0:7860", "agri_ai_app:app"]
