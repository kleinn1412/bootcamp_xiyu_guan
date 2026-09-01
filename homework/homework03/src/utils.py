def get_category_summary(df):
    """summarize the value column by category"""
    return df.groupby('category')['value'].agg(['sum','mean','count'])
    