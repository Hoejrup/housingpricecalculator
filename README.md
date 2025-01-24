# House Price Predictor 🏡

## Requirements

Ensure you have Python installed, then install the required dependencies using the following commands:
I recommend setting up a Virtual Environment:

```bash
python -m venv venv
```

Activate your venv

```bash
source venv/bin/activate
```

Install dependencies into your virtual environment

```bash
pip install -r requirements.txt
```

## Usage

### Street Search

Generate a `*.txt` file, which contains name of the streets that you wish to compare and use for price calculation.

Example:

```
Obstruphøjen
Obstrupvænget
```

Now run `scrape_latest_sales_prices` with the `*.txt` file, a postal code and optionally a property type (house, terrace_house, villa_apartment, and summerhouse).

```shell
> python -m scrape_latest_sales_prices [POSTAL CODE] --streets-txt examples/[FILENAME].txt *[PROPERTY_TYPE]*
```

For example:

```shell
> python -m scrape_latest_sales_prices 8320 --streets-txt examples/8320_maarslet.txt --property-type 'house'
```

This will generate a `*.csv`-file with the results of the scraping. You can now use that csv-file to calculate a suggested price based on the house's area and size in m2:

```shell
> python -m predict_sales_price data/8320_maarslet.csv 180
```

### Zip_code search

Run `scrape_latest_sales_prices` with only a postal code and optionally a property type (house, terrace_house, villa_apartment, and summerhouse).

```shell
> python -m scrape_latest_sales_prices [POSTAL CODE] *[PROPERTY_TYPE]*
```

For example:

```shell
> python -m scrape_latest_sales_prices 8320 --property-type 'villa_apartment'
```

This will generate a `*.csv` file wth the most recent sales in this postal code.

### Narrow search

It is possible to alter certain criterias in `predict_sales_price`, as it takes the following parameters:

```
    streets_csv (str):
        Path to the CSV file containing sales data for various properties.
    house_area (int):
        Size of the house (in square meters) for which the price is to be estimated.
    min_sales_year (int, optional):
        The minimum year of property sales to include in the analysis. Defaults to `datetime.MINYEAR`.
    max_sales_year (int, optional):
        The maximum year of property sales to include in the analysis. Defaults to the current year.
    min_area (int, optional):
        The minimum size (in square meters) of properties to consider in the analysis. Defaults to 0.
    max_area (int, optional):
        The maximum size (in square meters) of properties to consider in the analysis. Defaults to 9999.
    min_samples (int, optional):
        The minimum number of sales samples required for the analysis. Defaults to 0.
```

For example:

```shell
> python -m predict_sales_price eberts_villaby.csv 180 --min-sales-year=2010 --max-sales-year=2023 --min-area=100 --max-area=150 --min-samples=10
```

## File Descriptions

- **`scrape_latest_sales_prices.py`**: Main script for scraping sales data and estimating house prices.
- **`predict_sales_price.py`**: Main script for predicting price of house given area size.
- **`utils.py`**: Contains utility functions for processing and analyzing data. Useful for using functions in Python repl.
- **`test_address_regex.py`**: Unit tests for validating address-related functions.
- **`requirements.txt`**: Lists all the dependencies required to run the project.
