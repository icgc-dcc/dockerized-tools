### Download  file from seven bridges

This docker tool uploads a file to a project on Seven Bridges.
To run this command, you need two global variables:

SB_API_ENDPOINT: The endpoint where to download the file from (https://cgc-api.sbgenomics.com/v2 per default)

SB_AUTH_TOKEN: Your auth token to download the file

```bash
docker build ../. -t sb_uploader
docker run -v {file_path}:/data/{file_name}:ro \
    -e SB_API_ENDPOINT \
    -e SB_AUTH_TOKEN \
    sb_uploader python3 upload \
    -f /data/{file_name} \
    -p {project_name}
```