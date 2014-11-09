HW2
=========================================================
<p>Given a query string (either in English or Chinese) as the input, connect to iservDB and retrieve twitter data containing the query string. Finally print out every matching text ,its user_id, user_name (defined in iservDB) and sort according to the user ID in the ascendant order. Please show the result in the table form as the following example, and print the table out in console</p>

Requirement:
-------------------------------------------------------
psycopg2:

- Ubuntu

	sudo apt-get install python-psycopg2

Usage:
-------------------------------------------------------
	python IKDDhw2.py <query string>

Example:
-------------------------------------------------------
	python IKDDhw2.py 王建明
