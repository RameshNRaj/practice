import os.path

import polars as pl


class RetailSales:
    def __init__(self, input_path: str, output_path: str ):
        self.input_path = input_path
        self.output_path = output_path

    def write_csv(self, df: pl.DataFrame, output_path: str, file_name: str):
        df.write_csv(output_path + file_name)

    def read_csv(self, input_path: str, file_name: str) -> pl.DataFrame:
        df = pl.read_csv(input_path + file_name)
        return df

    def main(self):
        file_name = "retail_sales_dataset.csv"
        df = self.read_csv(self.input_path, file_name)
        df1 = df.group_by(['Gender', 'Product Category']).agg(pl.sum('Total Amount'))
        if not os.path.exists(self.output_path):
            os.mkdir(self.output_path)
        self.write_csv(df1, self.output_path, "sales_output.csv")
        return df1


if __name__ == "__main__":
    input_path = 'C:/Users/nara1005/Downloads/'
    output_path = 'C:/Users/nara1005/Downloads/output/'
    run = RetailSales(input_path, output_path)
    run.main()
