# Databricks notebook source
print("Hello World!")

# COMMAND ----------

# MAGIC %sql 
# MAGIC Select "Hello world from SQL!"

# COMMAND ----------

# MAGIC
# MAGIC
# MAGIC %md
# MAGIC
# MAGIC #Title
# MAGIC ## Tite 2
# MAGIC ### Title 3
# MAGIC
# MAGIC text with a **bold** and *italicized* in it.
# MAGIC
# MAGIC Ordered list
# MAGIC 1. once
# MAGIC 2. two
# MAGIC 3. three
# MAGIC
# MAGIC Unordered list
# MAGIC * apple
# MAGIC * peaches
# MAGIC * bananas
# MAGIC
# MAGIC Images:
# MAGIC ![Associate-badge](http://www.databricks.com/wp-content/uploads/2022/04/associate-badge-eng.svg)
# MAGIC
# MAGIC Tables:
# MAGIC |User_id|user_name|
# MAGIC |-------|---------|
# MAGIC |    1  |   Adam  |
# MAGIC |    2  |   Sarah |
# MAGIC |    3  |   John  |
# MAGIC
# MAGIC Links or Embedded HTML: <a href = "https://docs.databricks.com/en/notebooks/notebooks-manage.html" target='_blank'> Managing notebooks documentation</a>
# MAGIC
# MAGIC

# COMMAND ----------

# MAGIC %run ./Include/Setup

# COMMAND ----------

print(full_name)

# COMMAND ----------

# MAGIC %fs ls '/databricks-datasets'

# COMMAND ----------

dbutils.help()

# COMMAND ----------

dbutils.fs.help()

# COMMAND ----------

files = dbutils.fs.ls('./databricks-datasets')
print(files)

# COMMAND ----------

display(files)

# COMMAND ----------


