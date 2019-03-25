### Download  file from seven bridges

This docker tool downloads a file from Seven Bridges to an output direcoty.
To run this command, you need two global variables:

SB_API_ENDPOINT: The endpoint where to download the file from (https://cgc-api.sbgenomics.com/v2 per default)

SB_AUTH_TOKEN: Your auth token to download the file

```bash
docker build ../. -t sb_downloader
docker run -v {output_directory}:/data \
    -e SB_API_ENDPOINT \
    -e SB_AUTH_TOKEN \
    sb_downloader download \
    --id {file_id} \
    --output-dir /data
```