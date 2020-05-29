import pytest
import pandas as pd
import os
from datapreparation import is_international, merge_one_airport

os.chdir(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
COLTYPES = {"ORIGIN_AIRPORT": object, "DESTINATION_AIRPORT": object}


class TestIsInternational:
    def test_empty_string(self):
        assert is_international("") == 0

    def test_contain_inter_uppercase(self):
        assert is_international("INTER") == 1

    def test_contain_inter_lowercase(self):
        assert is_international("inter") == 1

    def test_contain_inter_camelcase(self):
        assert is_international("inter") == 1

    def test_without_international(self):
        assert is_international("abc") == 0

    def test_correct_row(self):
        raw_data = pd.read_csv("./data/dev/flights.csv",
                               nrows=100, dtype=COLTYPES)
        airports = pd.read_csv("./data/dev/airports.csv")
        merged_data = merge_one_airport(raw_data, airports, "ORIGIN")
        assert len(merged_data) == len(raw_data)

    def test_correct_column(self):
        raw_data = pd.read_csv("./data/dev/flights.csv",
                               nrows=100, dtype=COLTYPES)
        airports = pd.read_csv("./data/dev/airports.csv")
        merged_data = merge_one_airport(raw_data, airports, "ORIGIN")
        assert len(merged_data.columns) == len(
            raw_data.columns) + len(airports.columns) - 2


raw_data = pd.read_csv("./data/dev/flights.csv",
                       nrows=100, dtype=COLTYPES)
airports = pd.read_csv("./data/dev/airports.csv")
print(f"Global Data is loaded with shape {airports.shape}")


class test_merge_airport:

    print(f"Class Data is loaded with shape {airports.shape}")

    def test_correct_row(self):
        merged_data = merge_one_airport(raw_data, airports, "ORIGIN")
        assert len(merged_data) == len(raw_data)

    # def test_correct_row(self):
    #     print(self.airports.shape)
    #     merged_data = merge_one_airport(self.raw_data, self.airports, "ORIGIN")
    #     assert len(merged_data) == len(self.raw_data)

    # def test_correct_column(self):
    #     merged_data = merge_one_airport(self.raw_data, self.airports, "ORIGIN")
    #     assert len(merged_data.columns) == len(
    #         self.raw_data.columns) + len(self.airports.columns) - 2

    # def test_keyerror_flight(self):
    #     with pytest.raises(KeyError):
    #         merge_one_airport(self.raw_data.drop(
    #             "ORIGIN_AIRPORT", axis=1), self.airports, "ORIGIN")

    # def test_keyerror_airport(self):
    #     with pytest.raises(KeyError):
    #         merge_one_airport(self.raw_data, self.airports.drop(
    #             "IATA_CODE", axis=1), "ORIGIN")
