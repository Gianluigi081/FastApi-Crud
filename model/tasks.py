from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String
from sqlalchemy.orm import relationship
from config.db import engine, meta_data

tasks = Table("tasks", meta_data,
              Column("id", Integer, primary_key=True),
              Column("title", String(255), nullable=False),
              Column("description", String(255), nullable=False))

meta_data.create_all(engine)