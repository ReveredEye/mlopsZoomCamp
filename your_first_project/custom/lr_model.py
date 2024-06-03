import pandas as pd
from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LinearRegression
from sklearn.metrics import root_mean_squared_error

if 'custom' not in globals():
    from mage_ai.data_preparation.decorators import custom
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@custom
def transform_custom(train_data, **kwargs):
    """
    args: The output from any upstream parent blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    # Specify your custom logic here
    featDict = train_data[['PULocationID', 'DOLocationID']].to_dict(orient = 'records')
    dv = DictVectorizer()#sparse = False <- Use if small dataset
    dv.fit(featDict)
    featMat = dv.transform(featDict)
    lr_model = LinearRegression()
    lr_model.fit(featMat, train_data['duration'])
    print(lr_model.intercept_)

    return dv, lr_model


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
