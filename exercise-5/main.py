import psycopg2 
import csv
def main():
    host = "localhost"
    database = "mydatabase"
    user = "lucy"
    pas = "123456"
    conn = psycopg2.connect(host=host, database=database, user=user, password=pas)
    # your code here
    conn.autocommit = True
    cursor = conn.cursor()
    try:
        accounts = 'CREATE TABLE ACCOUNTS(customer_id INT  PRIMARY KEY, first_name  varchar(10), last_name varchar(10), address_1 varchar(50), address_2 varchar(50),city varchar(10) ,stat varchar(10), zip_code int , join_date date)'
        products='CREATE TABLE PRODUCTS(product_id int PRIMARY KEY , product_code char(3), product_description varchar(50))'
        transactions ="CREATE TABLE TRANSACTIONS(transaction_id varchar(50) , transaction_date date, product_id int, product_code int , product_description varchar(50), quantity int , account_id int , FOREIGN KEY (account_id) REFERENCES ACCOUNTS(customer_id), FOREIGN KEY (product_id) REFERENCES PRODUCTS(product_id))"
        cursor.execute(accounts)
        cursor.execute(products)
        cursor.execute(transactions)
    except:
        pass
    with open('/Users/macbook/Documents/tailieu/data-engineering-practice/exercise-4/Crawling-prac/exercise-5/data/accounts.csv','r') as file:
        cursor.copy_expert("COPY ACCOUNTS FROM STDOUT WITH CSV HEADER", file)
    with open('exercise-5/data/products.csv','r') as file1:
        cursor.copy_expert("COPY PRODUCTS FROM STDOUT WITH CSV HEADER", file1)
    with open('/Users/macbook/Documents/tailieu/data-engineering-practice/exercise-4/Crawling-prac/exercise-5/data/transactions.csv','r') as file2:
        cursor.copy_expert("COPY TRANSACTIONS FROM STDOUT WITH CSV HEADER", file2)
    conn.close()
if __name__ == "__main__":
    main()