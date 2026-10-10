import os
import re

import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import pendulum

from sqlalchemy import create_engine, text
from datetime import datetime
from io import BytesIO

from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator

# Пароль от пользователя PostgreSQL
# PgAdmin = 'qwerty123'
# Username = "postgres"
# Host = "localhost"
# Port = "5432"

# engine = create_engine("postgresql://postgres:qwerty123@localhost:5432/postgres")

# DAG - весь workflow/pipeline
# Task - один шаг pipeline
# Operator - способ выполнения Task
# Scheduler	- решает, когда запускать задачи
# Executor - определяет, как задачи выполняются
# API Server / UI - управление Airflow и веб-интерфейс
# Metadata DB - хранит состояние DAG, запусков, задач
# DAG Run - конкретный запуск DAG
# Task Instance - конкретный запуск отдельной Task
# XCom - передача небольших данных между Task

# Как запустить Airflow?
