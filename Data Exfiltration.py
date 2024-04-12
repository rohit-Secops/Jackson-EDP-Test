# Databricks notebook source
# MAGIC %sql
# MAGIC create table if not exists edp_data_catalog.edp_table_columns(
# MAGIC   id string,
# MAGIC   table_id string,
# MAGIC   name string,
# MAGIC   datatype string,
# MAGIC   comments string
# MAGIC ) using delta location "/mnt/edpdlcfgsa/edp_data_catalog/edp_table_columns";
# MAGIC
# MAGIC create table if not exists edp_data_catalog.edp_table_columns_extn(
# MAGIC   id string,    
# MAGIC   description string,
# MAGIC   classification string,
# MAGIC   piidata string,    
# MAGIC   status string
# MAGIC ) using delta location "/mnt/edpdlcfgsa/edp_data_catalog/edp_table_columns_extn";
