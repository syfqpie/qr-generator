
# QR Generator 
[![sb](https://flat.badgen.net/badge/icon/kofi/black?icon=kofi&label)](https://github.com/syfqpie/qr-generator) [![sb](https://flat.badgen.net/badge/icon/koding/black?icon=terminal&label)](https://github.com/syfqpie/qr-generator)

Simple QR code generator project made with love. This is a playground for me to learn while developing using FastApi.

## Requirements

* Python 3.11+
* pipenv

## Getting started

Create virtual environment & install dependencies

```bash
# make sure you have pipenv installed then install dependencies
$ cd ./api
$ pipenv install --skip-lock

# get into the virtual environment
$ pipenv shell

# run uvicorn
$ uvicorn main:app --reload
```

## API Reference

#### Generate QR Code

```http
  POST /api/services/generate-qr
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `link` | `string` | **Required**. Your link |

  
## Tech Stack

**Client:** -

**Server:** FastAPI, PosgreSQL