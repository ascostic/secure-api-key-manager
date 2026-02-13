Secure API Key Manager

This project is a backend system that allows users to securely generate and manage API keys.

It demonstrates how real-world systems handle authentication and protect access to sensitive endpoints.

What It Does

Users log in using JWT authentication.

Authenticated users can generate API keys.

API keys are securely stored using hashing (not saved in plain text).

Protected endpoints can only be accessed using a valid API key.

Expired or revoked keys are automatically blocked.

How It Works

A user logs in and receives a JWT access token.

Using that token, the user can create an API key.

The API key is generated securely and hashed before being stored.

To access protected data, the client must send the API key in the request header.

The system verifies the key and grants or denies access.

Security Features

Cryptographically secure key generation

SHA256 hashed key storage

Custom API key authentication class

Expiration handling

Revocation-ready structure

Technologies Used

Python

Django

Django REST Framework

Simple JWT

Purpose

This project demonstrates backend development aligned with security principles, including authentication separation, secure key storage, and controlled access to APIs.