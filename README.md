# Proxy Checker
================

A Python script to check the validity of proxies in a list.

## Description
---------------

This script reads a list of proxies from a file (`proxies.txt`), checks each proxy using multiple processes, and writes the working proxies to another file (`working_proxies.txt`).

## Features
------------

* Supports HTTP, HTTPS, SOCKS4, and SOCKS5 proxies
* Uses multiple processes to speed up the checking process
* Writes working proxies to a file for easy use

## Requirements
---------------

* Python 3.x
* [requests](cci:4://c:/Users/Maari/Desktop/Project/Proxy_Checker/proxy_checker.py:0:0-14:0) library
* [socks](cci:1://c:/Users/Maari/Desktop/Project/Proxy_Checker/proxy_checker.py:34:0-48:19) library

## Usage
-----

1. Create a file named `proxies.txt` with the list of proxies in the following format:
