# Refer example - https://github.com/definitive-io/crewai-groq/blob/main/app.py

import pandas as pd

class DataProcessingTool:
    """
    A tool to process, organize, and clean data received from the scraping agent.
    """

    def __init__(self):
        """
        Initializes the DataProcessingTool.
        """
        pass

    @tool("Pre-process which gets scraped from the website")
    def preprocess_data(self, raw_data):
        """
        Cleans and preprocesses raw scraped data.

        Parameters:
        raw_data (list of dict): Raw data collected by the scraping agent.

        Returns:
        pd.DataFrame: Cleaned and organized data.
        """
        # Convert raw data to DataFrame
        df = pd.DataFrame(raw_data)

        # Drop duplicates
        df.drop_duplicates(inplace=True)

        # Handle missing values
        df.fillna(method='ffill', inplace=True)

        # Convert price to numeric, handle currency symbols
        df['price'] = df['price'].replace('[\$,]', '', regex=True).astype(float)

        # Clean and standardize the offer column
        df['offer'] = df['offer'].str.lower().str.strip()

        return df

    @tool("Organize and compile the gathered data")
    def organize_data(self, df):
        """
        Organizes the data by sorting and setting appropriate indices.

        Parameters:
        df (pd.DataFrame): Cleaned data.

        Returns:
        pd.DataFrame: Organized data.
        """
        # Sort data by price
        df.sort_values(by='price', inplace=True)

        # Reset index
        df.reset_index(drop=True, inplace=True)

        return df

    @tool("Aggregate the data")
    def aggregate_data(self, df):
        """
        Aggregates data to provide summary statistics.

        Parameters:
        df (pd.DataFrame): Organized data.

        Returns:
        pd.DataFrame: Aggregated data with summary statistics.
        """
        # Group by product name and calculate average price and offer count
        aggregated_df = df.groupby('name').agg(
            average_price=pd.NamedAgg(column='price', aggfunc='mean'),
            offer_count=pd.NamedAgg(column='offer', aggfunc='count')
        ).reset_index()

        return aggregated_df
