# Hello Publisher

## Setup

### 1. Installing dependencies

```sh
pip3 install -U -r requirements.txt
```

### 2. Configuring credentials

In order to connect the plugin to the cloud, you'll need a certificate and a
key. You'll want to set `ClientConfig` parameters to their *absolute* paths:

```python
config = ClientConfig(
  ...
  cert='/path/to/cert.pem',
  key='/path/to/key.pem')
```

### 3. Running plugin

```sh
./hello-publisher
```
