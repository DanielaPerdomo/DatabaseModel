import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)
    subscription_date = Column(String(50), nullable=False)
    #Relacion con la tabla de Favorites (Child)
    favorites = relationship("Favorites", back_populates="users")

class Characters(Base):
    __tablename__ = 'characters'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    description = Column(String(250), nullable=False)
    #Relacion con la tabla de Favorites (Child)
    favorites = relationship("Favorites", back_populates="characters")

class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    population = Column(Integer, nullable=False)
    #Relacion con la tabla de Favorites (Child)
    favorites = relationship("Favorites", back_populates="planets")
    
class Favorites(Base): #(Father)
    __tablename__ = 'favorites'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    id_user = Column(ForeignKey("users.id")) 
    users = relationship( "Users", back_populates = "favorites")
    #Relacion con la tabla de Characters (Child)
    id_character = Column(ForeignKey("characters.id"))
    character = relationship("Characters", back_populates = "favorites")
    #Relacion con la tabla de Planets (Child)
    id_planets = Column(ForeignKey("planets.id"))
    planets = relationship( "Planets", back_populates = "favorites")

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')