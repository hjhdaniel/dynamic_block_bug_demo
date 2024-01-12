# Description

This repo serves to recreate the following bug from mage-ai dynamic block runs with a simple demo pipeline:

```
Error

Traceback (most recent call last):

  File "/usr/local/lib/python3.10/site-packages/mage_ai/data_preparation/executors/block_executor.py", line 625, in execute

    result = __execute_with_retry()

  File "/usr/local/lib/python3.10/site-packages/mage_ai/shared/retry.py", line 54, in retry_func

    raise e

  File "/usr/local/lib/python3.10/site-packages/mage_ai/shared/retry.py", line 38, in retry_func

    return func(*args, **kwargs)

  File "/usr/local/lib/python3.10/site-packages/mage_ai/data_preparation/executors/block_executor.py", line 598, in __execute_with_retry

    return self._execute(

  File "/usr/local/lib/python3.10/site-packages/mage_ai/data_preparation/executors/block_executor.py", line 1085, in _execute

    result = self.block.execute_sync(

  File "/usr/local/lib/python3.10/site-packages/mage_ai/data_preparation/models/block/__init__.py", line 1295, in execute_sync

    raise err

  File "/usr/local/lib/python3.10/site-packages/mage_ai/data_preparation/models/block/__init__.py", line 1213, in execute_sync

    output = self.execute_block(

  File "/usr/local/lib/python3.10/site-packages/mage_ai/data_preparation/models/block/__init__.py", line 1519, in execute_block

    outputs = self._execute_block(

  File "/usr/local/lib/python3.10/site-packages/mage_ai/data_preparation/models/block/__init__.py", line 1675, in _execute_block

    outputs = self.execute_block_function(

  File "/usr/local/lib/python3.10/site-packages/mage_ai/data_preparation/models/block/__init__.py", line 1714, in execute_block_function

    output = block_function_updated(*input_vars, **global_vars)

  File "<string>", line 139, in transform_df

AttributeError: 'NoneType' object has no attribute 'index'
```

# Steps to run and reproduce error
1) clone and cd into the repo
2) create python venv, pip install mage-ai
```
pip3 install mage-ai
```
3) run project
```
mage start dynamic_block_bug_demo
```
4) `Run@once` the `demo` pipeline
  
