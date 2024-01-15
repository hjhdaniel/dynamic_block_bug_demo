from pandas import DataFrame

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(dynamic_block_num: int, *args, **kwargs):
    # step to load something from API/S3 here based on dynamic parent's output
    print(type(dynamic_block_num))
    print(dynamic_block_num)
    output = DataFrame(data={"num": [dynamic_block_num]})
    print("output type", type(output))
    print("output", output)
    return output


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
