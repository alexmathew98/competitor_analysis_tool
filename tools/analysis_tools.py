import pandas as pd

class ComparisonTool:
    """
    A tool to compare competitor prices and identify pricing strategies.
    """

    @tool("Compare Prices")
    def compare_prices(self, base_data, competitor_data):
        """
        Compares competitor prices with base prices and identifies pricing strategies.

        Parameters:
        base_data (pd.DataFrame): DataFrame containing the base product prices.
        competitor_data (pd.DataFrame): DataFrame containing the competitor product prices.

        Returns:
        pd.DataFrame: DataFrame with comparison results.
        """
        # Convert price to numeric if not already done
        base_data['price'] = pd.to_numeric(base_data['price'], errors='coerce')
        competitor_data['price'] = pd.to_numeric(competitor_data['price'], errors='coerce')

        # Merge dataframes on product name
        merged_data = pd.merge(base_data, competitor_data, on='name', suffixes=('_base', '_competitor'))

        # Calculate price differences
        merged_data['price_difference'] = merged_data['price_competitor'] - merged_data['price_base']

        return merged_data