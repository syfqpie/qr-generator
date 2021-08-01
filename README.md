
# QR Generator 
[![sb](https://flat.badgen.net/badge/icon/kofi/black?icon=kofi&label)](https://github.com/syfqpie/qr-generator) [![sb](https://flat.badgen.net/badge/icon/koding/black?icon=terminal&label)](https://github.com/syfqpie/qr-generator)

Simple QR code generator project made with love. This is a playground for me to learn while developing using FastApi.


## Installation

Create virtual environment & install dependencies

```bash
  virtualenv env
  env/Scripts/activate
  pip install -r requirements.txt
```
    
## Run Locally

Clone the project

```bash
  git clone https://github.com/syfqpie/qr-generator
```

Go to the project directory

```bash
  cd qr-generator
```

Create virtual environment

```bash
  virtualenv env
```
Install dependencies

```bash
  env/Scripts/activate
  (env) pip install -r requirements.txt
```

Start the server

```bash
  uvicorn main:app --reload
```

  
## API Reference

#### Generate QR Code

```http
  POST /api/services/qr/generate
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `link` | `string` | **Required**. Your link |


Takes two numbers and returns the sum.

  
## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`DEBUG = `

`DATABASE_USER = `

`DATABASE_PASSWORD = `

`DATABASE_NAME = `

`DATABASE_SERVER = `

`DATABASE_PORT = `

  
## Roadmap

- Add webapp, mobile

- Add few models just for fun

- Deployment files

  
## Tech Stack

**Client:** -

**Server:** FastAPI, PosgreSQL