# Databricks notebook source
create table if not exists edp_data_catalog.edp_table_columns(
  id string,
  table_id string,
  name string,
  datatype string,
  comments string
) using delta location "/mnt/edpdlcfgsa/edp_data_catalog/edp_table_columns";

create table if not exists edp_data_catalog.edp_table_columns_extn(
  id string,    
  description string,
  classification string,
  piidata string,    
  status string
) using delta location "/mnt/edpdlcfgsa/edp_data_catalog/edp_table_columns_extn";
