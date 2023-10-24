import os
import inject

from flask import Flask
from infrastructure.adapters import MySqlAdapter
from domain.repositories import RepositoryInterface

def configure_application(application: Flask) -> None:
    application.config.update(
        DATABASE_URI=os.getenv('DATABASE_URI')
        # DATABASE_URI="mysql+mysqlconnector://root:password@222.239.193.15:30010/iotdb?charset=utf8"
    )
    
def configure_inject(application: Flask) -> None:
    def config(binder: inject.Binder) -> None:
            binder.bind(RepositoryInterface, MySqlAdapter(application.config['DATABASE_URI']))
            
    inject.configure(config)

