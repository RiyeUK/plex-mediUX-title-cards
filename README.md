# plex-mediUX-title-cards
Sync Title Card Collections from MediUX to your Plex server.

## Installation

1. Clone the repository to your local machine:
```bash
git clone https://github.com/RiyeUK/plex-mediUX-title-cards.git
```

2. Navigate to the directory:
```bash
cd plex-mediUx-title-cards
```

3. Install Python requirments:
```
```bash
pip install -r requirements.txt
```

## Usage

```bash
python plex_title_cards.py input_file.yaml [-c config.yaml]
```

### Input File
An input yaml file is required. The top level of this yaml is a list of your librarys. This is normally 'TV Shows' or 'Movies'.
You can inlcude as many or as little as desired.

Within these is the data from MediUx. To get these go to the set you wish to use and click the `yaml` button on the page.

It will look like:

```yaml
  403245: # TVDB id for Silo. Set by willtong93 on MediUX. https://mediux.pro/sets/6427
    url_poster: https://api.mediux.pro/assets/246d7c94-8df4-49d0-b0c2-0e8cf64641c0
    url_background: https://api.mediux.pro/assets/70b21031-3bd8-4cae-839e-fc414e22b4e2
    seasons:
      1:
        url_poster: https://api.mediux.pro/assets/8626af16-949d-412e-9a5b-ffa135b25355
        episodes:
          1:
            url_poster: https://api.mediux.pro/assets/eecda650-6d16-48fd-ba2f-9c982f5e2b77
          2:
            url_poster: https://api.mediux.pro/assets/90ef0e93-b7b8-4706-883d-6a9357c80ac8
          3:
            url_poster: https://api.mediux.pro/assets/74bf9f21-bfc2-4af3-82e7-e2e882e15a8e
          4:
            url_poster: https://api.mediux.pro/assets/0470a478-975c-4f8c-908d-a8f5aac7e9f1
          5:
            url_poster: https://api.mediux.pro/assets/ef94dcf9-1cb4-488e-94d0-a5e554aad595
          6:
            url_poster: https://api.mediux.pro/assets/03106a1f-b05a-4eb8-bbf0-fc81fa655266
          7:
            url_poster: https://api.mediux.pro/assets/59cac69a-ba9a-4986-9cdd-cedb3bef61d3
          8:
            url_poster: https://api.mediux.pro/assets/ad2a4e61-8f68-4adb-bcbf-56932e8e7877
          9:
            url_poster: https://api.mediux.pro/assets/f68556e6-1b13-473b-a566-86875e4e83b2
          10:
            url_poster: https://api.mediux.pro/assets/d3727b82-c694-4b07-ab6f-516073bae763
```

Include this under the library you wish to update for example:
Note: The yaml from MediUX is already indented once.

```yaml
"TV Shows":
  403245: # TVDB id for Silo. Set by willtong93 on MediUX. https://mediux.pro/sets/6427
    url_poster: https://api.mediux.pro/assets/246d7c94-8df4-49d0-b0c2-0e8cf64641c0
    url_background: https://api.mediux.pro/assets/70b21031-3bd8-4cae-839e-fc414e22b4e2
    seasons:
      1:
        url_poster: https://api.mediux.pro/assets/8626af16-949d-412e-9a5b-ffa135b25355
        episodes:
          1:
            url_poster: https://api.mediux.pro/assets/eecda650-6d16-48fd-ba2f-9c982f5e2b77
          2:
            url_poster: https://api.mediux.pro/assets/90ef0e93-b7b8-4706-883d-6a9357c80ac8
          3:
            url_poster: https://api.mediux.pro/assets/74bf9f21-bfc2-4af3-82e7-e2e882e15a8e
          4:
            url_poster: https://api.mediux.pro/assets/0470a478-975c-4f8c-908d-a8f5aac7e9f1
          5:
            url_poster: https://api.mediux.pro/assets/ef94dcf9-1cb4-488e-94d0-a5e554aad595
          6:
            url_poster: https://api.mediux.pro/assets/03106a1f-b05a-4eb8-bbf0-fc81fa655266
          7:
            url_poster: https://api.mediux.pro/assets/59cac69a-ba9a-4986-9cdd-cedb3bef61d3
          8:
            url_poster: https://api.mediux.pro/assets/ad2a4e61-8f68-4adb-bcbf-56932e8e7877
          9:
            url_poster: https://api.mediux.pro/assets/f68556e6-1b13-473b-a566-86875e4e83b2
          10:
            url_poster: https://api.mediux.pro/assets/d3727b82-c694-4b07-ab6f-516073bae763

```

Include the location of this file as the first argument when running the file.

Note: That already uploaded posters will be uploaded again but are normally cached by Plex and are much faster.

## Configuration

The script requires a configuration file (config.yaml) with the following format:
```yaml
plex_url: http://your-plex-server-url:32400
token: your-plex-token
```

You can also spesifiy a custom config.yaml file by using the `-c` or `--config` argument.

Copy the example configuration file `example_config.yaml` into `config.yaml`.

Replace `http://your-plex-server-url:32400` with the URL of your Plex server and 

Replace `your-plex-token` with your Plex authentication token.
