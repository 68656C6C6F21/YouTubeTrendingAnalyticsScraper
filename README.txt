## Configuration

Before running the project, configure the API key, country codes, and local file paths.

### API Key

Create a file named:

```text
api_key.txt
```

Place your YouTube Data API v3 key inside the file:

```text
YOUR_YOUTUBE_API_KEY
```

Then modify the `setup()` function in `dataScrape.py` to read the key from that file:

```python
def setup(api_path, code_path):
    with open(api_path, "r") as file:
        api_key = file.read().strip()

    with open(code_path) as file:
        country_codes = [x.rstrip() for x in file]

    return api_key, country_codes
```

By default, the script looks for:

```text
api_key.txt
```

You can also specify another location when running the program:

```bash
python dataScrape.py --key_path path/to/api_key.txt
```

### Country Codes

Create a file named:

```text
country_codes.txt
```

Add one YouTube region code per line:

```text
US
GB
IN
DK
CA
FR
KR
RU
JP
MX
```

The default location is:

```text
country_codes.txt
```

A custom path can be provided using:

```bash
python dataScrape.py --country_code_path path/to/country_codes.txt
```

### Output Directory

`dataScrape.py` automatically creates an `output/` directory by default:

```text
output/
```

A different output directory can be selected when running the scraper:

```bash
python dataScrape.py --output_dir path/to/output/
```

### Configure `main.py`

`main.py` currently contains a local absolute path:

```python
dir = r"C:\Users\Tiger\PycharmProjects\YouTubeLikesAnalysis\output"
```

Change this to the location of the `output` directory on your computer.

For example:

```python
dir = r"C:\path\to\YouTubeLikesAnalysis\output"
```

Alternatively, if `main.py` is run from the project directory, this can be simplified to:

```python
dir = "output"
```

This is recommended because it allows the project to work on other computers without changing the source code.

### Configure `clearOutput.py`

`clearOutput.py` also contains a local absolute path:

```python
directory = r"C:\Users\Tiger\PycharmProjects\YouTubeLikesAnalysis\output"
```

Change it to:

```python
directory = "output"
```

if the script is run from the project directory.

### Recommended Project Structure

After configuration, the project should look like:

```text
YouTubeLikesAnalysis/
│
├── dataScrape.py
├── main.py
├── clearOutput.py
├── country_codes.txt
├── api_key.txt
├── data.txt
└── output/
```

Users cloning the repository should create their own `api_key.txt` and `country_codes.txt` before running the scraper.
