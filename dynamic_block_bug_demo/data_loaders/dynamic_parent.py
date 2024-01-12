import pandas as pd

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):
    num_range = range(10)
    dynamic_block_nums = [num for num in num_range]
    dynamic_block_uuids = [{"block_uuid": f"{num}"} for num in dynamic_block_nums]
    return [dynamic_block_nums, dynamic_block_uuids]


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
