# SwaggerPetStore

This is a FastAPI-based project that provides an API with database integration.

## Table of Contents

- Overview
- Features
- Installation
- Running the project
- Project Structure
- Testing

## Overview

My Web Application is designed to [briefly describe the purpose of your application, e.g., manage tasks, provide a RESTful API, etc.]. It allows users to [list key functionalities, e.g., create, read, update, and delete items].

## Features

- RESTful API built with FastAPI
- Database support (likely SQLite)
- Modular structure for scalability
- Includes models and test databases


## Installation

#Prerequisites

-Python 3.8+

-Virtual environment (recommended)

#Setup
   1.Create a virtual environment and activate it:
        python -m venv venv
        source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    2.Install dependencies:
        pip install -r requirements.txt

## Running the project

1.Start the FastAPI server:
      uvicorn main:app --reload
2.Open the API documentation:
      Swagger UI: http://127.0.0.1:8000/docs
      Redoc: http://127.0.0.1:8000/redoc

## Project Structure

fastapi-env/
│── main.py        # Entry point for FastAPI
│── database.py    # Database connection setup
│── model.py       # Database models
│── pet.db         # SQLite database
│── test.db        # Test database
│── requirements.txt # Dependencies list
│── .idea/         # PyCharm project files

## Testing
  To run tests, use:
         pytest
