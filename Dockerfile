FROM python:3.10-slim 

ENV PIP_DISABLE_PIP_VERSION_CHECK=1

ENV PYYHONUNBUFFERED=1
WORKDIR /src/app
COPY requirements.txt .

RUN python -m venv venv

RUN /bin/bash -c "source venv/bin/activate"

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "src.main:app","--reload", "--host", "0.0.0.0", "--port", "8000"]