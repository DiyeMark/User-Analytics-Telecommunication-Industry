import numpy as np
import pandas as pd


class DataCleaner:
    def __init__(self, df: pd.DataFrame) -> None:
        """
        Returns a DataCleaner Object with the passed DataFrame Data set as its own DataFrame
        Parameters
        ----------
        df:
            Type: pd.DataFrame
        Returns
        -------
        None
        """
        self.df = df

    def remove_unwanted_columns(self, columns: list) -> pd.DataFrame:
        """
        Returns a DataFrame where the specified columns in the list are removed
        Parameters
        ----------
        columns:
            Type: list
        Returns
        -------
        pd.DataFrame
        """
        self.df.drop(columns, axis=1, inplace=True)
        return self.df

    def change_columns_type_to(
            self, cols: list, data_type: str
    ) -> pd.DataFrame:
        """
        Returns a DataFrame where the specified columns data types are changed to the specified data type
        Parameters
        ----------
        cols:
            Type: list
        data_type:
            Type: str
        Returns
        -------
        pd.DataFrame
        """
        try:
            for col in cols:
                self.df[col] = self.df[col].astype(data_type)
        except:
            print("Failed to change columns type")

        return self.df

    def remove_single_value_columns(
            self, unique_value_counts: pd.DataFrame
    ) -> pd.DataFrame:
        """
        Returns a DataFrame where columns with a single value are removed
        Parameters
        ----------
        unique_value_counts:
            Type: pd.DataFrame
        Returns
        -------
        pd.DataFrame
        """
        drop_cols = list(
            unique_value_counts.loc[
                unique_value_counts["Unique Value Count"] == 1
                ].index
        )
        return self.df.drop(drop_cols, axis=1, inplace=True)

    def remove_duplicates(self) -> pd.DataFrame:
        """
        Returns a DataFrame where duplicate rows are removed
        Returns
        -------
        pd.DataFrame
        """
        removables = self.df[self.df.duplicated()].index
        return self.df.drop(index=removables, inplace=True)

    def fill_numeric_values(
            self, missing_cols: list, acceptable_skewness: float = 5.0
    ) -> pd.DataFrame:
        """
        Returns a DataFrame where numeric columns are filled with either median or mean based on their skewness
        Parameters
        ----------
        missing_cols:
            Type: list
        acceptable_skewness:
            Type: float
            Default value = 5.0
        Returns
        -------
        pd.DataFrame
        """
        df_skew_data = self.df[missing_cols]
        df_skew = df_skew_data.skew(axis=0, skipna=True)
        for i in df_skew.index:
            if acceptable_skewness > df_skew[i] > (
                    acceptable_skewness * -1
            ):
                value = self.df[i].mean()
                self.df[i].fillna(value, inplace=True)
            else:
                value = self.df[i].median()
                self.df[i].fillna(value, inplace=True)

        return self.df

    def fill_non_numeric_values(
            self, missing_cols: list, ffill: bool = True, bfill: bool = False
    ) -> pd.DataFrame:
        """
        Returns a DataFrame where non-numeric columns are filled with forward or backward fill
        Parameters
        ----------
        missing_cols:
            Type: list
        ffill:
            Type: bool
            Default value = True
        bfill:
            Type: bool
            Default value = False
        Returns
        -------
        pd.DataFrame
        """
        for col in missing_cols:
            if ffill is True and bfill is True:
                self.df[col].fillna(method="ffill", inplace=True)
                self.df[col].fillna(method="bfill", inplace=True)

            elif ffill is True and bfill is False:
                self.df[col].fillna(method="ffill", inplace=True)

            elif ffill is False and bfill is True:
                self.df[col].fillna(method="bfill", inplace=True)

            else:
                self.df[col].fillna(method="bfill", inplace=True)
                self.df[col].fillna(method="ffill", inplace=True)

        return self.df

    def create_new_columns_from(
            self, new_col_name: str, col1: str, col2: str, func
    ) -> pd.DataFrame:
        """
        Returns a DataFrame where a new column is created using a function on two specified columns
        Parameters
        ----------
        new_col_name:
            Type: str
        col1:
            Type: str
        col2:
            Type: str
        func:
            Type: function
        Returns
        -------
        pd.DataFrame
        """
        try:
            self.df[new_col_name] = func(self.df[col1], self.df[col2])
        except:
            print("failed to create new column with the specified function")

        return self.df

    def convert_bytes_to_megabytes(self, columns: list) -> pd.DataFrame:
        """
        Returns a DataFrame where columns value is changed from bytes to megabytes
        Args:
        -----
        columns:
            Type: list
        Returns:
        --------
        pd.DataFrame
        """
        try:
            megabyte = 1 * 10e5
            for col in columns:
                self.df[col] = self.df[col] / megabyte
                self.df.rename(
                    columns={col: f"{col[:-7]}(MegaBytes)"}, inplace=True
                )

        except:
            print("failed to change values to megabytes")

        return self.df

    def fix_outlier(self, column: str) -> pd.DataFrame:
        """
        Returns a DataFrame where outlier of the specified column is fixed
        Parameters
        ----------
        column:
            Type: str
        Returns
        -------
        pd.DataFrame
        """
        self.df[column] = np.where(
            self.df[column] > self.df[column].quantile(0.95),
            self.df[column].median(),
            self.df[column],
        )

        return self.df

    def fix_outlier_columns(self, columns: list) -> pd.DataFrame:
        """
        Returns a DataFrame where outlier of the specified columns is fixed
        Parameters
        ----------
        columns:
            Type: list
        Returns
        -------
        pd.DataFrame
        """
        try:
            for column in columns:
                self.df[column] = np.where(
                    self.df[column] > self.df[column].quantile(0.95),
                    self.df[column].median(),
                    self.df[column],
                )
        except:
            print("Cant fix outliers for each column")

        return self.df

    def save_clean_data(self, name: str):
        """
        The objects dataframe gets saved with the specified name
        Parameters
        ----------
        name:
            Type: str
        Returns
        -------
        None
        """
        try:
            self.df.to_csv(name)

        except:
            print("Failed to save data")
