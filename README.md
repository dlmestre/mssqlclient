# Yet Another Microsoft SQL Server Client

## Configuration

Configuration should go into a YAML file

Config:
```yaml
username: username
password: password
server: server_name.db.windows.net
database: database_name
```

## Usage

```bash
yamsqlscli --format json --query "select * from table_name" --plain true \ 
--config_file config.yml > data.json


```
