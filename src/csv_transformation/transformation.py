import polars as pl


class TransformData:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def write_csv(self, df: pl.DataFrame, output_path: str, file_name: str):
        df.write_csv(output_path + file_name)

    def read_csv(self, input_path: str, file_name: str) -> pl.DataFrame:
        df = pl.read_csv(input_path + file_name)
        return df

    def main(self):
        file_name1 = 'address_data.csv'
        address_df = self.read_csv(self.file_path, file_name1)
        file_name2 = "survey_data.csv"
        survey_df = self.read_csv(self.file_path, file_name2)
        address_df = address_df.with_columns(pl.lit("spain").alias('LANGUAGE')).unique()
        joined_df= address_df.join(survey_df, on="RESPONSE_ID", how="left", coalesce=True)
        final_df= joined_df.filter(pl.col('CITY') == "Toluca")
        self.write_csv(final_df, self.file_path, "output.csv")


if __name__ == "__main__":
    file_path = 'C:/Users/nara1005/Downloads/'
    samp = TransformData(file_path)
    samp.main()
